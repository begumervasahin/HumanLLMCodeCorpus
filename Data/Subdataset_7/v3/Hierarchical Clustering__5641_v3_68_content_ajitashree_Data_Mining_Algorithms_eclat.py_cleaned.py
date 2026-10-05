import pandas as pd
def fonk1(list1, list2):
    return list(set(list1) & set(list2))
def fonk2(list1, list2):
    return all(item in list2 for item in list1)
def fonk3(b10, b12, b8, b14):
    if len(b10) == 1:
        b14.append(b10[0])
    for i in range(len(b10)):
        b8.append(b10[i])
        b1 = []
        for j in range(i + 1, len(b10)):
            b2 = list(set(b10[i][0] + b10[j][0]))
            b3 = fonk1(b10[i][1], b10[j][1])
            if len(b3) >= b12:
                b1.append((b2, b3, len(b2)))
        if b1:
            fonk3(b1, b12, b8, b14)
        else:
            if len(b10) != 1:
                b14.append(b10[i])
def fonk4(list1, list2):
    return [item for item in list1 if item not in list2]
def fonk5(b11, b12, b9, b15):
    if len(b11) == 1:
        b15.append(b11[0])
    for i in range(len(b11)):
        b9.append(b11[i])
        b4 = []
        for j in range(i + 1, len(b11)):
            b2 = list(set(b11[i][0] + b11[j][0]))
            b5 = fonk4(b11[j][2], b11[i][2])
            b6 = b11[i][1] - len(b5)
            if b6 >= b12:
                b4.append((b2, b6, b5, len(b2)))
        if b4:
            fonk5(b4, b12, b9, b15)
        else:
            if len(b11) != 1:
                b15.append(b11[i])
if b7 = = '__main__':
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    print()
    b12 = int(input('Enter minsupport: '))
    b13 = ["TID"]
    b14 = []
    b15 = []
    b16 = []
    b17 = pd.read_csv('./db.csv', header=None)
    for i in range(1, len(b17.b18)):
        b13.append(("i" + str(i)))
    b17.b18 = b13
    b19 = b17["TID"].count()
    del b17["TID"]
    b13.remove("TID")
    print()
    print("Itemsets", b13)
    b20 = [i + 1 for i in range(b19)]
    for col_name in b13:
        b21 = [index + 1 for index in range(b19) if b17[col_name][index] == 1]
        b16 = fonk4(b20, b21)
        if len(b21) >= b12:
            b10.append((col_name, b21, 1))
            b11.append((col_name, len(b21), b16, 1))
    print()
    print("     ECLAT Algorithm   ")
    fonk3(b10, b12, b8, b14)
    print("Freq Itemsets || Trans id's where pr")
    b14 = sorted(b14, key=lambda x: x[2], reverse=True)
    for a, b, c in b14:
        print(''.join(a), "=>", b)
    b22 = []
    for f in b14:
        b23 = True
        for m in b22:
            if fonk2(f[0], m[0]):
                b23 = False
        if b23:
            b22.append(f)
    print()
    print("MAximal Frequent set || Trans id's where pr")
    for a, b, c in b22:
        print(''.join(a), "=>", b)
    print()
    print("     DEclat  Algorithm   ")
    fonk5(b11, b12, b9, b15)
    b22 = []
    print("Freq Itemsets || support of b13")
    b15 = sorted(b15, key=lambda x: x[3], reverse=True)
    for a, b, c, d in b15:
        print(''.join(a), "=>", b)
    for f in b15:
        b23 = True
        for m in b22:
            if fonk2(f[0], m[0]):
                b23 = False
        if b23:
            b22.append(f)
    print()
    print("MAximal Frequent set || Trans id's where pr")
    for a, b, c, d in b22:
        print(''.join(a), "=>", b)