def fonk1(A, b10):
    b1 = len(A)
    b2 = len(b10)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    b4 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b5 in range(1, b2 + 1):
            if A[i - 1] == b10[b5 - 1]:
                b3[i][b5] = b3[i - 1][b5 - 1] + 1
                b4[i][b5] = 0
            elif b3[i][b5 - 1] >= b3[i - 1][b5]:
                b3[i][b5] = b3[i][b5 - 1]
                b4[i][b5] = 1
            else:
                b3[i][b5] = b3[i - 1][b5]
                b4[i][b5] = 2
    i, b5 = b1, b2
    b6 = []
    while i > 0 and b5 > 0:
        if b4[i][b5] == 0:
            b6.append(A[i - 1])
            i -= 1
            b5 -= 1
        elif b4[i][b5] == 2:
            i -= 1
        else:
            b5 -= 1
    return str(b3[b1][b2]), ''.join(reversed(b6))
def fonk2(file_path):
    with open(file_path, "r") as file:
        b7 = file.readlines()
    return b7[0].strip(), b7[1].strip()
def fonk3(file_path, length, b11):
    with open(file_path, "w") as file:
        file.write(length + "\b1")
        file.write(b11)
b8 = "input.txt"
b9 = "output.txt"
A, b10 = fonk2(b8)
length, b11 = fonk1(A, b10)
fonk3(b9, length, b11)