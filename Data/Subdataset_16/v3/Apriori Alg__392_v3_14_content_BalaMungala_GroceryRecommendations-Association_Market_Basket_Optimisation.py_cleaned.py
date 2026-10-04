
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
def fonk1(b18):
    b1 = pd.read_csv(b18, header=None)
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
        print(f"Rule: {b9}")
        print(f"Support: {b10:.4f}")
        print(f"Confidence: {b11:.4f}")
        print(f"Lift: {b12:.4f}")
        print("-" * 20)
def fonk4(b4):
    b9 = []
    b13 = []
    for rule in b4:
        for item in rule.b9:
            b9.append(item)
            b13.append(rule.b10)
    plt.figure(b14 = (10, 6))
    plt.bar(b9, b13, b15 = 'blue')
    plt.xlabel('Items')
    plt.ylabel('Support')
    plt.title('Item Frequencies')
    plt.xticks(b16 = 90)
    plt.show()
if b17 = = "__main__":
    b18 = 'F:
    b2 = fonk1(b18)
    b5 = 0.003
    b6 = 0.2
    b7 = 3
    b8 = 2
    b4 = fonk2(b2, b5, b6, b7, b8)
    fonk3(b4)
    fonk4(b4)