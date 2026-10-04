def fonk1(seq1, seq2):
    a1 = 5
    a2 = -4
    a3 = -6
    b1 = len(seq2) + 1
    b2 = len(seq1) + 1
    b3 = fonk2(b1, b2, 0)
    b4 = fonk2(b1, b2, "A")
    for b9 in range(b2):
        b3[0][b9] = a3 * b9
        b4[0][b9] = "L"
    for row in range(1, b1):
        b3[row][0] = a3 * row
        b4[row][0] = "T"
    b4[0][0] = 'F'
    for row in range(1, b1):
        for b9 in range(1, b2):
            b5 = b3[row-1][b9] + a3
            b6 = b3[row][b9-1] + a3
            b7 = b3[row-1][b9-1] + (a1 if seq1[b9-1] == seq2[row-1] else a2)
            b8 = max(b5, b6, b7)
            b3[row][b9] = b8
            if b8 = = b6:
                b4[row][b9] = "L"
            elif b8 = = b7:
                b4[row][b9] = "D"
            else:
                b4[row][b9] = "T"
    fonk4(b4, seq1, seq2, "alignment.txt")
    return b3[b1-1][b2-1]
def fonk2(b1, b2, initialValue):
    return [[initialValue for _ in range(b2)] for _ in range(b1)]
def fonk3(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\t".join(map(str, row)) + "\n")
def fonk4(b4, seq1, seq2, filename):
    with open(filename, 'w') as file:
        row, b9 = len(b4) - 1, len(b4[0]) - 1
        b11, b10 = "", ""
        while b4[row][b9] != "F":
            if b4[row][b9] == "T":
                b11 = "-" + b11
                b10 = seq2[row-1] + b10
                row -= 1
            elif b4[row][b9] == "L":
                b11 = seq1[b9-1] + b11
                b10 = "-" + b10
                b9 -= 1
            elif b4[row][b9] == "D":
                b11 = seq1[b9-1] + b11
                b10 = seq2[row-1] + b10
                row -= 1
                b9 -= 1
        for i in range(0, len(b11), 50):
            file.write(b11[i:i+50] + "\n")
            file.write(b10[i:i+50] + "\n")
            file.write("\n")
b12 = "AGCGTCTA"
b13 = "TGCATCTCG"
b14 = fonk1(b12, b13)
print(b12)
print(b13)
print("Global alignment score: " + str(b14))