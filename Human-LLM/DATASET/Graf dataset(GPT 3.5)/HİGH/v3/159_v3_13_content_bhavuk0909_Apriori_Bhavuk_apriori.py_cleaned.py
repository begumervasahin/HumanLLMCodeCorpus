
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(b7):
    b1 = pd.read_csv(b7, header=None)
    b2 = []
    for i in range(len(b1)):
        b3 = [str(b1.values[i, j]) for j in range(len(b1.columns))]
        b2.append(b3)
    return b2
def fonk2(b2, b4 = 0.003, min_confidence=0.2, b6=3, min_length=2):
    b5 = apriori(b2, b4=b4, min_confidence=min_confidence,
                    b6 = b6, min_length=min_length)
    return list(b5)
def fonk3(b5):
    for rule in b5:
        print(rule)
def fonk4():
    b7 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b7)
    b5 = fonk2(b2)
    fonk3(b5)
if b8 = = "__main__":
    fonk4()