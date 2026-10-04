
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b7):
    b1 = pd.read_csv(b7, header=None)
    b2 = []
    for i in range(0, len(b1)):
        b2.append([str(b1.values[i, j]) for j in range(0, b1.shape[1])])
    return b2
def fonk2(b2, a1, a2, a3, a4):
    b3 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
    return list(b3)
def fonk3(b3):
    for item in b3:
        b4 = item[0]
        b5 = [x for x in b4]
        print(f"Rule: {b5[0]} -> {b5[1]}")
        print(f"Support: {item[1]}")
        print(f"Confidence: {item[2][0][2]}")
        print(f"Lift: {item[2][0][3]}")
        print("=====================================")
if b6 = = "__main__":
    b7 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b7)
    a1 = 0.003
    a2 = 0.2
    a3 = 3
    a4 = 2
    b3 = fonk2(b2, a1, a2, a3, a4)
    fonk3(b3)