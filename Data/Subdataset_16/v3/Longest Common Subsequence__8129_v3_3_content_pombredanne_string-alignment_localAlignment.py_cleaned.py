def fonk1(s1, s2):
    a1 = 5
    a2 = -4
    a3 = -6
    b1 = len(s2) + 1
    b2 = len(s1) + 1
    b3 = fonk2(b1, b2, 0)
    b4 = fonk2(b1, b2, "A")
    fonk3(b3, b4, b1, b2)
    a4, a5, b5 = fonk4(b3, b4, s1, s2, a1, a2, a3, b1, b2)
    fonk6(b3, "b3.txt")
    fonk6(b4, "b4.txt")
    fonk7(b4, s1, s2, a5, b5, "alignment.txt")
    return b3[a5][b5]
def fonk2(numRows, numCols, value):
    return [[value] * numCols for _ in range(numRows)]
def fonk3(b3, b4, numRows, numCols):
    for i in range(numCols):
        b3[0][i] = 0
        b4[0][i] = "F"
    for j in range(1, numRows):
        b3[j][0] = 0
        b4[j][0] = "F"
def fonk4(b3, b4, s1, s2, match, mismatch, gap, numRows, numCols):
    a4 = 0
    a5 = 0
    b5 = 0
    for b10 in range(1, numRows):
        for x in range(1, numCols):
            b6 = b3[b10-1][x] + gap
            b7 = b3[b10][x-1] + gap
            b8 = b3[b10-1][x-1] + (match if s1[x-1] == s2[b10-1] else mismatch)
            b9 = max(b6, b7, b8, 0)
            if b9 > a4:
                a4 = b9
                a5 = b10
                b5 = x
            b3[b10][x] = b9
            b4[b10][x] = fonk5(b9, b6, b7, b8)
    return a4, a5, b5
def fonk5(b9, b6, b7, b8):
    if b9 = = 0:
        return "F"
    elif b9 = = b7:
        return "L"
    elif b9 = = b8:
        return "D"
    else:
        return "T"
def fonk6(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\b15".join(map(str, row)) + "\n")
def fonk7(b4, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x, b10 = col, row
        b12, b11 = "", ""
        while b4[b10][x] != "F":
            if b4[b10][x] == "T":
                b12 = "-" + b12
                b11 = s2[b10-1] + b11
                b10 -= 1
            elif b4[b10][x] == "L":
                b12 = s1[x-1] + b12
                b11 = "-" + b11
                x -= 1
            elif b4[b10][x] == "D":
                b12 = s1[x-1] + b12
                b11 = s2[b10-1] + b11
                x -= 1
                b10 -= 1
        for i in range(0, len(b12), 50):
            file.write(b12[i:i+50] + "\n")
            file.write(b11[i:i+50] + "\n")
            file.write("\n")
if b13 = = "__main__":
    b14 = "AAGGTATGAATC"
    b15 = "CAGTTGCAA"
    b16 = fonk1(b14, b15)
    print(b14)
    print(b15)
    print(f"Local alignment score: {b16}")