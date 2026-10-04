
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b5):
    b1 = pd.read_csv(b5, header=None)
    b2 = []
    for i in range(b1.shape[0]):
        b3 = [str(b1.values[i, j]) for j in range(b1.shape[1]) if str(b1.values[i, j]) != 'nan']
        b2.append(b3)
    return b2
def fonk2(b2, a1, a2, a3, a4):
    b4 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
    return list(b4)
def fonk3():
    b5 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b5)
    a1 = 0.003
    a2 = 0.2
    a3 = 3
    a4 = 2
    b4 = fonk2(b2, a1, a2, a3, a4)
    for rule in b4:
        print(rule)
if b6 = = "__main__":
    fonk3()