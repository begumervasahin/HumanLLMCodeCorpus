import math
def fonk1(b5, b6):
    b1 = abs(len(b6) - len(b5))
    b2 = max(len(b5), len(b6))
    b3 = min(len(b5), len(b6))
    return math.factorial(b2) / (math.factorial(b1) * math.factorial(b3))
def fonk2(b10, lst, b1):
    return 0
def fonk3(b10):
    for row in b10:
        a1 = 0
        row.append([])
        for i in range(len(row[0])):
            if row[0][i] == row[1][i]:
                a1 += 0
                row[2].append(0)
            elif row[0][i] == "-" or row[1][i] == "-":
                a1 += 2
                row[2].append(2)
            else:
                a1 += 1
                row[2].append(1)
        row.append(a1)
        try:
            if row[3] < b4[3]:
                b4 = row
        except UnboundLocalError:
            b4 = row
    return b4
def fonk4(b5, b6):
    b5 = list(b5)
    b6 = list(b6)
    b7 = len(b5)
    b8 = len(b6)
    b9 = max(b7, b8)
    b10 = []
    b11 = fonk1(b5, b6)
    if b7 > b8:
        for _ in range(b11):
            b10.append([b5, []])
    elif b8 > b7:
        for _ in range(b11):
            b10.append([[], b6])
    else:
        b10.append([[], b6])
    b12 = b6 if b7 > b8 else b5
    b1 = abs(b7 - b8)
    if b1 = = 1:
        b13 = [b12[:i] + ["-"] + b12[i:] for i in range(len(b12) + 1)]
        for i in range(len(b10)):
            if b7 > b8:
                b10[i][1] = b13[i]
            else:
                b10[i][0] = b13[i]
    elif b1 = = 2:
        b14 = [b12[:i] + ["-"] + b12[i:] for i in range(len(b12) + 1)]
        b15 = [i[:j] + ["-"] + i[j:] for i in b14 for j in range(len(b12) + 1) if i[:j] + ["-"] + i[j:] not in b14]
        for i in range(len(b10)):
            if b7 > b8:
                b10[i][1] = b15[i]
            else:
                b10[i][0] = b15[i]
    elif b1 = = 3:
        b14 = [b12[:i] + ["-"] + b12[i:] for i in range(len(b12) + 1)]
        b15 = [i[:j] + ["-"] + i[j:] for i in b14 for j in range(len(b12) + 1) if i[:j] + ["-"] + i[j:] not in b14]
        b16 = [i[:j] + ["-"] + i[j:] for i in b15 for j in range(len(b12) + 1) if i[:j] + ["-"] + i[j:] not in b15]
        for i in range(len(b10)):
            if b7 > b8:
                b10[i][1] = b16[i]
            else:
                b10[i][0] = b16[i]
    return fonk3(b10)
b17 = "TACAGTTACC"
b18 = "TAAGGTCA"
b19 = fonk4(b17, b18)
print("Edit b20 = ", b19[3])
for j in range(len(b19[0])):
    print(b19[0][j], b19[1][j], b19[2][j])