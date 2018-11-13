# Spice Sales
This project will analyze sales orders created for a retailer with several specialty spice stores. This store offers hundreds of spices, seasonings, and other specialty food products at over 20 locations nationwide and online through their website. This will involve looking at 6 years worth of Sales Order data, list of products, and a database of recipies.   The model will use several superviesed and unsupervised Machine Learning algorithms.   I also found a list of about 20,000 recipes and used a web scraper to get 7,000 more recipes.

## Product Analysis

This spice retailer sells a number of products but the main areas are direct herbs and spices and spice blends.  Spice blends are custom blend of spices that can be used 

![image info](images/Products.png)



## New Blend Analysis

### Spices

'achiote', 'acid', 'adobo', 'aji', 'ajowan', 'aleppo', 'allspice',
       'amarillo', 'ancho', 'anise', 'annatto', 'applewood', 'arbol',
       'asabi', 'asafetida', 'basil', 'bay', 'bean', 'berries', 'bhut',
       'bourbon', 'brokenbag', 'bulb', 'cacao', 'california', 'candied',
       'caraway', 'cardamom', 'cascabel', 'cassia', 'cayenne', 'celery',
       'ceylon', 'ceylontrue', 'charnushka', 'chervil', 'chia', 'chile',
       'chiles', 'chinese', 'chipotle', 'chives', 'chocolate', 'cilantro',
       'cinnamon', 'citric', 'cloves', 'coarse', 'cocoa', 'coriander',
       'coupe', 'crack', 'crushed', 'crystallized', 'cubeb', 'cumin',
       'curry', "d'espelette", 'dehydrated:', 'dill', 'dried', 'dutch',
       'epazote', 'essential', 'european', 'fennel', 'fenugreek',
       'frankincense', 'freezedried', 'french', 'galangal', 'garlic',
       'ghost', 'ginger', 'grains', 'granulated', 'greek', 'green',
       'grenada', 'guajillo', 'gum', 'gumbo', 'habanero', 'habanerobag',
       'hibiscus', 'horseradish', 'hot', 'hungarian', 'indonesian',
       'inner', 'island', 'jalapeno', 'japones', 'jolokia', 'juniper',
       'lampong', 'lavender', 'leaves', 'lemon', 'lemongrass', 'lime',
       'long', 'lovage', 'mace', 'mahlab', 'makrut', 'malabar',
       'marjoram', 'mecos', 'mesquite', 'mexican', 'minced', 'morita',
       'moritas', 'moroccan', 'mulato', 'mustard', 'myrrh', 'mysore',
       'negro', 'nibs', 'nutmeg', 'nutmegs', 'onion', 'onyx', 'orange',
       'oregano', 'organically', 'orgs', 'oriental', 'osemary',
       'pakistan', 'paprika', 'paradise', 'parsley', 'pasilla', 'paste',
       'peel', 'pepper', 'peppercorns', 'peppermint', 'pequin', 'petals',
       'piment', 'pink', 'pods', 'pollen', 'poppy', 'powder', 'powdered',
       'premium', 'pure', 'raw', 'red', 'regular', 'retired', 'reunion',
       'roasted', 'root', 'rose', 'rosebuds', 'rosemary', 'rubbed',
       'saffron', 'sage', 'saigon', 'sarawak', 'sauce', 'savory',
       'scallions', 'scorpion', 'seeds', 'serrano', 'sesame', 'shallots',
       'smoked', 'smokedbag', 'sourced', 'spanish', 'spearmint', 'star',
       'sticks', 'sumac', 'summer', 'sweet', 'szechwan', 'tahitian',
       'tarragon', 'tasmanian', 'tears', 'tellicherry', 'tellicherry:',
       'thai', 'threads', 'thyme', 'tipico', 'toasted', 'trinidad',
       'true', 'turmeric', 'urfa', 'vanilla', 'verbena', 'wasabi', 'weed',
       'white', 'whole', 'wood', 'yellow'
       
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

