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
        for x in range(1, b2):
            b5 = b3[b11-1][x] + a3
            b6 = b3[b11][x-1] + a3
            if s1[x-1] == s2[b11-1]:
                b7 = b3[b11-1][x-1] + a1
            else:
                b7 = b3[b11-1][x-1] + a2
            b8 = max(b5, b6, b7, 0)
            if b8 > a4:
                a4 = b8
                a5 = b11
                a6 = x
            b3[b11][x] = b8
            if b8 = = 0:
                b4[b11][x] = "F"
            elif b8 = = b6:
                b4[b11][x] = "L"
            elif b8 = = b7:
                b4[b11][x] = "D"
            else:
                b4[b11][x] = "T"
    fonk3(b3, "b3.txt")
    fonk3(b4, "b4.txt")
    fonk4(b4, s1, s2, a5, a6, "alignment.txt")
    return b3[a5][a6]
def fonk2(b1, b2, value):
    return [[value for _ in range(b2)] for _ in range(b1)]
def fonk3(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\b13".join(map(str, row)) + "\n")
def fonk4(b4, s1, s2, row, col, filename):
    b9 = ""
    b10 = ""
    x, b11 = col, row
    while b4[b11][x] != "F":
        if b4[b11][x] == "T":
            b9 = "-" + b9
            b10 = s2[b11-1] + b10
            b11 -= 1
        elif b4[b11][x] == "L":
            b9 = s1[x-1] + b9
            b10 = "-" + b10
            x -= 1
        elif b4[b11][x] == "D":
            b9 = s1[x-1] + b9
            b10 = s2[b11-1] + b10
            x -= 1
            b11 -= 1
    with open(filename, 'w') as file:
        for i in range(0, len(b9), 50):
            file.write(b9[i:i+50] + "\n")
            file.write(b10[i:i+50] + "\n")
            file.write("\n")
b12 = "AAGGTATGAATC"
b13 = "CAGTTGCAA"
b14 = fonk1(b12, b13)
print(b12)
print(b13)
print("Local alignment score: " + str(b14))