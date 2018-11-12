import savory_items
import savory_recipes
import savory_blends
import pandas as pd

def remove_product_string(y):
    y = y.strip()
    y = y.replace('(', '')
    y = y.replace(')', '')
    y = y.replace('Discontinued Size -', '')
    y = y.replace('-8floz Plastic', '')
    y = y.replace('-16oz Bag', '')
    y = y.replace('Refill', '')
    y = y.replace('-1oz Bag', '')
    y = y.replace('-1/2 Cup', '')
    y = y.replace('-1/2', '')
    y = y.replace('1 Cup', '')
    y = y.replace('2 Cup', '')
    y = y.replace('3 Cup', '')
    y = y.replace('-8floz', '')
    y = y.replace('-8', '')
    y = y.replace('Medium', '')
    y = y.replace('Small', '')
    y = y.replace('Jar', '')
    y = y.replace(' oz ', '')
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
    y = y.replace(', Extra Fine', '')
    y = y.replace('Discontinued -', '')
    y = y.replace(', Coarse', '')
    y = y.replace(', Cracked', '')
    y = y.replace(', Extra Coarse', '')
    y = y.replace('-16', '')
    y = y.replace('-0','')
    y = y.replace('.5', '')
    y = y.replace('-1', '')
    y = y.replace(' oz', '')
    y = y.replace('/8oz', '')
    y = y.replace("(Spice 'n Easy)", '')
    y = y.replace('Mediterranean', '')
    y = y.replace('Madagascar', '')
    y = y.replace('gr in small glass jar', '')
    y = y.replace('DISCONTINUED', '')
    y = y.replace(',', ' ')
    y = y.replace('Jamaican', '')
    y = y.replace('(Organically Sourced)', '')
    y = y.replace('Turkish', '')
    y = y.replace('New Mexican', '')
    y = y.replace('Mild Red', '')
    y = y.replace('/4', '')
    y = y.replace('3', '')
    y = y.replace('6', '')
    y = y.replace('Disontinued Size', '')
    y = y.replace('Dip & Spread', '')
    y = y.replace('(20g)', '')
    y = y.replace('(50g)', '')
    y = y.replace('&', '')
    y = y.replace('1/', '')
    y = y.replace('9', '')
    y = y.replace('Korean', '')
    y = y.replace('/8', '')
    y = y.replace('0', '')
    y = y.replace('gr in a', '')
    y = y.replace('glass jar', '')
    y = y.replace('', '')
    y = y.replace('8oz', '')
    y = y.replace("''", '')
    y = y.replace('""', '')
    y = y.replace('[', '')
    y = y.replace(']', '')
    y = y.replace('4oz', '')
    y = y.replace('-', '')
    y = y.replace('-', '')
    y = y.replace('-', '')



    y = y.replace('-', '') #leave at bottom

    y = y.strip()
    return(y.lower())

def inglist(spices,ingredients):
    totalspices = []

    ing_split = ingredients.split()
    for elements in ing_split:
        elements = remove_product_string(elements)
        #print(elements)
        if elements in spices and elements not in totalspices:
            totalspices.append(elements)
    return totalspices
if __name__ == '__main__':

    items = savory_items.SItems()
    recipes = savory_recipes.SRecipes()
    blends = savory_blends.SBlends()
    dfmodel = col_names =  ['title', 'ingredients', 'url']
    dfmodel1 = recipes.data[['title', 'ingredients', 'url']]
    dfmodel2 = blends.data[['LineItemName', 'Ingredients']]
    dfmodel2.rename(index=str, columns={"LineItemName": "title", "Ingredients": "ingredients"}, inplace=True)
    dfmodel2['url'] = 'savoryblend'
    result = pd.merge(dfmodel1, dfmodel2, on=['title','ingredients','url'], how='outer')
    result['spicelist'] = [inglist(items.spices,rec) for rec in result.ingredients]
    result.to_csv('../data/IngSpiceList.csv')
