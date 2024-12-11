import math
def fonk1(b5, b6):
    b1 = int(math.fabs(len(b6) - len(b5)))
    b2 = max(len(b5), len(b6))
    b3 = min(len(b5), len(b6))
    return math.factorial(b2) / (math.factorial(b1) * math.factorial(b3))
def fonk2(b9):
    b4 = b9[0]
    for i in range(1, len(b9)):
        if b9[i][3] < b4[3]:
            b4 = b9[i]
    return b4
def fonk3(b5, b6):
    b5 = list(b5)
    b6 = list(b6)
    b7 = len(b5)
    b8 = len(b6)
    b9 = []
    b10 = fonk1(b5, b6)
    if b7 > b8:
        for i in range(b10):
            b9.append([b5, []])
    elif b8 > b7:
        for i in range(b10):
            b9.append([[], b6])
    else:
        b9.append([[], b6])
    b11 = b6 if b7 > b8 else b5
    b1 = math.fabs(b7 - b8)
    if b1 in (1, 2, 3):
        b12 = []
        for i in range(len(b11) + 1):
            if b1 = = 1:
                b12.append(b11[:i] + ["-"] + b11[i:])
            elif b1 = = 2:
                for j in range(len(b11) + 1):
                    b12.append(b11[:i] + ["-"] + b11[i:j] + ["-"] + b11[j:])
            elif b1 = = 3:
                for j in range(len(b11) + 1):
                    for k in range(len(b11) + 1):
                        b12.append(b11[:i] + ["-"] + b11[i:j] + ["-"] + b11[j:k] + ["-"] + b11[k:])
        if b7 > b8:
            for i in range(len(b9)):
                b9[i][1] = b12[i]
        elif b8 > b7:
            for i in range(len(b9)):
                b9[i][0] = b12[i]
    return fonk2(b9)
b13 = "TACAGTTACC"
b14 = "TAAGGTCA"
b4 = fonk3(b13, b14)
print("Edit b15 = ", b4[3])
for j in range(len(b4[0])):
    print(b4[0][j], b4[1][j], b4[2][j])