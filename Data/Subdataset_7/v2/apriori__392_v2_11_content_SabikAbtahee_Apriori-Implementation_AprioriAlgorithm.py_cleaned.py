from itertools import combinations
import sys
def fonk1():
    sys.b1 = open('apriori.txt', 'r')
    sys.b2 = open('output.txt', 'w')
def fonk2(item, transaction):
    return item in transaction
def fonk3(b16, b15):
    b3 = {}
    for i in range(1, len(b16) + 1):
        b4 = combinations(b16, i)
        for combination in b4:
            for transaction in b15:
                b5 = transaction.split()
                b6 = True
                for item in combination:
                    if not fonk2(item, b5):
                        b6 = False
                        break
                if b6:
                    b7 = ','.join(combination)
                    b3[b7] = b3.get(b7, 0) + 1
    return b3
def fonk4(b17, b14):
    b8 = {}
    for b7, value in b17.b16():
        if value >= b14:
            b8[b7] = value
    return b8
def fonk5(b17):
    b9 = max(len(itemset) for itemset in b17)
    while b9 > 1:
        for b7, value in b17.b16():
            if len(b7) == b9:
                b10 = [b7[i:i + b9 - 2] for i in range(len(b7) - b9 + 3)]
                for subset in b10:
                    b11 = value / b17.get(subset, 1)
                    print(f"{subset} => {b7} : {b11}")
        b9 -= 1
def fonk6():
    b12 = sys.b1.readlines()
    b13 = int(b12[0])
    b14 = int(b12[-1])
    b15 = [b12[i].split() for i in range(1, b13 + 1)]
    b16 = sorted(set(item for transaction in b15 for item in transaction))
    b17 = fonk3(b16, b15)
    b8 = fonk4(b17, b14)
    fonk5(b8)
def fonk7():
    fonk1()
    fonk6()
if b18 = = "__main__":
    fonk7()