import os
import datetime
import pandas as pd
import numpy as np
import savory_utils
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import missingno as msno
import math
from pymongo import MongoClient, errors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class SOrders(object):
    '''
      SItems will contain a list of
    '''

    def __init__(self, reload=False):

        self.reload = reload
        self.dataloaded = False
        self.data = None
        self.loaddata()


    def state_fix(self,x):
        switcher = {
            'ALABAMA' : 'AL',
            'COLORADO': 'CO',
            'Colorado': 'CO',
            'CALIFORNIA': 'CA',
            'GEORGIA': 'GA',
            'HAWAII': 'HI',
            'TEXAS': 'TX',
            'MASSACHUSETTS': 'MA',
            'Massachusetts': 'MA',
            'SOUTH CAROLINA': 'SC',
            'MISSOURI': 'MO',
            'VIRGINIA': 'VI',
            'OREGON': 'OR',
            'OREGON ': 'OR',
            'UTAH': 'UT',
            'OKLAHOMA': 'OK',
            'Tennessee': 'TN',
            'NEW JERSEY': 'NJ',
            'New Mexico': 'NM',
            'ALASKA': 'AK',
            'Michigan': 'MI',
            'WISCONSIN': 'WI',
            'WASHINGTON': 'WA',
            'WASHINGTON ': 'WA',
            'FLORIDA': 'FL',
            'Washington': 'WA',
            'IDAHO': 'ID',
            'CALIFORNIA': 'CA',
            'INDIANA': 'IN',
            'Florida': 'FL',
            'WYOMING': 'WY',
            'Washington': 'WA',
            'NEW YORK': 'NY',
            'OHIO': 'OH',
            'PENNSYLVANIA': 'PA',
            'WASHINGTON': 'WA',
            'CONNECTICUT': 'CT',
            'NORTH DAKOTA': 'ND',
            'ARIZONA': 'AZ',
            'MAINE': 'MA',
            'CA ': 'CO',
            'ILLINOIS': 'IL',
            'TENNESSEE': 'TN',
            'DELAWARE': 'DE',
            'NEVADA': 'NV',
            'WISCONSIN ': 'WI',
            'NORTH CAROLINA': 'NC',
            'AE': 'NA',
            'AS': 'NA',
            'AS': 'NA',
            'FM': 'NA',
            'FM': 'NA',
            'BA': 'NA',
            'HA': 'NA',
            'TE': 'NA',
            'NB': 'NA',
            'MH': 'NA',
            'IO': 'NA',
            'AB': 'NA',
            'MP': 'NA',
            'DI': 'NA',
            'PU': 'NA',
            'BC': 'NA',
            'GU': 'NA',
            'PW': 'NA',
            'MS': 'NA',
            '34': 'NA'
        }
        if isinstance(x, float) or isinstance(x, int):
            return('NA')
        else:
            x = x.upper()
            return switcher.get(x, x)
    def herbs_spices(self):
        return(self.data[self.data['SiteDisplayName']=='Herbs & Spices'].LineItemName.unique())
    def herbs_spices_id(self):
        return(self.data[self.data['SiteDisplayName']=='Herbs & Spices'].ItemId.unique())
    def spice_blends(self):
        return(self.data[self.data['SiteDisplayName']=='Spice Blends'].LineItemName.unique())
    def extracts(self):
        return(self.data[self.data['SiteDisplayName']=='Extracts'].LineItemName.unique())
    def gift_packs(self):
        return(self.data[self.data['SiteDisplayName']=='Gift Packs'].LineItemName.unique())
    def specialty_items(self):
        return(self.data[self.data['SiteDisplayName']=='Specialty Items'].LineItemName.unique())
    def get_desc_fromID(self,ID,df_item):
        if len(df_item[df_item['ItemId']==ID])>0:
            return(df_item[df_item['ItemId']==ID].item_desc.values[0])
        else:
            return(' ')

    def load_desc(self):
        df_item = pd.read_csv('../data/clean_item.csv')
        self.data['item_desc'] = [self.get_desc_fromID(x,df_item) for x in self.data['ItemId']]
    def loadcleanorder(self):
        df_order = pd.read_csv('../data/order.csv')
        #df_order  = df_order.iloc[:4,]
        # Some Strange data for a few HI records
        #df_order.loc[df_order['BillingState'] == '96', 'BillingState'] = 'HI'
        df_order.drop([373969, 373970],inplace= True)
        df_order.loc[df_order['ShippingState']=='96768','ShippingState'] = 'HI'
        #df_order.loc[df_order['BillingZipCode'] == 'HI', 'BillingZipCode'] = '96768'

        df_order['ShippingState'] = [self.state_fix(x) for x in df_order['ShippingState']]
        df_order['ShippingState'] = [x.upper() for x in df_order['ShippingState']]
        df_order['ShippingState'] = [self.state_fix(x) for x in df_order['ShippingState']]
        df_order['ShippingState'] = [x.upper() for x in df_order['ShippingState']]
        #df_order['item_desc'] = [self.get_desc_fromID(x) for x in df_order['ItemId']]


        df_order.drop(['BillingState','BillingCity'],axis=1, inplace = True)


        #df_order['OrderDateTime']  =  pd.to_datetime(df_order['OrderDateTime'], format="%m/%d%/%Y")
        df_order['OrderDateTime']  =  pd.to_datetime(df_order['OrderDateTime'])

        df_order.to_csv('../data/clean_order.csv')
        # plot_missing(df_order, name = 'missing-order' )
        return(df_order)

    def loaddata(self):
        if self.reload == True:
            self.data = self.loadcleanorder()
        else:
            self.data = pd.read_csv('../data/clean_order.csv')
        self.dataloaded = True
    def plot(df):
       df1 = df[['Subtotal','SiteDisplayName']].groupby('SiteDisplayName').sum().round(2)
       objects = df1.index.values
       y_pos = np.arange(len(objects))
       performance = df1.Subtotal.values

       plt.bar(y_pos, performance, align='center', alpha=0.5)
       plt.xticks(y_pos, objects,rotation='vertical')
       plt.ylabel('$')
       plt.title('Types of Products')
       plt.gcf().subplots_adjust(bottom=0.3)

       plt.show()
    def blendlist(self):
        list = []
        for b in self.spice_blends():
            z = self.data[self.data['ItemId']==b].head(1).LineItemName.values[0]
            list.append((b,z))
        return(list)


if __name__ =='__main__':
    orders = SOrders()
    #print(dfO.data)
