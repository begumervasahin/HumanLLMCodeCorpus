
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b13):
    b1 = pd.read_csv(b13, header=None)
    b2 = []
    for i in range(b1.shape[0]):
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
    for rule in b3:
        b8 = [item for item in rule.b8]
        b9 = rule.b9
        b10 = rule.ordered_statistics[0].b10
        b11 = rule.ordered_statistics[0].b11
        print(f"Rule: {b8}")
        print(f"Support: {b9:.4f}")
        print(f"Confidence: {b10:.4f}")
        print(f"Lift: {b11:.4f}")
        print("-" * 20)
if b12 = = "__main__":
    b13 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b13)
    b4 = 0.003
    b5 = 0.2
    b6 = 3
    b7 = 2
    b3 = fonk2(b2, b4, b5, b6, b7)
    fonk3(b3)