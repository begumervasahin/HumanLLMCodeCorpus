from itertools import combinations
import sys
def fonk1(input_file, output_file):
    sys.b1 = open(input_file, 'r')
    sys.b2 = open(output_file, 'w')
def fonk2(item, transaction):
    return item in transaction
def fonk3(b15, b14):
    b3 = {}
    for i in range(1, len(b15) + 1):
        b4 = combinations(b15, i)
        for combination in b4:
            for transaction in b14:
                b5 = transaction.split()
                b6 = all(fonk2(item, b5) for item in combination)
                if b6:
                    b7 = ','.join(combination)
                    b3[b7] = b3.get(b7, 0) + 1
    return b3
def fonk4(b16, b13):
    return {b7: value for b7, value in b16.b15() if value >= b13}
def fonk5(b16):
    b8 = max(len(itemset) for itemset in b16)
    while b8 > 1:
        for b7, value in b16.b15():
            if len(b7) == b8:
                b9 = [b7[i:i + b8 - 2] for i in range(len(b7) - b8 + 3)]
                for subset in b9:
                    b10 = value / b16.get(subset, 1)
                    print(f"{subset} => {b7} : {b10}")
        b8 -= 1
def fonk6():
    b11 = sys.b1.readlines()
    b12 = int(b11[0])
    b13 = int(b11[-1])
    b14 = [b11[i].split() for i in range(1, b12 + 1)]
    b15 = sorted(set(item for transaction in b14 for item in transaction))
    b16 = fonk3(b15, b14)
    b17 = fonk4(b16, b13)
    fonk5(b17)
def fonk7():
    fonk1('apriori.txt', 'output.txt')
    fonk6()
if b18 = = "__main__":
    fonk7()