def fonk1(b15, b16):
    b1 = len(b16) + 1
    b2 = len(b15) + 1
    b3 = fonk2(b1, b2, 0)
    b4 = fonk2(b1, b2, "A")
    fonk3(b4, b1, b2)
    b10, b11, b5 = fonk4(b3, b4, b15, b16, b1, b2)
    fonk6(b3, "b3.txt")
    fonk6(b4, "b4.txt")
    fonk7(b4, b15, b16, b10, b11, "alignment.txt")
    return b3[b10][b11]
def fonk2(b1, b2, value):
    return [[value for _ in range(b2)] for _ in range(b1)]
def fonk3(b4, b1, b2):
    for i in range(b2):
        b4[0][i] = "F"
    for j in range(1, b1):
        b4[j][0] = "F"
def fonk4(b3, b4, b15, b16, b1, b2):
    b10, b11, b5 = 0, 0, 0
    for b13 in range(1, b1):
        for x in range(1, b2):
            b6 = b3[b13 - 1][x]
            b7 = b3[b13][x - 1]
            b8 = b3[b13 - 1][x - 1] + 1 if b15[x - 1] == b16[b13 - 1] else -1
            b9 = max(b6, b7, b8)
            b3[b13][x] = b9
            if b9 > b5:
                b5 = b9
                b10 = b13
                b11 = x
            b4[b13][x] = fonk5(b9, b7, b8)
    return b10, b11, b5
def fonk5(b9, b7, b8):
    if b9 = = b7:
        return "L"
    elif b9 = = b8:
        return "D"
    else:
        return "T"
def fonk6(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\t".join(map(str, row)) + "\n")
def fonk7(b4, b15, b16, row, col, filename):
    b12 = ""
    x, b13 = col, row
    while b4[b13][x] != "F":
        if b4[b13][x] == "T":
            b13 -= 1
        elif b4[b13][x] == "L":
            x -= 1
        elif b4[b13][x] == "D":
            b12 = b15[x - 1] + b12
            x -= 1
            b13 -= 1
    with open(filename, 'w') as file:
        for i in range(0, len(b12), 50):
            file.write(b12[i:i + 50] + "\n")
if b14 = = "__main__":
    b15 = "AGCGTCTA"
    b16 = "TGCATCTCG"
    b17 = fonk1(b15, b16)
    print(b15)
    print(b16)
    print(f"LCS Score: {b17}")