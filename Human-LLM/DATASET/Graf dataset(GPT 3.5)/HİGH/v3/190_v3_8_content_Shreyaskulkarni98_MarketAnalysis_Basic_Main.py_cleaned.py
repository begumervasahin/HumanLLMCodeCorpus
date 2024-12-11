import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b10):
    return pd.read_csv(b10, b1 = None)
def fonk2(dataframe):
    b2 = []
    for i in range(len(dataframe)):
        b3 = [str(dataframe.values[i, j]) for j in range(len(dataframe.columns))]
        b2.append(b3)
    return b2
def fonk3(b2, b4 = 0.0045, min_confidence=0.2, b6=3, min_length=2):
    b5 = apriori(b2, b4=b4, min_confidence=min_confidence,
                                b6 = b6, min_length=min_length)
    return list(b5)
def fonk4(b12):
    print("\nNumber of association rules:", len(b12))
    if len(b12) > 0:
        print("\nDetails of the first association rule:")
        b7 = b12[0]
        print("Rule:", b7[0])
        print("Support:", b7[1])
        print("Confidence:", b7[2][0][2])
        print("Lift:", b7[2][0][3])
    print("\nAll association rules:")
    for item in b12:
        b8 = item[0]
        b9 = [x for x in b8]
        print("Rule: " + b9[0] + " -> " + b9[1])
        print("Support: " + str(item[1]))
        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
def fonk5():
    b10 = 'D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\b11.csv'
    b11 = fonk1(b10)
    print("First few rows of the dataset:")
    print(b11.head())
    b2 = fonk2(b11)
    b12 = fonk3(b2)
    fonk4(b12)
if b13 = = "__main__":
    fonk5()