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
    b10, b11, b5 = 0, 0, 0
    for b12 in range(1, b1):
        for x in range(1, b2):
            b6 = b3[b12-1][x]
            b7 = b3[b12][x-1]
            b8 = b3[b12-1][x-1] + 1 if s1[x-1] == s2[b12-1] else -1
            b9 = max(b6, b7, b8)
            b3[b12][x] = b9
            if b9 > b5:
                b5 = b9
                b10 = b12
                b11 = x
            if b9 = = b7:
                b4[b12][x] = "L"
            elif b9 = = b8:
                b4[b12][x] = "D"
            else:
                b4[b12][x] = "T"
    fonk3(b3, "b3.txt")
    fonk3(b4, "b4.txt")
    fonk4(b4, s1, s2, b10, b11, "alignment.txt")
    return b3[b10][b11]
def fonk2(numRows, numCols, value):
    return [[value for _ in range(numCols)] for _ in range(numRows)]
def fonk3(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\b15".join(map(str, row)) + "\n")
def fonk4(direction, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x, b12 = col, row
        b13 = ""
        while direction[b12][x] != "F":
            if direction[b12][x] == "T":
                b12 -= 1
            elif direction[b12][x] == "L":
                x -= 1
            elif direction[b12][x] == "D":
                b13 = s1[x-1] + b13
                x -= 1
                b12 -= 1
        for i in range(0, len(b13), 50):
            file.write(b13[i:i+50] + "\n")
b14 = "AGCGTCTA"
b15 = "TGCATCTCG"
b16 = fonk1(b14, b15)
print(b14)
print(b15)
print("LCS Score:", b16)