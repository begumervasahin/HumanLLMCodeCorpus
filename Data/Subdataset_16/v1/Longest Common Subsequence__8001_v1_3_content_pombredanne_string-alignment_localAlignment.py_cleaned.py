def fonk1(s1, s2):
    a1 = 5
    a2 = -4
    a3 = -6
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
    a4 = 0
    a5 = 0
    a6 = 0
    for b11 in range(1, b1):
        for b10 in range(1, b2):
            b5 = b3[b11-1][b10] + a3
            b6 = b3[b11][b10-1] + a3
            if s1[b10-1] == s2[b11-1]:
                b7 = b3[b11-1][b10-1] + a1
            else:
                b7 = b3[b11-1][b10-1] + a2
            b8 = max(b5, b6, b7, 0)
            if b8 > a4:
                a4 = b8
                a5 = b11
                a6 = b10
            b3[b11][b10] = b8
            if b8 = = 0:
                b4[b11][b10] = "F"
            elif b8 = = b6:
                b4[b11][b10] = "L"
            elif b8 = = b7:
                b4[b11][b10] = "D"
            else:
                b4[b11][b10] = "T"
    fonk3(b3, "b3.txt")
    fonk3(b4, "b4.txt")
    fonk4(b4, s1, s2, a5, a6, "alignment.txt")
    return b3[a5][a6]
def fonk2(numRows, numCols, value):
    b9 = []
    for row in range(numRows):
        b9.append([value] * numCols)
    return b9
def fonk3(b9, filename):
    with open(filename, 'w') as file:
        for row in b9:
            file.write("\b17".join(map(str, row)) + "\n")
def fonk4(direction, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        b10 = col
        b11 = row
        b12 = direction[b11][b10]
        b13 = ""
        b14 = ""
        while b12 != "F":
            if direction[b11][b10] == "T":
                b13 = "-" + b13
                b14 = s2[b11-1] + b14
                b11 -= 1
            elif direction[b11][b10] == "L":
                b13 = s1[b10-1] + b13
                b14 = "-" + b14
                b10 -= 1
            elif direction[b11][b10] == "D":
                b13 = s1[b10-1] + b13
                b14 = s2[b11-1] + b14
                b10 -= 1
                b11 -= 1
            b12 = direction[b11][b10]
        for i in range(0, len(b13), 50):
            file.write(b13[i:i+50] + "\n")
            file.write(b14[i:i+50] + "\n")
            file.write("\n")
if b15 = = "__main__":
    b16 = "AAGGTATGAATC"
    b17 = "CAGTTGCAA"
    b18 = fonk1(b16, b17)
    print(b16)
    print(b17)
    print("Local alignment score: " + str(b18))