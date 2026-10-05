def fonk1(A, B):
    b1 = len(A)
    b2 = len(B)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    b4 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b5 in range(1, b2 + 1):
            if A[i - 1] == B[b5 - 1]:
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
            b6 = A[i - 1] + b6
            i -= 1
            b5 -= 1
        elif b4[i][b5] == 2:
            i -= 1
        else:
            b5 -= 1
    return b3[b1][b2], b6
b7 = "input.txt"
b8 = "output.txt"
with open(b7, "r") as file_in:
    b9 = file_in.readlines()
    b10 = b9[0].strip()
    b11 = b9[1].strip()
lcs_length, b12 = fonk1(b10, b11)
with open(b8, "w") as file_out:
    file_out.write(str(lcs_length) + "\b1")
    file_out.write(b12)
