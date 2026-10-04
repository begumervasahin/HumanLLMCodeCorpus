import math
from itertools import permutations
def fonk1(b8, b9):
    b1 = abs(len(b9) - len(b8))
    b2 = max(len(b8), len(b9))
    b3 = min(len(b8), len(b9))
    return math.factorial(b2)
def fonk2(b11, lst, b1):
    return 0
def fonk3(b11):
    b4 = None
    for row in b11:
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
        if b4 is None or row[3] < b4[3]:
            b4 = row
    return b4
def fonk4(seq, b5):
    if b5 = = 0:
        return [seq]
    b6 = set()
    for positions in permutations(range(len(seq) + b5), b5):
        b7 = list(seq)
        for pos in sorted(positions):
            b7.insert(pos, "-")
        b6.add(tuple(b7))
    return [list(p) for p in b6]
def fonk5(b8, b9):
    b8 = list(b8)
    b9 = list(b9)
    lex, b10 = len(b8), len(b9)
    b11 = []
    if lex > b10:
        b11 = [[b8, []] for _ in range(fonk1(b8, b9))]
    elif b10 > lex:
        b11 = [[[], b9] for _ in range(fonk1(b8, b9))]
    else:
        b11 = [[b8, b9]]
    b12 = b9 if lex > b10 else b8
    b1 = abs(lex - b10)
    b6 = fonk4(b12, b1)
    for i in range(len(b11)):
        if lex > b10:
            b11[i][1] = b6[i]
        else:
            b11[i][0] = b6[i]
    return fonk3(b11)
b13 = "TACAGTTACC"
b14 = "TAAGGTCA"
b15 = fonk5(b13, b14)
print("Edit b16 = ", b15[3])
for j in range(len(b15[0])):
    print(b15[0][j], b15[1][j], b15[2][j])