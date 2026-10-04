
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
def fonk1(file_path):
    return pd.read_csv(file_path, b1 = None)
def fonk2(b5):
    b2 = []
    for i in range(len(b5)):
        b3 = [str(b5.values[i, j]) for j in range(b5.shape[1]) if str(b5.values[i, j]) != 'nan']
        b2.append(b3)
    return b2
def fonk3(b2, b4, min_confidence, min_lift, min_length):
    return apriori(b2, b4 = b4, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
def fonk4(b7):
    for result in b7:
        print(result)
def fonk5():
    b5 = fonk1('Market_Basket_Optimisation.csv')
    b2 = fonk2(b5)
    b6 = fonk3(b2, b4=0.003, min_confidence=0.2, min_lift=3, min_length=2)
    b7 = list(b6)
    fonk4(b7)
if b8 = = "__main__":
    fonk5()