def fonk1(b10, b11):
    b1 = len(b10)
    b2 = len(b11)
    b3 = [[0 for _ in range(b2 + 1)] for _ in range(b1 + 1)]
    b4 = [[0 for _ in range(b2 + 1)] for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b5 in range(1, b2 + 1):
            if b10[i - 1] == b11[b5 - 1]:
                b3[i][b5] = b3[i - 1][b5 - 1] + 1
                b4[i][b5] = 0
            elif b3[i][b5 - 1] >= b3[i - 1][b5]:
                b3[i][b5] = b3[i][b5 - 1]
                b4[i][b5] = 1
            else:
                b3[i][b5] = b3[i - 1][b5]
                b4[i][b5] = 2
    i, b5 = b1, b2
    b6 = ''
    while i > 0 and b5 > 0:
        if b4[i][b5] == 0:
            b6 = b10[i - 1] + b6
            i -= 1
            b5 -= 1
        elif b4[i][b5] == 2:
            i -= 1
        else:
            b5 -= 1
    return str(b3[b1][b2]), b6
def fonk2():
    b7 = "input.txt"
    b8 = "output.txt"
    with open(b7, "r") as file_in:
        b9 = file_in.readlines()
    b10 = b9[0].strip()
    b11 = b9[1].strip()
    length, b12 = fonk1(b10, b11)
    with open(b8, "w") as file_out:
        file_out.write(length + "\b1")
        file_out.write(b12)
if b13 = = "__main__":
    fonk2()