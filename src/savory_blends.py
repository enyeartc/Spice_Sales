import os
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import missingno as msno
import math
import savory_utils
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


class SBlends(object):
    '''
      SItems will contain a list of
    '''

    def __init__(self, reload=0):

        self.reload = reload
        self.data = self.load_blend_data()

    def vectorizeKmeans(self,n_clusters = 6):
        cv = CountVectorizer(stop_words='english')
        self.vectorized = cv.fit_transform(self.data.Ingredients)

        vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidfed = vectorizer.fit_transform(self.data.Ingredients)

        self.features = vectorizer.get_feature_names()
        kmeans = KMeans(n_clusters = n_clusters)
        kmeans.fit(self.tfidfed)

        print("\n2) cluster centers:")
        print(kmeans.cluster_centers_)

        # 3. Find the top 10 features for each cluster.
        top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
        print("\n3) top features (words) for each cluster:")
        for num, centroid in enumerate(top_centroids):
            print("%d: %s" % (num, ", ".join(self.features[i] for i in centroid)))

        print("\nRandom sample of titles in each cluster")
        X = self.vectorized
        assigned_cluster = kmeans.transform(X).argmin(axis=1)
        for i in range(kmeans.n_clusters):
            cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
            sample_articles = np.random.choice(cluster, 2, replace=False)
            print("cluster %d:" % i)
            for article in sample_articles:
                print("    %s" % self.data.ix[article]['item_desc'])


    def remove_product_string(self,x):
        y = x.replace('Discontinued Size - ', '')
        y = y.replace('-8floz Plastic', '')
        y = y.replace('-16oz Bag ', '')
        y = y.replace('Refill ', '')
        y = y.replace('-1oz Bag', '')
        y = y.replace('-1/2 Cup', '')
        y = y.replace('-1/2', '')
        y = y.replace('1 Cup', '')
        y = y.replace('2 Cup', '')
        y = y.replace('3 Cup', '')
        y = y.replace('-8floz', '')
        y = y.replace('-8', '')
        y = y.replace(' oz ', '')
        y = y.replace(' oz', '')
        y = y.replace('Medium', '')
        y = y.replace('Small', '')
        y = y.replace('Jar', '')
        y = y.replace(' oz ', '')
        y = y.replace(' oz', '')
        y = y.replace('Refill', '')
        y = y.replace('(ORG-S) - ', '')
        y = y.replace('- Bag', '')
        y = y.replace(' Bag', '')
        y = y.replace('-3', '')
        y = y.replace('-5', '')
        y = y.replace('-2', '')
        y = y.replace('-4', '')
        y = y.replace('-4oz', '')
        y = y.replace('Bulbs', '')
        y = y.replace('-12', '')
        y = y.replace('floz', '')
        y = y.replace('Glass', '')
        y = y.replace('Bottle', '')
        y = y.replace('Bulbs', '')
        y = y.replace('-1 1/', '')
        y = y.replace('Large', '')
        y = y.replace('Bulbs', '')
        y = y.replace('(Clearance)', '')
        y = y.replace('(ORG-S) oz', '')
        y = y.replace('(ORG-S)', '')
        y = y.replace('-16oz', '')
        y = y.replace('-4oz', '')
        y = y.replace('-2oz', '')
        y = y.replace('-1/4oz', '')
        y = y.replace('-1oz', '')
        y = y.replace('-', '')
        y = y.replace(' oz', '')
        y = y.replace(' -Tube', '')
        y = y.replace(' -6.5oz', '')
        y = y.replace(' Canister', '')
        y = y.replace(' 6oz', '')
        y = y.replace(' 6.5oz', '')
        y = y.replace('êgarlic', 'garlic')
        y = y.replace('êspanish', 'spanish')
        y = y.replace('êwhite', 'white')
        return(y)

    def load_clean_blend(self):
        df_blend = pd.read_csv('../data/blends.csv' ,encoding = "ISO-8859-1")
        df_blend['item_desc'] = [self.remove_product_string(x) for x in df_blend['LineItemName']]
        df_blend = df_blend[pd.notna(df_blend['Ingredients'])]
        df_blend.to_csv('../data/clean_blend.csv')
        return(df_blend)
    def load_blend_data(self):
        if self.reload == 1:
            return(self.load_clean_blend())
        df_blend = pd.read_csv('../data/clean_blend.csv')
        return(df_blend)


if __name__ =='__main__':
    z = 'Discontinued Size - Ajowan Seeds -1oz Bag'
    #loadcleanitem()
    blends = SBlends()
