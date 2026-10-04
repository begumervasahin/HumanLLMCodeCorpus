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
    for b9 in range(1, b1):
        for x in range(1, b2):
            b5 = b3[b9-1][x] + a3
            b6 = b3[b9][x-1] + a3
            if s1[x-1] == s2[b9-1]:
                b7 = b3[b9-1][x-1] + a1
            else:
                b7 = b3[b9-1][x-1] + a2
            b8 = max(b5, b6, b7, 0)
            if b8 > a4:
                a4 = b8
                a5 = b9
                a6 = x
            b3[b9][x] = b8
            if b8 = = 0:
                b4[b9][x] = "F"
            elif b8 = = b6:
                b4[b9][x] = "L"
            elif b8 = = b7:
                b4[b9][x] = "D"
            else:
                b4[b9][x] = "T"
    fonk3(b3, "b3.txt")
    fonk3(b4, "b4.txt")
    fonk4(b4, s1, s2, a5, a6, "alignment.txt")
    return b3[a5][a6]
def fonk2(numRows, numCols, value):
    return [[value] * numCols for _ in range(numRows)]
def fonk3(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\b14".join(map(str, row)) + "\n")
def fonk4(direction, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x, b9 = col, row
        b11, b10 = "", ""
        while direction[b9][x] != "F":
            if direction[b9][x] == "T":
                b11 = "-" + b11
                b10 = s2[b9-1] + b10
                b9 -= 1
            elif direction[b9][x] == "L":
                b11 = s1[x-1] + b11
                b10 = "-" + b10
                x -= 1
            elif direction[b9][x] == "D":
                b11 = s1[x-1] + b11
                b10 = s2[b9-1] + b10
                x -= 1
                b9 -= 1
        for i in range(0, len(b11), 50):
            file.write(b11[i:i+50] + "\n")
            file.write(b10[i:i+50] + "\n")
            file.write("\n")
if b12 = = "__main__":
    b13 = "AAGGTATGAATC"
    b14 = "CAGTTGCAA"
    b15 = fonk1(b13, b14)
    print(b13)
    print(b14)
    print(f"Local alignment score: {b15}")