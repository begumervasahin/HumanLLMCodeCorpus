import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b8):
    return pd.read_csv(b8, b1 = None)
def fonk2(data):
    b2 = []
    for i in range(len(data)):
        b2.append([str(data.values[i, j]) for j in range(data.shape[1])])
    return b2
def fonk3(transactions, b3, b4, min_lift, b5):
    return list(apriori(transactions, b3 = b3,
                        b4 = b4, min_lift=min_lift,
                        b5 = b5))
def fonk4(rules):
    print(f"Number of association rules: {len(rules)}")
    if rules:
        print(f"First association rule: {rules[0]}")
    for item in rules:
        b6 = item[0]
        b7 = [x for x in b6]
        print(f"Rule: {b7[0]} -> {b7[1]}")
        print(f"Support: {item[1]}")
        print(f"Confidence: {item[2][0][2]}")
        print(f"Lift: {item[2][0][3]}")
        print("=====================================")
def fonk5():
    b8 = 'D:/Shreyas Kulkarni/Documents/PycharmProjects/MarketAnalysis_Apriori_Basic/b9.csv'
    b9 = fonk1(b8)
    print(b9.head())
    b2 = fonk2(b9)
    b10 = fonk3(b2, b3=0.0045, b4=0.2, min_lift=3, b5=2)
    fonk4(b10)
if b11 = = "__main__":
    fonk5()