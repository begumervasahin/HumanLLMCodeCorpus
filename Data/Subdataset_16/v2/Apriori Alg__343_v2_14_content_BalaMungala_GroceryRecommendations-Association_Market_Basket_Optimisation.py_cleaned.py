
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
def fonk1(b17):
    b1 = pd.read_csv(b17, header=None)
    b2 = []
    for i in range(len(b1)):
        b2.append([str(b1.values[i, j]) for j in range(20)])
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
        b9 = rule.b9
        b10 = rule.ordered_statistics[0].b10
        b11 = rule.ordered_statistics[0].b11
        print(f"Rule: {b8}")
        print(f"Support: {b9:.4f}")
        print(f"Confidence: {b10:.4f}")
        print(f"Lift: {b11:.4f}")
        print("-" * 20)
def fonk4(b3):
    b8 = []
    b12 = []
    for rule in b3:
        for item in rule.b8:
            b8.append(item)
            b12.append(rule.b9)
    plt.figure(b13 = (10, 6))
    plt.bar(b8, b12, b14 = 'blue')
    plt.xlabel('Items')
    plt.ylabel('Support')
    plt.title('Item Frequencies')
    plt.xticks(b15 = 90)
    plt.show()
if b16 = = "__main__":
    b17 = 'F:
    b2 = fonk1(b17)
    b4 = 0.003
    b5 = 0.2
    b6 = 3
    b7 = 2
    b3 = fonk2(b2, b4, b5, b6, b7)
    fonk3(b3)
    fonk4(b3)