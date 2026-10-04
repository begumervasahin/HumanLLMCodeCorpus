import math
def fonk1(b5, b6):
    b1 = abs(len(b6) - len(b5))
    b2 = max(len(b5), len(b6))
    b3 = min(len(b5), len(b6))
    return math.factorial(b2)
def fonk2(b10):
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
def fonk3(b5, b6):
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
        b10.append([b5, b6])
    b12 = b6 if b7 > b8 else b5
    b1 = abs(b7 - b8)
    b13 = []
    def fonk4(lst, b1):
        if b1 = = 0:
            return [lst]
        b13 = []
        for i in range(len(lst) + 1):
            b14 = lst[:i] + ["-"] + lst[i:]
            b13 += fonk4(b14, b1 - 1)
        return b13
    b15 = fonk4(b12, b1)
    if b7 > b8:
        for i in range(len(b10)):
            b10[i][1] = b15[i]
    else:
        for i in range(len(b10)):
            b10[i][0] = b15[i]
    return fonk2(b10)
b16 = "TACAGTTACC"
b17 = "TAAGGTCA"
b18 = fonk3(b16, b17)
print("Edit b19 = ", b18[3])
for j in range(len(b18[0])):
    print(b18[0][j], b18[1][j], b18[2][j])