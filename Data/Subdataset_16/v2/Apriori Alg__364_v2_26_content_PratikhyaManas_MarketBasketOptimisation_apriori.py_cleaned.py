
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b11):
    b1 = pd.read_csv(b11, header=None)
    b2 = []
    for i in range(len(b1)):
        b2.append([str(b1.values[i, j]) for j in range(b1.shape[1])])
    return b2
def fonk2(b2, b4, b5, b6, b7):
    b3 = apriori(
        b2,
        b4 = b4,
        b5 = b5,
        b6 = b6,
        b7 = b7
    )
    return list(b3)
def fonk3(b3):
    for item in b3:
        b8 = item[0]
        b9 = [x for x in b8]
        print(f"Rule: {b9[0]} -> {b9[1]}")
        print(f"Support: {item[1]:.4f}")
        print(f"Confidence: {item[2][0][2]:.4f}")
        print(f"Lift: {item[2][0][3]:.4f}")
        print("=====================================")
if b10 = = "__main__":
    b11 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b11)
    b4 = 0.003
    b5 = 0.2
    b6 = 3
    b7 = 2
    b3 = fonk2(b2, b4, b5, b6, b7)
    fonk3(b3)