import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b8):
    return pd.read_csv(b8, b1 = None)
def fonk2(dataset, b2 = 5):
    print(f"First {b2} rows of the dataset:")
    print(dataset.head(b2))
def fonk3(dataset, b2 = 7501):
    b3 = [[str(dataset.values[i, j]) for j in range(dataset.shape[1])] for i in range(b2)]
    return b3
def fonk4(b3, b4, a1, b5, a2):
    return list(apriori(b3, b4 = b4, a1=a1,
                         b5 = b5, a2=a2))
def fonk5(association_results):
    print("\nNumber of association rules:", len(association_results))
    if association_results:
        print("\nDetails of the first association rule:")
        print(association_results[0])
    print("\nAll association rules:")
    for item in association_results:
        b6 = item[0]
        b7 = [str(x) for x in b6]
        print(f"Rule: {b7[0]} -> {b7[1]}")
        print(f"Support: {item[1]}")
        print(f"Confidence: {item[2][0][2]}")
        print(f"Lift: {item[2][0][3]}")
        print("=====================================")
def fonk6():
    b8 = 'D:\Shreyas Kulkarni\Documents\PycharmProjects\MarketAnalysis_Apriori_Basic\b9.csv'
    b9 = fonk1(b8)
    fonk2(b9)
    b3 = fonk3(b9)
    b4 = 0.0045
    a1 = 0.2
    b5 = 3
    a2 = 2
    b10 = fonk4(b3, b4, a1, b5, a2)
    fonk5(b10)
if b11 = = "__main__":
    fonk6()