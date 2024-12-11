def fonk1(s1, s2):
    b1 = len(s2) + 1
    b2 = len(s1) + 1
    b3 = fonk2(b1, b2, 0)
    b4 = fonk2(b1, b2, "A")
    for i in range(0, b2):
        b3[0][i] = 0
        b4[0][i] = "F"
    for j in range(1, b1):
        b3[j][0] = 0
        b4[j][0] = "F"
    a1 = 0
    a2 = 0
    a3 = 0
    for b10 in range(1, b1):
        for b9 in range(1, b2):
            b5 = b3[b10 - 1][b9]
            b6 = b3[b10][b9 - 1]
            if s1[b9 - 1] == s2[b10 - 1]:
                b7 = b3[b10 - 1][b9 - 1] + 1
            else:
                b7 = -1
            b8 = max(b5, b6, b7)
            b3[b10][b9] = b8
            if b8 > a3:
                a3 = b8
                a1 = b10
                a2 = b9
            if b8 = = b6:
                b4[b10][b9] = "L"
            elif b8 = = b7:
                b4[b10][b9] = "D"
            else:
                b4[b10][b9] = "T"
    fonk3(b3, "b3.txt")
    fonk3(b4, "b4.txt")
    fonk4(b4, s1, s2, a1, a2, "alignment.txt")
    return b3[a1][a2]
def fonk2(numRows, numCols, value):
    return [[value] * numCols for _ in range(numRows)]
def fonk3(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write('\b14'.join(map(str, row)) + '\n')
def fonk4(direction, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        b9 = col
        b10 = row
        b11 = direction[b10][b9]
        b12 = ""
        while b11 != "F":
            if direction[b10][b9] == "T":
                b10 -= 1
            elif direction[b10][b9] == "L":
                b9 -= 1
            elif direction[b10][b9] == "D":
                b12 = s1[b9 - 1] + b12
                b9 -= 1
                b10 -= 1
            b11 = direction[b10][b9]
        for i in range(0, len(b12), 50):
            file.write(b12[i:i + 50] + "\n")
b13 = "AGCGTCTA"
b14 = "TGCATCTCG"
b15 = fonk1(b13, b14)
print(b13)
print(b14)
print("LCS Score: " + str(b15))