# Spice Sales
This project  analyzed the sales orders created for a retailer with several specialty spice stores. This store offers hundreds of spices, seasonings, and other specialty food products at over 20 locations nationwide and online through their website. This will involve looking at 6 years worth of Sales Order data, list of products, and a database of recipies.   The model will used Non-negative matrix factorization (NMF) for its model although PCA and others were considered.   

## Product Analysis

This spice retailer sells a number of products but the main areas are direct herbs and spices and spice blends.  Spice blends are custom blend of spices that can be used 

![image info](images/Products.png)

The two main pieces of data used for this project from above was the list if Herbs and Spices and the list of Blends.  From the companies website you could get a list of ingredients for each spice blend.   From this list of Spices and the ingredients of the blends a list of words we wanted to analize was created.   

Using the list of recipies like an example below, and the blends, and ingredients can be used to find blends that match to recipies, and potentially blends yet to be created.  

Steamed Black Cod with Soy-Chile Sauce
https://www.bonappetit.com/recipe/steamed-black-cod-with-soy-chile-sauce
[\'1 head of garlic, 3 cloves sliced, remaining head halved crosswise\', \'6 scallions, trimmed, 2 cut into 2" pieces, 4 thinly sliced\', \'1 5" piece peeled fresh ginger, cut into matchstick-size pieces\', \'1/2 lemon\', \'4 4-ounce black cod fillets, skin on\', \'1 tablespoon vegetable oil\', \'Kosher salt\', \'2 tablespoons reduced-sodium soy sauce\', \'2 green Thai chiles or 1 serrano chile, thinly sliced\', \'1 tablespoon chopped fresh cilantro\']


## Recipe Analysis
First I looked for order in the data by using PCA with two pricipal components.  
![image info](images/PCA.png)
In the diagram above one recipe in the top part contained ['dried', 'green', 'celery', 'lemon', 'pepper'] one in the below shape contained ['fennel', 'bulb', 'anise', 'leaves', 'onion'].  Although this might have worked for this analysis, a spice with -.2 and -.4 in not very intuative to understand.   
### Spices

'achiote', 'acid', 'adobo', 'aji', 'aleppo', 'allspice',
       'amarillo', 'ancho', 'anise', 'annatto', 'applewood', 'arbol',
       'asafetida', 'basil', 'bay', 'bean', 'berries', 'bourbon', 'bulb',
       'cacao', 'candied', 'caraway', 'cardamom', 'cascabel', 'cassia',
       'cayenne', 'celery', 'ceylon', 'charnushka', 'chervil', 'chia',
       'chile', 'chiles', 'chinese', 'chipotle', 'chives', 'chocolate',
       'cilantro', 'cinnamon', 'citric', 'cloves', 'coarse', 'cocoa',
       'coriander', 'coupe', 'crack', 'crystallized', 'cumin', 'curry',
       'dill', 'dried', 'dutch', 'epazote', 'espelette', 'european',
       'fennel', 'fenugreek', 'freezedried', 'galangal', 'garlic',
       'ghost', 'ginger', 'grains', 'granulated', 'greek', 'green',
       'guajillo', 'gum', 'gumbo', 'habanero', 'hibiscus', 'horseradish',
       'inner', 'jalapeno', 'japones', 'juniper', 'lampong', 'lavender',
       'leaves', 'lemon', 'lemongrass', 'lime', 'long', 'lovage', 'mace',
       'makrut', 'malabar', 'marjoram', 'mesquite', 'minced', 'morita',
       'moritas', 'moroccan', 'mulato', 'mustard', 'mysore', 
       'nibs', 'nutmeg', 'nutmegs', 'onion', 'onyx', 'orange', 'oregano',
       'oriental', 'paprika', 'parsley', 'pasilla', 'paste', 'peel',
       'pepper', 'peppercorns', 'peppermint', 'pequin', 'petals',
       'piment', 'pods', 'pollen', 'poppy', 'powder', 'powdered',
       'premium', 'raw', 'roasted', 'root', 'rose', 'rosebuds',
       'rosemary', 'rubbed', 'saffron', 'sage', 'saigon', 'sarawak',
       'sauce', 'savory', 'scallions', 'seeds', 'serrano', 'sesame',
       'shallots', 'smoked', 'spanish', 'spearmint', 'star', 'sumac',
       'summer', 'sweet', 'szechwan', 'tarragon', 'thai', 'threads',
       'thyme', 'toasted', 'true', 'turmeric', 'urfa', 'vanilla',
       'verbena', 'wasabi', 'weed', 'white', 'wood'

So based in the previous recipe you would only get the following ingredients for this recipe.

['garlic', 'cloves', 'scallions', 'ginger', 'green', 'thai', 'chiles', 'serrano', 'chile']

### Using NMF
When using NMF it inforces positve values and this can be helpful to understand which ingredients will be used.  NMF decomposes the recipe list into two matrices, W and H, when multiplied together they approximately recreate our original V matrix. Below is visulizaton of the H matrix with the latent topics (k) across the bottom and the ingredients on the y axis.  The W matrix would be similar but it would have the recipies relating to the latent topics.   

![image info](images/WH.png)

I went with 50 topics, there was not much of a bend in the elbow plot seen below.   

![image info](images/Reconstruction60.png)

Using these two matricies allows the data to be compaired and recomendation made for the company and customers.   

![image info](images/FeaturestoSpices.png)

Break down every recipe and blend into a list of latent topics allows us to compare a recipe to all the blends.  For example the recipe based on the W matrix above 'Mackerel with Crushed Potatoes and Oregano' would have a latent feature matrix of 
0.03, 0.05, 0.  , 0.07, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,.....
and one of the blends 'Mt. Olympus Greek Style Seasoning'
0.  , 0.03, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.04,

This is a pretty close match base on the ingredients, so this blend could be recomended to anyone using this recipe.

![image info](images/Mackerel.png)

But what if there isn't a good match 'Asian Noodles with Barbecued Duck Confit' there isn't a good blend match, although it does reccomend 'Nacho Cheese Dip' 
![image info](images/EpicuriousDuck.png)

Interesting no blends contain scallions.  But 700+ recipies call for this ingredient, this could be a potential new spice blend since there isn't a good match.    
![image info](images/Freeze.png)

These are recipes like

Korean Marinated Beef 
Steamed Chicken with Black Mushrooms and Bok C...
Cold Noodle Salad with Ponzu Sauce 
Quick Sesame Chicken With Broccoli 
Kimchi-Style Sautéed Cabbage 

That contain ingredients like the following.
'sesame', 'scallions', 'white', 'green', 'lime', 'powder', 'cayenne', 'garlic', 'ginger'

Maybe there might be a 'Ramen Booster' spice blend that is needed.  



![image info](images/Features.png)

