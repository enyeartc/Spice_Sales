
from sklearn.feature_extraction.text import TfidfVectorizer
# import nltk.data
import numpy as np
import pandas as pd
import savory_orders
import savory_items
import savory_blends
import savory_utils
import savory_recipes
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import math
from ast import literal_eval

class SModels(object):
    # SModels is a class that will utilize several other classes items, blends, and orders
    # this script does the main processing for this project
    def __init__(self, reload=0):
        self.vectorizer = None
        self.reload = reload
        self.vectors = None
        self.nmf = None
        self.recipes_ing = None
        self.spices = None
        self.create_ing_list()
        # if(self.reload == 1):
        #    self.process_data_tfidf()
        #    self.fit_nmf(50)
        #    self.find_blend()

    def create_ing_list(self):
        #  Create Ingredient List - really a DataFrame
        #  this function will combine the recipies data with the blend data
        #  to create a full dataframe then save it into a csv for future use
        if(self.reload == 1):
            items = savory_items.SItems()
            self.spices = items.spices
            recipes = savory_recipes.SRecipes()
            blends = savory_blends.SBlends()
            dfmodel = col_names =  ['title', 'ingredients', 'url']
            dfmodel1 = recipes.data[['title', 'ingredients', 'url']]
            dfmodel2 = blends.data[['LineItemName', 'Ingredients']]
            dfmodel2.rename(index=str, columns={"LineItemName": "title", "Ingredients": "ingredients"}, inplace=True)
            dfmodel2['url'] = 'savoryblend'
            result = pd.merge(dfmodel1, dfmodel2, on=['title','ingredients','url'], how='outer')
            #  now only include words in the result database that are spices
            result['spicelist'] = [savory_utils.inglist(items.spices,rec) for rec in result.ingredients]
            # save it off so in the future it will not need to be re-generated
            result.to_csv('../data/IngSpiceList.csv')
        self.recipes_ing = pd.read_csv('../data/IngSpiceList.csv')
    def process_data_tfidf(self):
        # DO TFIDF TRANSFORMATION
        print('process TFIDF')
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.vectors = self.vectorizer.fit_transform(self.recipes_ing.spicelist).toarray()
        self.words = self.vectorizer.get_feature_names()

    def fit_nmf(self,k):
        #  This function will run the NMF model that will take the TfIDF
        #  information and create the W and H matrices
        print('fit_nmf')
        self.nmf = NMF(n_components=k)
        self.nmf.fit(self.vectors)
        self.W = self.nmf.transform(self.vectors);
        self.H = self.nmf.components_;
        return self.nmf.reconstruction_err_

    def fit_pca(self,k,mat):
        #  This function will run the PCA model that will take the TfIDF
        #  information and return the fit_transform result if it is
        #  using 2 priciple components then it will also create a graph
        print('fit_pca')
        scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
        # X_scaled = scaler.fit_transform(mat) # standardize data
        pca = PCA(n_components=k) #pca object
        X_pca = pca.fit_transform(mat)
        if(k ==2):
            fig, ax = plt.subplots(1, 1, figsize=(8, 6))
            ax.scatter(X_pca[:, 0], X_pca[:, 1], c='y',
                       cmap=plt.cm.Set1, edgecolor='k', s=10)
            ax.set_title("PCA two Principal components")
            ax.set_xlabel("1st eigenvector (PC1)")
            ax.set_ylabel("2nd eigenvector (PC2)")
            plt.savefig('../images/PCA.png')
        return(X_pca)
    def plot_features(self,df):
        #  This function will create a graph showing a comparison of the
        #  blends to the recipes

        fig, ax = plt.subplots()
        width = 0.35  # the width of the bars

        rects1 = ax.bar( df.feature,df.blends,
                        color='SkyBlue', label='Blends')
        rects2 = ax.bar( df.feature, df.recipes/100,width,
                        color='IndianRed', label='Recipies')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Blends or Recipies/100')
        ax.set_xlabel('Features')
        ax.set_title('Number of Recipies/Blends by feature')
        # ax.set_xticks(df.feature)
        #ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

        ax.legend()
        plt.savefig('../images/Features.png')
    def print_spice_by_feature(self,amount = .03):
        #  This function is for data analysis
        #  it prints out any recipe or blend that has a value greater
        #  that 'amount'  for a latent topic in the H matrix
        #  then uses the W matrix and the list of recipes to print out
        #  the data
        amount = .03
        npwords = np.array(self.words)
        blend_rec_feat  = pd.DataFrame(columns=['feature','blends','recipes'])

        for i in range(self.H.shape[0]):
           print('-----',i)
           print(npwords[tuple([self.H[i]>amount])])
           b1 = np.sum(self.W[self.recipes_ing['url']=='savoryblend'][:,i]>amount)
           r1 = np.sum(self.W[self.recipes_ing['url']!='savoryblend'][:,i]>amount)
           print('Blends',b1)
           print('Recipies',r1)
           blend_rec_feat = blend_rec_feat.append({'feature':i,'blends':b1,'recipes':r1}, ignore_index=True)

        return(blend_rec_feat)
    def print_rec_of_interest(self,num,count = 10,amount = .03):
        #  This function is for data analysis pass in a Latent Topic - num
        #  and it will print out spices and recipies associated with it
        df = self.recipes_ing[self.W[:,num]>amount]
        print('Feature',num,'--------------')
        df = df[0:count]
        print(df.spicelist)
        print(df.title)
    def print_recipe(self,num):
        #  Print recipies based on the number
        r1 = self.recipes_ing.iloc[num]
        return(r1)
    def print_blend(self,num):
        #  Blends are part of the same recipe set so this function
        #  find the blend relating to the 'num' parameter
        b1 = self.recipes_ing[self.recipes_ing['url']=='savoryblend'].iloc[num]
        return(b1)
    def cosine_similarity(self,vec1, vec2):

        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        norm_prod = norm1 * norm2

        return vec1.T.dot(vec2) / norm_prod
    def find_blend (self):
        #  this funciton loops thorugh all the recipes and all the Blends
        #  and finds the blend with the closest cosine simularity and
        #  creates two additional columns int the datafram blend_rec_rec
        #  which is blend recomendation and the cosine similarity
        print('find_blend')
        if(self.reload == 1):
            blend_rec = []
            cosinesim = []
            Blends = self.W[self.recipes_ing['url']=='savoryblend']
            for i in range(len(self.recipes_ing)):
                sim = [self.cosine_similarity(self.W[i],s) for s in Blends]
                sim  = [0 if math.isnan(z) else z for z in sim]
                blend_rec.append(np.argmax(sim))
                cosinesim.append(np.max(sim))
            self.recipes_ing['blend_rec'] = blend_rec
            self.recipes_ing['cosinesim'] = cosinesim

            self.recipes_ing.to_csv('../data/IngSpiceListCosine.csv')
        else:
            self.recipes_ing = pd.read_csv('../data/IngSpiceListCosine.csv')
    def find_recipe_low_match (self,cosinesim = .3, listlen = 4):
        #  this is a data analysis function showing recipies with
        #  ingredients but low cosine simularity showing Recipies
        #  that really have a poor match
        print(self.recipes_ing[(self.recipes_ing.cosinesim < cosinesim) &
              (self.recipes_ing.spicelist.apply(literal_eval).apply(len) > listlen)])

    def find_recipe_high_match (self,cosinesim = .8, listlen = 4):
        #  opposite of above recipies with a good blend match
        print(self.recipes_ing[(self.recipes_ing.cosinesim > cosinesim) & (self.recipes_ing.cosinesim < .99) &
              (self.recipes_ing.spicelist.apply(literal_eval).apply(len) > listlen)])
    def find_recipe_DoNotUse (self):
        # This method is not finished and will be removed before publication
        return(1)
        #self.recipes_ing = pd.read_csv('../data/IngSpiceListCosine.csv')
        blend_ing = self.recipes_ing[self.recipes_ing['url']=='savoryblend']
        recipe_data[recipe_data.cosinesim < .4]
        blend_data.iloc[1]
        recipe_data[(recipe_data.cosinesim < .4) & (recipe_data.cosinesim > .3)]
        recipe_data[(recipe_data.cosinesim < .3) & (recipe_data.spicelist.apply(literal_eval).apply(len) > 4)]
        # s_model.recipes_ing[(s_model.recipes_ing.cosinesim >.7) & (s_model.recipes_ing.spicelist.apply(literal_eval).apply(len) > 4)]


    def process_customer(self, customer= 3196):
        # This method is not finished and will be updated before publication
        orders = savory_orders.SOrders()

        # P = orders.data[orders.data.LoginId   == customer].LineItemName
        # cust_ing = [p for p in P]
        #
        # s_model.recipes_ing[s_model.recipes_ing.title.str.startswith('Mt. Elbert')]
        # result['spicelist'] = [savory_utils.inglist(items.spices,rec) for rec in result.ingredients]



if __name__ == '__main__':
    s_model = SModels(reload = 1)
    if(s_model.reload ==1):
        s_model.process_data_tfidf()
        s_model.fit_nmf(50)
        # df1 = s_model.print_spice_by_feature()
        # s_model.plot_features(df1)
    #
        s_model.find_blend()
