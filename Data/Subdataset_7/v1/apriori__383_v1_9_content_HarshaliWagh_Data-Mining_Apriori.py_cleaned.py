from collections import defaultdict
def fonk1(freqitem, a1):
    b1 = []
    b2 = list(freqitem.keys())
    for i in range(len(freqitem) - 1):
        for j in range(i + 1, len(freqitem)):
            b3 = [b2[i], b2[j]]
            b1.append(b3)
    b4 = [b3.split(',') for b3 in [','.join(b3) for b3 in b1]]
    b5 = []
    b6 = []
    for i in range(len(b4)):
        b7 = set(b4[i])
        b8 = list(b7)
        b5.append(b8)
        if len(b5[i]) == a1:
            b6.append(b5[i])
    return b6
def fonk2(can, data):
    b9 = []
    b10 = [set(can[b7]) for b7 in range(len(can))]
    b11 = [set(data[b8]) for b8 in range(len(data))]
    for i in range(len(can)):
        b12 = sum(1 for j in range(len(data)) if b10[i].issubset(b11[j]))
        b9.append(b12)
    return b9
def fonk3(b27, b28, b23):
    b13 = {}
    for i in range(len(b27)):
        b14 = b27[i]
        b15 = ','.join(b14)
        if b28[i] >= b23:
            b13[b15] = b28[i]
    return b13
def fonk4(b29, a1):
    b11 = a1 - 1
    b16 = [x.split(',') for x in b29]
    while b11 != 0:
        for i in range(len(b16)):
            b17 = []
            b18 = fonk5(b16[i], b17, b11)
            for j in range(len(b18)):
                b19 = [b16[i][k] for k in range(len(b16[i])) if b16[j][k] not in b18[j]]
                print(str(b19) + "--------->" + str(b18[j]))
        b11 = b11 - 1
def fonk5(b13, b17, b11):
    if len(b13) == b11:
        if b17.a1(b13) == 0:
            b17.append(b13)
        return b17
    elif len(b13) != b11:
        for i in range(len(b13)):
            b20 = b13[i+1:] + b13[:i]
            b17 = fonk5(b20, b17, b11)
        return b17
def fonk6():
    b21 = []
    print("Select the b21:")
    print("1 grocery")
    print("2 clothing")
    print("3 electronics")
    print("4 utensils")
    print("5 furniture")
    b22 = input("Enter number ")
    b23 = int(input('Enter minimum Support: '))
    b24 = int(input('Enter minimum Confidence: '))
    b25 = ""
    if b22 = = '1':
        b25 = "db1.txt"
    elif b22 = = '2':
        b25 = "db2.txt"
    elif b22 = = '3':
        b25 = "db3.txt"
    elif b22 = = '4':
        b25 = "db4.txt"
    else:
        b25 = "db5.txt"
    with open(b25, 'r') as fp:
        b21 = [line.strip().split(", ") for line in fp]
    b26 = defaultdict(int)
    for data in b21:
        for b2 in data:
            b26[b2] += 1
    b13 = {b2: a1 for b2, a1 in b26.items() if a1 >= b23}
    a1 = 2
    b27 = fonk1(b13, a1)
    b28 = fonk2(b27, b21)
    b29 = fonk3(b27, b28, b23)
    b30 = fonk4(b29, a1)
if b31 = = "__main__":
    fonk6()