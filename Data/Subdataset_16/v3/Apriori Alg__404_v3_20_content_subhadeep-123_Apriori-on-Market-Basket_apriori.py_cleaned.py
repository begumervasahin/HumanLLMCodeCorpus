
import pandas as pd
from apyori import apriori
def fonk1(b14):
    b1 = pd.read_csv(b14, header=None)
    b2 = [
        [str(b1.values[i, j]) for j in range(b1.shape[1]) if pd.notna(b1.values[i, j])]
        for i in range(b1.shape[0])
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
        b8 = list(rule.b8)
        b9 = rule.b9
        b10 = rule.ordered_statistics[0]
        b11 = b10.b11
        b12 = b10.b12
        print(f"Rule: {b8}")
        print(f"Support: {b9:.4f}")
        print(f"Confidence: {b11:.4f}")
        print(f"Lift: {b12:.4f}")
        print("=====================================")
if b13 = = "__main__":
    b14 = 'Market_Basket_Optimisation.csv'
    b2 = fonk1(b14)
    b4 = 0.003
    b5 = 0.2
    b6 = 3
    b7 = 2
    b3 = fonk2(b2, b4, b5, b6, b7)
    fonk3(b3)