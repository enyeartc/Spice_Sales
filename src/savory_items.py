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
import savory_orders


class SItems(object):
    '''
      SItems will contain a list of
    '''

    def __init__(self, reload=0):

        self.reload = reload
        self.data = self.loaddata()
        self.spices = self.loadspices()


    def loadspices(self):
        orders1 = savory_orders.SOrders()

        # spices = orders.herbs_spices()
        spiced = self.data[self.data['ItemId'].isin(orders1.herbs_spices_id())]
        spices = spiced.item_desc

        # small = items.data.groupby('ItemId').first()
        # small.drop(['LineItemName'],axis=1, inplace = True)
        # result = pd.merge(self.spices, small, on=['ItemId'], how='outer')

        spices = [savory_utils.remove_product_string(y) for y in spices]
        spices = np.unique(spices)
        totalspices = []
        for elements in spices:
            elements_split = elements.split(' ')
            totalspices.extend(elements_split)
        spices = np.unique(totalspices)
        badlist = [ 'de', 'glass', 'gr','ill', 'in', 'jar', 'of', 'or', 's', 'small','', '&', "'n", '(20g)', '(50g)',
                    'Tom', 'True,', '/4', '/8', '0', '1/', '2', '3', '5', '6','8oz', '9', 'a','bag','2g', '5g','sunday', 'dipped', 'mug',
                    'risotto','filã©','4oz','apple', 'barrel', 'beans','bell', 'big', 'black','mild', 'sliced','chips' , 'organic','crumbled',
                    'blade','bleached', 'blue', 'brine', 'broken','natural' ,'strips','cubed','ground','chopped','oil','diced',
                    'brown', 'clearance', 'file', 'fine','flakes', 'flower',  'freeze', 'plastic',
                    'california', 'crushed', 'french','hot', 'hungarian', 'indonesian','island', 'mexican', 'osemary','pink',
                    'pure','red', 'regular', 'retired', 'reunion','yellow' ]
        ix = np.isin(spices, badlist,invert=True)
        spices = spices[ix]
        return(spices)

    def loadcleanitem(self):
        df_item = pd.read_csv('../data/item.csv')
        df_item['item_desc'] = [savory_utils.remove_product_string(x) for x in df_item['LineItemName']]

        df_item.to_csv('../data/clean_item.csv')
        return(df_item)
    def loaddata(self):
        if self.reload == 1:
            return(self.loadcleanitem())
        df_item = pd.read_csv('../data/clean_item.csv')
        return(df_item)


if __name__ =='__main__':
    items = SItems(reload=1)
