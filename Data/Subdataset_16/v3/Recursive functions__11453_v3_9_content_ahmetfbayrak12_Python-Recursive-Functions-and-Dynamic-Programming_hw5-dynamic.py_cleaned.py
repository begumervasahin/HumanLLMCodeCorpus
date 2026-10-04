import math
def fonk1(b8, b9):
    b1 = abs(len(b9) - len(b8))
    b2 = max(len(b8), len(b9))
    b3 = min(len(b8), len(b9))
    return math.factorial(b2)
def fonk2(lst, b1):
    if b1 = = 0:
        return [lst]
    b4 = []
    for i in range(len(lst) + 1):
        b5 = lst[:i] + ["-"] + lst[i:]
        b4 += fonk2(b5, b1 - 1)
    return b4
def fonk3(b12):
    b6 = None
    for row in b12:
        a1 = 0
        row.append([])
        for b7, b in zip(row[0], row[1]):
            if b7 = = b:
                row[2].append(0)
            elif b7 = = "-" or b == "-":
                row[2].append(2)
                a1 += 2
            else:
                row[2].append(1)
                a1 += 1
        row.append(a1)
        if b6 is None or a1 < b6[3]:
            b6 = row
    return b6
def fonk4(b8, b9):
    b8 = list(b8)
    b9 = list(b9)
    lex, b10 = len(b8), len(b9)
    b11 = max(lex, b10)
    b12 = []
    b13 = fonk1(b8, b9)
    b14 = b9 if lex > b10 else b8
    b1 = abs(lex - b10)
    b15 = fonk2(b14, b1)
    if lex > b10:
        for _ in range(b13):
            b12.append([b8, []])
        for i in range(len(b12)):
            b12[i][1] = b15[i]
    elif b10 > lex:
        for _ in range(b13):
            b12.append([[], b9])
        for i in range(len(b12)):
            b12[i][0] = b15[i]
    else:
        b12.append([b8, b9])
    return fonk3(b12)
b16 = "TACAGTTACC"
b17 = "TAAGGTCA"
b18 = fonk4(b16, b17)
print("Edit b19 = ", b18[3])
for j in range(len(b18[0])):
    print(b18[0][j], b18[1][j], b18[2][j])