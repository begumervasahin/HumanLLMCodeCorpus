
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b6):
    b1 = pd.read_csv(b6, header=None)
    b2 = []
    for i in range(0, b1.shape[0]):
        b2.append([str(b1.values[i, j]) for j in range(0, b1.shape[1]) if pd.notna(b1.values[i, j])])
    return b2
def fonk2(b2, a1, a2, a3, a4):
    b3 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
    return list(b3)
def fonk3(b3):
    for rule in b3:
        b4 = [x for x in rule.b4]
        print(f"Rule: {b4}")
        print(f"Support: {rule.support}")
        print(f"Confidence: {rule.ordered_statistics[0].confidence}")
        print(f"Lift: {rule.ordered_statistics[0].lift}")
        print("=====================================")
if b5 = = "__main__":
    b6 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b6)
    a1 = 0.003
    a2 = 0.2
    a3 = 3
    a4 = 2
    b3 = fonk2(b2, a1, a2, a3, a4)
    fonk3(b3)