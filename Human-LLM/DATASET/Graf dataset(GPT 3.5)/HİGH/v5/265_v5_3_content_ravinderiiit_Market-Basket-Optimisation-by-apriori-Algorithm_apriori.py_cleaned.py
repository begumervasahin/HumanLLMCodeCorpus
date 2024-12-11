
import pandas as pd
from apyori import apriori
def fonk1(b8):
    b1 = pd.read_csv(b8, header=None)
    b2 = []
    for i in range(len(b1)):
        b2.append([str(b1.values[i, j]) for j in range(len(b1.columns))])
    return b2
def fonk2(b2, b4, b5, b6, b7):
    b3 = apriori(b2,
                    b4 = b4,
                    b5 = b5,
                    b6 = b6,
                    b7 = b7)
    return list(b3)
def fonk3():
    b8 = 'Market_Basket_Optimisation.csv'
    b4 = 0.003
    b5 = 0.2
    b6 = 3
    b7 = 2
    b2 = fonk1(b8)
    b3 = fonk2(b2, b4, b5, b6, b7)
    for rule in b3:
        print("Association Rule:", rule.items)
        print("Support:", rule.support)
        print("Confidence:", rule.ordered_statistics[0].confidence)
        print("Lift:", rule.ordered_statistics[0].lift)
        print("===================================")
if b9 = = "__main__":
    fonk3()