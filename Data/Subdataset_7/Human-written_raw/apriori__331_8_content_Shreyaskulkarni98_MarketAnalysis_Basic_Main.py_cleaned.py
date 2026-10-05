8. Repository: Shreyaskulkarni98/MarketAnalysis_Basic
   File: Main.py
   URL: https:
   Code Content:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\b1.csv', header=None)
b1.head()
b2 = []
for i in range(0, 7501):
    b2.append([str(b1.values[i,j]) for j in range(0, 20)])
b3 = apriori(b2, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
b4 = list(b3)
print(len(b4))
print(b4[0])
for item in b4:
    b5 = item[0]
    b6 = [x for x in b5]
    print("Rule: " + b6[0] + " -> " + b6[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
   README Content:
This is a analysis of a supermarket's transactions to predicts associations between b6 purchased using the apriori algorithm.
Association rule mining is a technique to identify underlying relations between different b6. Take an example of a Super Market where customers can buy variety of b6. Usually, there is a pattern in what the customers buy. For instance, mothers with babies buy baby products such as milk and diapers. Damsels may buy makeup b6 whereas bachelors may buy beers and chips etc. In short, transactions involve a pattern. More profit can be generated if the relationship between the b6 purchased in different transactions can be identified.
For instance, if item A and B are bought together more frequently then several steps can be taken to increase the profit. For example:
A and B can be placed together so that when a customer buys one of the product he doesn't have to go far away to buy the other product.
People who buy one of the products can be targeted through an advertisement campaign to buy the other.
Collective discounts can be offered on these products if the customer buys both of them.
Both A and B can be packaged together.
This analysis was done on 7501 transactions using the apriori algorithm for association rule mining.
