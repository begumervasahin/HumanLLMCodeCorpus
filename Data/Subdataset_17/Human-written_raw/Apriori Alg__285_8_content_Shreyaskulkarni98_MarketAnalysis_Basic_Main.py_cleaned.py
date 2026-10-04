8. Repository: Shreyaskulkarni98/MarketAnalysis_Basic
   File: Main.py
   URL: https:
   Code Content:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data = pd.read_csv('D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\store_data.csv', header=None)
store_data.head()
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print(len(association_results))
print(association_results[0])
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
   README Content:
This is a analysis of a supermarket's transactions to predicts associations between items purchased using the apriori algorithm.
Association rule mining is a technique to identify underlying relations between different items. Take an example of a Super Market where customers can buy variety of items. Usually, there is a pattern in what the customers buy. For instance, mothers with babies buy baby products such as milk and diapers. Damsels may buy makeup items whereas bachelors may buy beers and chips etc. In short, transactions involve a pattern. More profit can be generated if the relationship between the items purchased in different transactions can be identified.
For instance, if item A and B are bought together more frequently then several steps can be taken to increase the profit. For example:
A and B can be placed together so that when a customer buys one of the product he doesn't have to go far away to buy the other product.
People who buy one of the products can be targeted through an advertisement campaign to buy the other.
Collective discounts can be offered on these products if the customer buys both of them.
Both A and B can be packaged together.
This analysis was done on 7501 transactions using the apriori algorithm for association rule mining.
