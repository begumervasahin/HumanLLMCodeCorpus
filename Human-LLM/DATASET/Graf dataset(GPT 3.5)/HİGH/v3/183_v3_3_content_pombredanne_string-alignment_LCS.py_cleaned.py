def fonk1(s1, s2):
    b1 = len(s2) + 1
    b2 = len(s1) + 1
    b3 = fonk2(b1, b2, 0)
    b4 = fonk2(b1, b2, "A")
    fonk3(b3, b4)
    max_row, b10, b5 = fonk4(b3, b4, s1, s2)
    fonk5(b3, b4)
    fonk6(b4, s1, s2, max_row, b10, "alignment.txt")
    return b5
def fonk2(b1, b2, value):
    return [[value] * b2 for _ in range(b1)]
def fonk3(b3, b4):
    b1, b2 = len(b3), len(b3[0])
    for i in range(b2):
        b3[0][i] = 0
        b4[0][i] = "F"
    for j in range(1, b1):
        b3[j][0] = 0
        b4[j][0] = "F"
def fonk4(b3, b4, s1, s2):
    max_row, b10, b5 = 0, 0, 0
    for b11 in range(1, len(b3)):
        for x in range(1, len(b3[0])):
            b6 = b3[b11 - 1][x]
            b7 = b3[b11][x - 1]
            b8 = b3[b11 - 1][x - 1] + 1 if s1[x - 1] == s2[b11 - 1] else -1
            b9 = max(b6, b7, b8)
            b3[b11][x] = b9
            if b9 > b5:
                b5, max_row, b10 = b9, b11, x
            b4[b11][x] = "L" if b9 = = b7 else ("D" if b9 == b8 else "T")
    return max_row, b10, b5
def fonk5(b3, b4):
    print_table(b3, "b3.txt")
    print_table(b4, "b4.txt")
def fonk6(b4, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x, b11 = col, row
        b12 = ""
        while b4[b11][x] != "F":
            if b4[b11][x] == "L":
                x -= 1
            elif b4[b11][x] == "D":
                b12 = s1[x - 1] + b12
                x, b11 = x - 1, b11 - 1
            else:
                b11 -= 1
        for i in range(0, len(b12), 50):
            file.write(b12[i:i + 50] + "\n")
b13 = "AGCGTCTA"
b14 = "TGCATCTCG"
b15 = fonk1(b13, b14)
print(b13)
print(b14)
print("LCS Score: " + str(b15))