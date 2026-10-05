14. Repository: BalaMungala/GroceryRecommendations-Association
   File: Market_Basket_Optimisation.py
   URL: https:
   Code Content:
import pandas as pd
b1 = pd.read_csv("F:
b2 = []
for i in range(0,len(b1)):
    b2.append([str(b1.values[i,j]) for j in range(0,20)])
from apyori import apriori
b3 = apriori(b2,min_support=0.003,min_confidence=0.2,min_length=2,min_lift=3)
b4 = list(b3)
import matplotlib.pyplot as plt
plt.itemFrequency(b4)
   README Content:
Recommending the Products to place in racks for improving the business of Grocery using Collaborative Filtering Algorithm - Apriori in python
