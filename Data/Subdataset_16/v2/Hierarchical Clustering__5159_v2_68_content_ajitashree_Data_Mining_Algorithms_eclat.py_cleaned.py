import sys
import pandas as pd
def fonk1(l1, l2):
    return list(set(l1) & set(l2))
def fonk2(subset, superset):
    return all(elem in superset for elem in subset)
def fonk3(l1, l2):
    return list(set(l1) - set(l2))
def fonk4(P, b15, F, b16):
    if len(P) == 1:
        b16.append(P[0])
    for i in range(len(P)):
        F.append(P[i])
        b1 = []
        for j in range(i + 1, len(P)):
            b2 = list(set(P[i][0] + P[j][0]))
            b3 = fonk1(P[i][1], P[j][1])
            if len(b3) >= b15:
                b1.append((b2, b3, len(b2)))
        if b1:
            fonk4(b1, b15, F, b16)
        else:
            if len(P) != 1:
                b16.append(P[i])
def fonk5(b10, b15, IF, b18):
    if len(b10) == 1:
        b18.append(b10[0])
    for i in range(len(b10)):
        IF.append(b10[i])
        b4 = []
        for j in range(i + 1, len(b10)):
            b2 = list(set(b10[i][0] + b10[j][0]))
            b5 = fonk3(b10[j][2], b10[i][2])
            b6 = b10[i][1] - len(b5)
            if b6 >= b15:
                b4.append((b2, b6, b5, len(b2)))
        if b4:
            fonk5(b4, b15, IF, b18)
        else:
            if len(b10) != 1:
                b18.append(b10[i])
def fonk6(file_path):
    b7 = pd.read_csv(file_path, header=None)
    b8 = ["TID"] + [f"i{col}" for col in range(1, len(b7.b9))]
    b7.b9 = b8
    return b7, b8
def fonk7(b7, b8, b15):
    P, b10 = [], []
    b11 = b7["TID"].count()
    b12 = list(range(1, b11 + 1))
    b7.drop(b9 = ["TID"], inplace=True)
    b8.remove("TID")
    for col_name in b8:
        b13 = [index + 1 for index in range(b11) if b7[col_name][index] == 1]
        b14 = fonk3(b12, b13)
        if len(b13) >= b15:
            P.append((col_name, b13, 1))
            b10.append((col_name, len(b13), b14, 1))
    return P, b10
def fonk8():
    b15 = int(input('Enter b15: '))
    b7, b8 = fonk6('./db.csv')
    P, b10 = fonk7(b7, b8, b15)
    print("\nECLAT Algorithm")
    F, b16 = [], []
    fonk4(P, b15, F, b16)
    b16 = sorted(b16, key=lambda x: x[2], reverse=True)
    print("Frequent Itemsets || Transaction IDs where present")
    for itemset, transactions, _ in b16:
        print(''.join(itemset), "=>", transactions)
    print("\nMaximal Frequent Sets || Transaction IDs where present")
    b17 = [f for f in b16 if all(not fonk2(f[0], m[0]) for m in b16 if m != f)]
    for itemset, transactions, _ in b17:
        print(''.join(itemset), "=>", transactions)
    print("\nDECLAT Algorithm")
    IF, b18 = [], []
    fonk5(b10, b15, IF, b18)
    b18 = sorted(b18, key=lambda x: x[3], reverse=True)
    print("Infrequent Itemsets || Support of Itemsets")
    for itemset, support, _, _ in b18:
        print(''.join(itemset), "=>", support)
    print("\nMaximal Infrequent Sets || Transaction IDs where present")
    b19 = [f for f in b18 if all(not fonk2(f[0], m[0]) for m in b18 if m != f)]
    for itemset, support, _, _ in b19:
        print(''.join(itemset), "=>", support)
if b20 = = '__main__':
    fonk8()