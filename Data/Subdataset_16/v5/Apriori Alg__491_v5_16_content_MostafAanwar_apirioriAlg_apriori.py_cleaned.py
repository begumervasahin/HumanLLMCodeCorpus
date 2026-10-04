import itertools
import pandas as pd
from collections import defaultdict
from itertools import chain, permutations
def fonk1(b14, b11):
    b1 = sum(1 for _ in open(b14))
    b2 = int((b11 / 100) * b1)
    return pd.read_csv(b14, b3 = ' ', header=None, nrows=b2).values
def fonk2(b15):
    b4 = defaultdict(int)
    for transaction in b15:
        for i in range(1, len(transaction) + 1):
            for combination in itertools.b9(transaction, i):
                b4[combination] += 1
    return b4
def fonk3(b4, b12):
    return {item: count for item, count in b4.items() if count >= b12}
def fonk4(b4, b13):
    b5 = max(len(item) for item in b4)
    b6 = [item for item in b4 if len(item) == b5]
    b7 = [b4[item] for item in b6]
    b8 = set(chain.from_iterable(b6))
    b9 = [subset for itemset in b6
                    for i in range(1, len(itemset))
                    for subset in itertools.b9(itemset, i)]
    b10 = list(permutations(b8, b5))
    return b7, b9, b10
def fonk5():
    b11 = int(input("Enter the b11 of records to read: "))
    b12 = int(input("Enter the minimum support: "))
    b13 = int(input("Enter the minimum confidence b11: "))
    b14 = "CarSales.txt"
    b15 = fonk1(b14, b11)
    b4 = fonk2(b15)
    b16 = fonk3(b4, b12)
    print("Filtered Itemsets:", b16)
    b7, b9, b10 = fonk4(b16, b13)
    print("Confidence Values:", b7)
    print("Combinations:", b9)
    print("Permutations:", b10)
if b17 = = "__main__":
    fonk5()