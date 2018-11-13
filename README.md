# Spice Sales
This project  analyzed the sales orders created for a retailer with several specialty spice stores. This store offers hundreds of spices, seasonings, and other specialty food products at over 20 locations nationwide and online through their website. This will involve looking at 6 years worth of Sales Order data, list of products, and a database of recipies.   The model will used NMP for its model although PCA and others were considered.   

## Product Analysis

This spice retailer sells a number of products but the main areas are direct herbs and spices and spice blends.  Spice blends are custom blend of spices that can be used 

![image info](images/Products.png)

The two main pieces of data used for this project from above was the list if Herbs and Spices and the list of Blends.  From the companies website you could get a list of ingredients for each spice blend.   From this list of Spices and the ingredients of the blends a list of words we wanted to analize was created.   

Using the list of recipies 

Steamed Black Cod with Soy-Chile Sauce
https://www.bonappetit.com/recipe/steamed-black-cod-with-soy-chile-sauce
[\'1 head of garlic, 3 cloves sliced, remaining head halved crosswise\', \'6 scallions, trimmed, 2 cut into 2" pieces, 4 thinly sliced\', \'1 5" piece peeled fresh ginger, cut into matchstick-size pieces\', \'1/2 lemon\', \'4 4-ounce black cod fillets, skin on\', \'1 tablespoon vegetable oil\', \'Kosher salt\', \'2 tablespoons reduced-sodium soy sauce\', \'2 green Thai chiles or 1 serrano chile, thinly sliced\', \'1 tablespoon chopped fresh cilantro\']

## New Blend Analysis

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
       'moritas', 'moroccan', 'mulato', 'mustard', 'mysore', 'negro',
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
       
![image info](images/FeaturestoSpices.png)
Break down every recipe and rub into list of Herbs and Spices

Ham Persillade with Mustard Potato Salad and M.     'long', 'parsley', 'garlic', 'celery'

Limnos Lamb Rub                                     'coarse', 'garlic', 'lemon', 'peel', 'onion'


Feature 38 No Blends but 700+ recipies
----- 38
['chile' 'chinese' 'chives' 'dill' 'ginger' 'greek' 'long' 'paste' 'pods' 'scallions']

8      ['sesame', 'scallions', 'white', 'green', 'min...
38                                ['sweet', 'scallions']
90            ['lime', 'powder', 'cayenne', 'scallions']
118                     ['lemon', 'garlic', 'scallions']



![image info](images/Reconstruction60.png)

![image info](images/Features.png)

