import itertools
import pandas as pd
def fonk1(b6, b7):
    b1 = sum(1 for line in open(b6))
    b2 = int((b7 / 100) * b1)
    b3 = pd.read_csv(b6, sep=' ', header=None, nrows=b2).values
    return b3
def fonk2(b3):
    b4 = {}
    for record in b3:
        for i in range(1, len(record) + 1):
            for combo in itertools.combinations(record, i):
                if combo in b4:
                    b4[combo] += 1
                else:
                    b4[combo] = 1
    return b4
def fonk3(b4, b8):
    return {k: v for k, v in b4.items() if v >= b8}
def fonk4(b4, b9, b10):
    for k in range(2, b10 + 1):
        for combo in [k for k in b4 if len(k) == k]:
            for subset in itertools.combinations(combo, k - 1):
                b5 = b4[combo] / b4[subset]
                if b5 >= b9:
                    print(f"Rule: {subset} -> {set(combo) - set(subset)}, Confidence: {b5:.2f}")
def fonk5():
    b6 = "CarSales.txt"
    b7 = int(input("How many % of b2 you want to read? "))
    b8 = int(input("What is the minimum support? "))
    b9 = float(input("What is the % of the minimum b5? ")) / 100
    b3 = fonk1(b6, b7)
    b4 = fonk2(b3)
    b4 = fonk3(b4, b8)
    print("Frequent itemsets:", b4)
    b10 = max(len(k) for k in b4)
    fonk4(b4, b9, b10)
if b11 = = "__main__":
    fonk5()