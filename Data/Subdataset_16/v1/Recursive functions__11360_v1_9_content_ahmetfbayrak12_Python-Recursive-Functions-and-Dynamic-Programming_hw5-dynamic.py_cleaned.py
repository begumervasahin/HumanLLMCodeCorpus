import math
def fonk1(b5, b6):
    b1 = int(math.fabs(len(b6) - len(b5)))
    b2 = max(len(b5), len(b6))
    b3 = min(len(b5), len(b6))
    return math.factorial(b2)
def fonk2(b10, liste, b1):
    return 0
def fonk3(b10):
    for i in range(len(b10)):
        a1 = 0
        b10[i].append([])
        for j in range(len(b10[i][0])):
            if b10[i][0][j] == b10[i][1][j]:
                a1 += 0
                b10[i][2].append(0)
            elif b10[i][0][j] == "-" or b10[i][1][j] == "-":
                a1 += 2
                b10[i][2].append(2)
            else:
                a1 += 1
                b10[i][2].append(1)
        b10[i].append(a1)
        try:
            if b10[i][3] < b4[3]:
                b4 = b10[i]
        except UnboundLocalError:
            b4 = b10[i]
    return b4
def fonk4(b5, b6):
    b5 = list(b5)
    b6 = list(b6)
    b7 = len(b5)
    b8 = len(b6)
    b9 = max(b7, b8)
    b10 = []
    b11 = fonk1(b5, b6)
    if len(b5) > len(b6):
        for i in range(b11):
            b10.append([b5, []])
    elif b8 > b7:
        for i in range(b11):
            b10.append([[], b6])
    else:
        b10.append([[], b6])
    b12 = b6 if b7 > b8 else b5
    b1 = math.fabs(b7 - b8)
    b13 = []
    if b1 = = 1:
        for i in range(len(b12) + 1):
            b13.append(b12[:i] + ["-"] + b12[i:])
        if b7 > b8:
            for i in range(len(b10)):
                b10[i][1] = b13[i]
        else:
            for i in range(len(b10)):
                b10[i][0] = b13[i]
    elif b1 = = 2:
        for i in range(len(b12) + 1):
            b13.append(b12[:i] + ["-"] + b12[i:])
        b14 = []
        for i in b13:
            for j in range(len(b12) + 1):
                b15 = i[:j] + ["-"] + i[j:]
                if b15 not in b14:
                    b14.append(b15)
        if b7 > b8:
            for i in range(len(b10)):
                b10[i][1] = b14[i]
        else:
            for i in range(len(b10)):
                b10[i][0] = b14[i]
    elif b1 = = 3:
        for i in range(len(b12) + 1):
            b13.append(b12[:i] + ["-"] + b12[i:])
        b14 = []
        for i in b13:
            for j in range(len(b12) + 1):
                b15 = i[:j] + ["-"] + i[j:]
                if b15 not in b14:
                    b14.append(b15)
        b16 = []
        for i in b14:
            for j in range(len(b12) + 1):
                b15 = i[:j] + ["-"] + i[j:]
                if b15 not in b16:
                    b16.append(b15)
        if b7 > b8:
            for i in range(len(b10)):
                b10[i][1] = b16[i]
        else:
            for i in range(len(b10)):
                b10[i][0] = b16[i]
    return fonk3(b10)
b17 = "TACAGTTACC"
b18 = "TAAGGTCA"
b19 = fonk4(b17, b18)
print("Edit b20 = ", b19[3])
for j in range(len(b19[0])):
    print(b19[0][j], b19[1][j], b19[2][j])