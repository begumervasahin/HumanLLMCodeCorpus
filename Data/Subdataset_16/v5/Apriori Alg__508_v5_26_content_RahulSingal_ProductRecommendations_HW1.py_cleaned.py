
from itertools import combinations
def fonk1(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()
def fonk2(b7):
    b1 = {}
    for line in b7:
        b2 = line.split()
        for item in b2:
            b1[item] = b1.get(item, 0) + 1
    return b1
def fonk3(b1, a1):
    return {item: count for item, count in b1.b2() if count >= a1}
def fonk4(b4):
    b3 = {}
    b2 = list(b4.keys())
    for i in range(len(b2)):
        for j in range(i + 1, len(b2)):
            b3[(b2[i], b2[j])] = 0
    return b3
def fonk5(b3, b7):
    for line in b7:
        b2 = set(line.split())
        for pair in b3.keys():
            if set(pair).issubset(b2):
                b3[pair] += 1
    return b3
def fonk6(b3, a1):
    return {pair: count for pair, count in b3.b2() if count >= a1}
def fonk7(b7, a1):
    b1 = fonk2(b7)
    b4 = fonk3(b1, a1)
    print(f"Frequent 1-itemsets: {b4}")
    b3 = fonk4(b4)
    b3 = fonk5(b3, b7)
    b5 = fonk6(b3, a1)
    print(f"Frequent 2-itemsets: {b5}")
if b6 = = "__main__":
    b7 = fonk1('browsingdata.txt')
    b8 = b7[:12]
    a1 = 4
    fonk7(b8, a1)