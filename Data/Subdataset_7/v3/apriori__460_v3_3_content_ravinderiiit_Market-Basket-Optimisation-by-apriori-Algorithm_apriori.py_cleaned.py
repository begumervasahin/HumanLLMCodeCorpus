import pandas as pd
from apyori import apriori
def fonk1(b3):
    b1 = pd.read_csv(b3, header=None)
    b2 = [[str(b1.values[i, j]) for j in range(len(b1.columns))] for i in range(len(b1))]
    return b2
def fonk2():
    b3 = 'Market_Basket_Optimisation.csv'
    a1 = 0.003
    a2 = 0.2
    a3 = 3
    a4 = 2
    b2 = fonk1(b3)
    b4 = apriori(b2,
                    a1 = a1,
                    a2 = a2,
                    a3 = a3,
                    a4 = a4)
    fonk3(b4)
def fonk3(b4):
    for result in b4:
        print("Association Rule:", result.items)
        print("Support:", result.support)
        print("Confidence:", result.ordered_statistics[0].confidence)
        print("Lift:", result.ordered_statistics[0].lift)
        print("===================================")
if b5 = = "__main__":
    fonk2()