
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
def fonk1(b10):
    b1 = pd.read_csv(b10, header=None)
    b2 = []
    for i in range(0, len(b1)):
        b2.append([str(b1.values[i, j]) for j in range(0, 20)])
    return b2
def fonk2(b2, a1, a2, a3, a4):
    b3 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
    return list(b3)
def fonk3(b3):
    for rule in b3:
        b4 = [x for x in rule.b4]
        print(f"Rule: {b4}")
        print(f"Support: {rule.support}")
        print(f"Confidence: {rule.ordered_statistics[0].confidence}")
        print(f"Lift: {rule.ordered_statistics[0].lift}")
        print("-" * 20)
def fonk4(b3):
    b4 = []
    b5 = []
    for rule in b3:
        for item in rule.b4:
            b4.append(item)
            b5.append(rule.support)
    plt.figure(b6 = (10, 6))
    plt.bar(b4, b5, b7 = 'blue')
    plt.xlabel('Items')
    plt.ylabel('Support')
    plt.title('Item Frequencies')
    plt.xticks(b8 = 90)
    plt.show()
if b9 = = "__main__":
    b10 = 'F:
    b2 = fonk1(b10)
    a1 = 0.003
    a2 = 0.2
    a3 = 3
    a4 = 2
    b3 = fonk2(b2, a1, a2, a3, a4)
    fonk3(b3)
    fonk4(b3)