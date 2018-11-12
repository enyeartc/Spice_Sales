
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk.data
import numpy as np
import pandas as pd
import savory_orders
import savory_items
import savory_blends
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class SModels(object):
    def __init__(self, reload=0):
        self.vectorizer = None
        self.vectors = None
        self.recipes_ing = pd.read_csv('../data/IngSpiceList.csv')
    def process_data_tfidf(self):
        # DO TFIDF TRANSFORMATION
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.vectors = self.vectorizer.fit_transform(self.recipes_ing.spicelist).toarray()
        self.words = self.vectorizer.get_feature_names()


    def fit_nmf(self,k):
        nmf = NMF(n_components=k)
        nmf.fit(self.vectors)
        self.W = nmf.transform(self.vectors);
        self.H = nmf.components_;
        return nmf.reconstruction_err_

    def fit_pca(self,k,mat):
        scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
        # X_scaled = scaler.fit_transform(mat) # standardize data
        pca = PCA(n_components=k) #pca object
        X_pca = pca.fit_transform(mat)
        if(k ==2):
            fig, ax = plt.subplots(1, 1, figsize=(8, 6))
            ax.scatter(X_pca[:, 0], X_pca[:, 1], c='y',
                       cmap=plt.cm.Set1, edgecolor='k', s=10)
            ax.set_title("First two PCA directions")
            ax.set_xlabel("1st eigenvector (PC1)")
            ax.set_ylabel("2nd eigenvector (PC2)")
            plt.savefig('../images/PCA.png')
        return(X_pca)
    def plot_features(self,df):
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
    def print_spice_by_feature(self):
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
    def print_rec_of_interest(self,num):

        df = self.recipes_ing[self.W[:,num]>.03]
        print('Feature',num,'--------------')
        df = df[0:10]
        print(df.spicelist)
        print(df.title)
if __name__ == '__main__':
    s_model = SModels()
    s_model.process_data_tfidf()
    s_model.fit_nmf(50)
    df1 = s_model.print_spice_by_feature()
    s_model.plot_features(df1)
    
    s_model.print_rec_of_interest(7)
    s_model.print_rec_of_interest(12)
    s_model.print_rec_of_interest(21)
    s_model.print_rec_of_interest(38)
    s_model.print_rec_of_interest(45)



    # error = [fit_nmf(i,vectors) for i in range(1,60)]
    # plt.plot(range(1,60), error)
    # plt.xlabel('k')
    # plt.ylabel('Reconstruction Error')
    # plt.title('NMF')
    # plt.savefig('../images/Reconstruction.png')

    #fit_pca(2,vectors)
