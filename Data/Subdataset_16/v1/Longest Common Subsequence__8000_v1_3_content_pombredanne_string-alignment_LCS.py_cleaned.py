def fonk1(s1, s2):
    b1 = len(s2) + 1
    b2 = len(s1) + 1
    b3 = fonk2(b1, b2, 0)
    b4 = fonk2(b1, b2, "A")
    for i in range(b2):
        b3[0][i] = 0
        b4[0][i] = "F"
    for j in range(1, b1):
        b3[j][0] = 0
        b4[j][0] = "F"
    a1 = 0
    a2 = 0
    a3 = 0
    for b11 in range(1, b1):
        for x in range(1, b2):
            b5 = b3[b11 - 1][x]
            b6 = b3[b11][x - 1]
            if s1[x - 1] == s2[b11 - 1]:
                b7 = b3[b11 - 1][x - 1] + 1
            else:
                b7 = -1
            b8 = max(b5, b6, b7)
            b3[b11][x] = b8
            if b8 > a3:
                a3 = b8
                a1 = b11
                a2 = x
            if b8 = = b6:
                b4[b11][x] = "L"
            elif b8 = = b7:
                b4[b11][x] = "D"
            else:
                b4[b11][x] = "T"
    fonk3(b3, "b3.txt")
    fonk3(b4, "b4.txt")
    fonk4(b4, s1, s2, a1, a2, "alignment.txt")
    return b3[a1][a2]
def fonk2(numRows, numCols, value):
    b9 = []
    for row in range(numRows):
        b9.append([value] * numCols)
    return b9
def fonk3(b9, filename):
    with open(filename, 'w') as file:
        for row in b9:
            file.write("\b14".join(map(str, row)) + "\n")
def fonk4(b4, s1, s2, row, col, filename):
    b10 = ""
    x, b11 = col, row
    while b4[b11][x] != "F":
        if b4[b11][x] == "T":
            b11 -= 1
        elif b4[b11][x] == "L":
            x -= 1
        elif b4[b11][x] == "D":
            b10 = s1[x - 1] + b10
            x -= 1
            b11 -= 1
    with open(filename, 'w') as file:
        for i in range(0, len(b10), 50):
            file.write(b10[i:i + 50] + "\n")
if b12 = = "__main__":
    b13 = "AGCGTCTA"
    b14 = "TGCATCTCG"
    b15 = fonk1(b13, b14)
    print(b13)
    print(b14)
    print("LCS Score: " + str(b15))