import math
def fonk1(b5, b6):
    b1 = int(math.fabs(len(b6) - len(b5)))
    b2 = max(len(b5), len(b6))
    b3 = min(len(b5), len(b6))
    return (math.factorial(b2)) / (math.factorial(b1) * math.factorial(b3))
def fonk2(b9):
    for i in range(len(b9)):
        a1 = 0
        b9[i].append([])
        for j in range(len(b9[i][0])):
            if b9[i][0][j] == b9[i][1][j]:
                a1 += 0
                b9[i][2].append(0)
            elif b9[i][0][j] == "-" or b9[i][1][j] == "-":
                a1 += 2
                b9[i][2].append(2)
            else:
                a1 += 1
                b9[i][2].append(1)
        b9[i].append(a1)
    b4 = b9[0]
    for i in range(1, len(b9)):
        if b9[i][3] < b4[3]:
            b4 = b9[i]
    return b4
def fonk3(b9, b12, b1):
    return 0
def fonk4(b5, b6):
    b5 = list(b5)
    b6 = list(b6)
    b7 = len(b5)
    b8 = len(b6)
    b9 = []
    b10 = fonk1(b5, b6)
    if len(b5) > len(b6):
        for i in range(b10):
            b9.append([])
            b9[i].append(b5)
            b9[i].append([])
    elif b8 > b7:
        for i in range(b10):
            b9.append([])
            b9[i].append([])
            b9[i].append(b6)
    else:
        b9.append([])
        b9[i].append([])
        b9[i].append(b6)
    b11 = list()
    b1 = math.fabs(b7 - b8)
    if b7 > b8:
        b11 = b6
    elif b8 > b7:
        b11 = b5
    if b1 = = 1:
        b12 = []
        for i in range(len(b11) + 1):
            b12.append(b11[:1] + ["-"] + b11[i:1])
        if b7 > b8:
            for i in range(len(b9)):
                b9[i][0] = b12[i]
        elif b8 > b7:
            for i in range(len(b9)):
                b9[i][0] = b12[i]
    elif b1 = = 2:
        b12 = []
        for i in range(len(b11) + 1):
            b12.append(b11[:i] + ["-"] + b11[i:])
        b13 = []
        for i in b12:
            for j in range(len(b11) + 1):
                b14 = i[:j] + ["-"] + i[j:]
                if b14 not in b13:
                    b13.append(b14)
        if b7 > b8:
            for i in range(len(b9)):
                b9[i][1] = b13[i]
        elif b8 > b7:
            for i in range(len(b9)):
                b9[i][0] = b13[i]
    elif b1 = = 3:
        b12 = []
        for i in range(len(b11) + 1):
            b12.append(b11[:i] + "-" + b11[i:])
        b13 = []
        for i in b13:
            for j in range(len(b11) + 1):
                b14 = i[:j] + ["-"] + i[j:]
                if b14 not in b13:
                    b13.append(b14)
        b15 = []
        for i in b13:
            for j in range(len(b11) + 1):
                b14 = i[:j] + ["-"] + i[j:]
                if b14 not in b15:
                    b15.append(b14)
        if b7 > b8:
            for i in range(len(b9)):
                b9[i][1] = b15[i]
        elif b8 > b7:
            for i in range(len(b9)):
                b9[i][0] = b15[i]
    return fonk2(b9)
b16 = "TACAGTTACC"
b17 = "TAAGGTCA"
b18 = fonk4(b16, b17)
print("Edit b19 = " + str(b18[3]))
for j in range(len(b18[0])):
    print(b18[0][j] + " " + b18[1][j] + " " + str(b18[2][j])))