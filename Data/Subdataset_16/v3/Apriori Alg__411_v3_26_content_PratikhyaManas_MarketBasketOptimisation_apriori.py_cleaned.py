
import pandas as pd
from apyori import apriori
def fonk1(b14):
    b1 = pd.read_csv(b14, header=None)
    b2 = []
    for i in range(len(b1)):
        b3 = [str(b1.values[i, j]) for j in range(b1.shape[1]) if pd.notna(b1.values[i, j])]
        b2.append(b3)
    return b2
def fonk2(b2, b5, b6, b7, b8):
    b4 = apriori(
        b2,
        b5 = b5,
        b6 = b6,
        b7 = b7,
        b8 = b8
    )
    return list(b4)
def fonk3(b4):
    for rule in b4:
        b9 = [item for item in rule.b9]
        b10 = rule.b10
        b11 = rule.ordered_statistics[0].b11
        b12 = rule.ordered_statistics[0].b12
        print(f"Rule: {b9[0]} -> {b9[1]}")
        print(f"Support: {b10:.4f}")
        print(f"Confidence: {b11:.4f}")
        print(f"Lift: {b12:.4f}")
        print("=====================================")
if b13 = = "__main__":
    b14 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b14)
    b5 = 0.003
    b6 = 0.2
    b7 = 3
    b8 = 2
    b4 = fonk2(b2, b5, b6, b7, b8)
    fonk3(b4)