import sys
import pandas as pd
def fonk1(l1, l2):
    return list(set(l1) & set(l2))
def fonk2(l, m):
    return all(elem in m for elem in l)
def fonk3(l1, l2):
    return list(set(l1) - set(l2))
def fonk4(b9, b11, b7, b19):
    if len(b9) == 1:
        b19.append(b9[0])
    for i in range(len(b9)):
        b7.append(b9[i])
        b1 = []
        for j in range(i + 1, len(b9)):
            b2 = list(set(b9[i][0] + b9[j][0]))
            b3 = fonk1(b9[i][1], b9[j][1])
            if len(b3) >= b11:
                b1.append((b2, b3, len(b2)))
        if b1:
            fonk4(b1, b11, b7, b19)
        else:
            if len(b9) != 1:
                b19.append(b9[i])
def fonk5(b10, b11, b8, b21):
    if len(b10) == 1:
        b21.append(b10[0])
    for i in range(len(b10)):
        b8.append(b10[i])
        b4 = []
        for j in range(i + 1, len(b10)):
            b2 = list(set(b10[i][0] + b10[j][0]))
            b5 = fonk3(b10[j][2], b10[i][2])
            b6 = b10[i][1] - len(b5)
            if b6 >= b11:
                b4.append((b2, b6, b5, len(b2)))
        if b4:
            fonk5(b4, b11, b8, b21)
        else:
            if len(b10) != 1:
                b21.append(b10[i])
def fonk6():
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = int(input('Enter b11: '))
    b12 = pd.read_csv('./db.csv', header=None)
    b13 = ["TID"] + [f"i{col}" for col in range(1, len(b12.b14))]
    b12.b14 = b13
    b15 = b12["TID"].count()
    b12.drop(b14 = ["TID"], inplace=True)
    b13.remove("TID")
    b16 = list(range(1, b15 + 1))
    for colName in b13:
        b17 = [index + 1 for index in range(b15) if b12[colName][index] == 1]
        b18 = fonk3(b16, b17)
        if len(b17) >= b11:
            b9.append((colName, b17, 1))
            b10.append((colName, len(b17), b18, 1))
    print("\nECLAT Algorithm")
    b19 = []
    fonk4(b9, b11, b7, b19)
    b19 = sorted(b19, key=lambda x: x[2], reverse=True)
    print("Frequent Itemsets || Transaction IDs where present")
    for a, b, c in b19:
        print(''.join(a), "=>", b)
    b20 = []
    for f in b19:
        if all(not fonk2(f[0], m[0]) for m in b20):
            b20.append(f)
    print("\nMaximal Frequent Sets || Transaction IDs where present")
    for a, b, c in b20:
        print(''.join(a), "=>", b)
    print("\nDECLAT Algorithm")
    b21 = []
    fonk5(b10, b11, b8, b21)
    b21 = sorted(b21, key=lambda x: x[3], reverse=True)
    print("Infrequent Itemsets || Support of Itemsets")
    for a, b, c, d in b21:
        print(''.join(a), "=>", b)
    b20 = []
    for f in b21:
        if all(not fonk2(f[0], m[0]) for m in b20):
            b20.append(f)
    print("\nMaximal Infrequent Sets || Transaction IDs where present")
    for a, b, c, d in b20:
        print(''.join(a), "=>", b)
if b22 = = '__main__':
    fonk6()