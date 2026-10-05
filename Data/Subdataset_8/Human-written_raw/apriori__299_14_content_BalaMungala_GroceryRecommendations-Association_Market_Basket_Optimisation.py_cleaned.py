14. Repository: BalaMungala/GroceryRecommendations-Association
   File: Market_Basket_Optimisation.py
   URL: https:
   Code Content:
import pandas as pd
dataset=pd.read_csv("F:
transactions=[]
for i in range(0,len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
from apyori import apriori
rules=apriori(transactions,min_support=0.003,min_confidence=0.2,min_length=2,min_lift=3)
results=list(rules)
import matplotlib.pyplot as plt
plt.itemFrequency(results)
   README Content:
Recommending the Products to place in racks for improving the business of Grocery using Collaborative Filtering Algorithm - Apriori in python
