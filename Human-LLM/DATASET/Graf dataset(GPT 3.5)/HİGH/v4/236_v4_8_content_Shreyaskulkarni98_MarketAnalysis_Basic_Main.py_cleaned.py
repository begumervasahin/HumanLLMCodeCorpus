import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\b1.csv', header=None)
print("First few rows of the dataset:")
print(b1.head())
b2 = []
for i in range(0, 7501):
    b2.append([str(b1.values[i, j]) for j in range(0, 20)])
b3 = apriori(b2, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
b4 = list(b3)
print("Number of association rules:", len(b4))
if len(b4) > 0:
    print("Details of the first association rule:")
    print(b4[0])
for item in b4:
    b5 = item[0]
    b6 = [x for x in b5]
    print("Rule: " + b6[0] + " -> " + b6[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")