3. Repository: ravinderiiit/Market-Basket-Optimisation-by-apriori-Algorithm
   File: apriori.py
   URL: https:
   Code Content:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
b2 = []
for i in range(0, 7501):
    b2.append([str(b1.values[i,j]) for j in range(0, 20)])
from apyori import apriori
b3 = apriori(b2, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
b4 = list(b3)
   README Content:
In the b1 their is b1 of a mall transaction given . There are record of 7500 transaction which purchased by customer. The owner of mall want to known which are element are associate with each other. which is done by Apriori Algorithm.
