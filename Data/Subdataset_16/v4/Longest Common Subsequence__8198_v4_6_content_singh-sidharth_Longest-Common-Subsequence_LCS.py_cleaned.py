def fonk1(b4, b5):
    b1 = len(b4)
    b2 = len(b5)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for j in range(1, b2 + 1):
            if b4[i - 1] == b5[j - 1]:
                b3[i][j] = b3[i - 1][j - 1] + 1
            else:
                b3[i][j] = max(b3[i - 1][j], b3[i][j - 1])
    return b3[b1][b2]
b4 = input("First string: ")
b5 = input("Second string: ")
print("The length of the LCS is:", fonk1(b4, b5))