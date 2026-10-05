import csv
import math
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = {}
def fonk1(b17):
    try:
        with open(b17, "r") as file:
            b8 = csv.b8(file)
            a1 = 0
            for row in b8:
                b1.append(row)
                a1 += 1
            print("CREATED LIST ITEMS WITH DUPLICATES: \n", a1, len(b1), b1)
            return b1, a1
    except FileNotFoundError:
        print(f"File {b17} not found.")
        return None, 0
def fonk2(a1):
    a2 = 0
    a3 = 0
    a2 = math.exp(-0.4 * a1 - 0.2) + 0.2
    a3 = a2 * a1 / 100
    return a2, a3
def fonk3(b1):
    for i in range(len(b1)):
        b2.extend(b1[i])
    print("ONLY ONE LIST with duplicates: \n", len(b2), b2)
    return b2
def fonk4(seq, b9 = None):
    if b9 is None:
        def fonk5(x): return x
    b10 = {}
    for item in seq:
        b11 = fonk5(item)
        if b11 in b10:
            continue
        b10[b11] = 1
        b3.append(item)
    print("DUPLICATES REMOVED LIST :\n", len(b3), b3)
    return b3
def fonk6(b3):
    b7 = dict(zip(b3, range(1, len(b3) + 1)))
    print('b12 = ', b7)
    for key in sorted(b7.keys()):
        print("%s: %s" % (key, b7[key]))
    return b7
def fonk7(b1, b7):
    for i in range(len(b1)):
        b13 = []
        for j in range(len(b1[i])):
            print(b1[i][j])
            print(b7[b1[i][j]])
            b13.append(b7[b1[i][j]])
        b4.append(b13)
    print("MAPPER LIST:\n", b4)
    return b4
def fonk8(b4, b3):
    for i in range(len(b4)):
        b14 = [0 for k in range(len(b3))]
        for j in range(len(b4[i])):
            for k in range(len(b3)):
                if b4[i][j] == k + 1:
                    b14.pop(b4[i][j] - 1)
                    b14.insert(b4[i][j] - 1, 1)
    b5.append(b14)
    print("b5:\n", b5)
    return b5
def fonk9(item, dict_list):
    b15 = 'Null'
    for itemset in dict_list:
        if item in itemset:
            b15 = itemset[0]
            break
    return b15
if b16 = = "__main__":
    b17 = "groceries_small.csv"
    b1, a1 = fonk1(b17)
    a2, a3 = fonk2(a1)
    b2 = fonk3(b1)
    b3 = fonk4(b2)
    b7 = fonk6(b3)
    b4 = fonk7(b1, b7)
    b5 = fonk8(b4, b3)