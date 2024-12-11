import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = 'D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\b2.csv'
b2 = pd.read_csv(b1, header=None)
print("First few rows of the dataset:")
print(b2.head())
b3 = []
for i in range(len(b2)):
    b4 = [str(b2.values[i, j]) for j in range(len(b2.columns))]
    b3.append(b4)
a1 = 0.0045
a2 = 0.2
a3 = 3
a4 = 2
b5 = apriori(b3, a1=a1, a2=a2,
                            a3 = a3, a4=a4)
b6 = list(b5)
print("\nNumber of association rules:", len(b6))
if len(b6) > 0:
    print("\nDetails of the first association rule:")
    print("Rule:", b6[0][0])
    print("Support:", b6[0][1])
    print("Confidence:", b6[0][2][0][2])
    print("Lift:", b6[0][2][0][3])
print("\nAll association rules:")
for item in b6:
    b7 = item[0]
    b8 = [x for x in b7]
    print("Rule: " + b8[0] + " -> " + b8[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")