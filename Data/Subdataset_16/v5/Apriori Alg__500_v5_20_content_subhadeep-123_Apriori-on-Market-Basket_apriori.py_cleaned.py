
import pandas as pd
from apyori import apriori
def fonk1(b9):
    b1 = pd.read_csv(b9, header=None)
    b2 = [
        [str(b1.values[i, j]) for j in range(b1.shape[1])]
        for i in range(len(b1))
    ]
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
        print(f"Rule: {b8[:-1]} -> {b8[-1]}")
        print(f"Support: {rule.support}")
        for ordered_stat in rule.ordered_statistics:
            print(f"Confidence: {ordered_stat.confidence}")
            print(f"Lift: {ordered_stat.lift}")
        print("")
def fonk4():
    b9 = 'Market_Basket_Optimisation.csv'
    b4 = 0.003
    b5 = 0.2
    b6 = 3
    b7 = 2
    b2 = fonk1(b9)
    b3 = fonk2(b2, b4, b5, b6, b7)
    fonk3(b3)
if b10 = = "__main__":
    fonk4()