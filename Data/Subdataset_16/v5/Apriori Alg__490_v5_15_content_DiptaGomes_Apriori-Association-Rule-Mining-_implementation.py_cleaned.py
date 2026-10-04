
import numpy as np
import pandas as pd
from apyori import apriori
def fonk1(b6):
    return pd.read_csv(b6, b1 = None)
def fonk2(b7):
    b2 = []
    for i in range(len(b7)):
        b3 = [str(b7.values[i, j]) for j in range(b7.shape[1]) if str(b7.values[i, j]) != 'nan']
        b2.append(b3)
    return b2
def fonk3(b2, a1, a2, a3, a4):
    b4 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
    return list(b4)
def fonk4(b4):
    for rule in b4:
        b5 = [x for x in rule.b5]
        print(f"Rule: {b5[0]} -> {b5[1]}")
        print(f"Support: {rule.support}")
        print(f"Confidence: {rule.ordered_statistics[0].confidence}")
        print(f"Lift: {rule.ordered_statistics[0].lift}")
        print("=====================================")
def fonk5():
    b6 = 'Nursery.csv'
    b7 = fonk1(b6)
    b2 = fonk2(b7)
    a1 = 0.04
    a2 = 0.90
    a3 = 3
    a4 = 2
    b4 = fonk3(b2, a1, a2, a3, a4)
    fonk4(b4)
if b8 = = "__main__":
    fonk5()