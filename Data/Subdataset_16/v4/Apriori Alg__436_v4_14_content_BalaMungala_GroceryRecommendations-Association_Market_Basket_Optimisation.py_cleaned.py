
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
def fonk1(b5):
    return pd.read_csv(b5, b1 = None)
def fonk2(b6):
    b2 = []
    for i in range(len(b6)):
        b3 = [str(b6.values[i, j]) for j in range(b6.shape[1]) if str(b6.values[i, j]) != 'nan']
        b2.append(b3)
    return b2
def fonk3(b2, a1, a2, a3, a4):
    b4 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
    return list(b4)
def fonk4(results):
    for result in results:
        print(result)
def fonk5():
    b5 = "F:
    b6 = fonk1(b5)
    b2 = fonk2(b6)
    a1 = 0.003
    a2 = 0.2
    a3 = 3
    a4 = 2
    b4 = fonk3(b2, a1, a2, a3, a4)
    fonk4(b4)
if b7 = = "__main__":
    fonk5()