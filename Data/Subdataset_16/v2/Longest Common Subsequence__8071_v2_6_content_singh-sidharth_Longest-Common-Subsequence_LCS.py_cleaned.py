def fonk1(b5, b6):
    b1 = len(b5)
    b2 = len(b6)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for j in range(1, b2 + 1):
            if b5[i - 1] == b6[j - 1]:
                b3[i][j] = b3[i - 1][j - 1] + 1
            else:
                b3[i][j] = max(b3[i - 1][j], b3[i][j - 1])
    return b3[b1][b2]
if b4 = = "__main__":
    b5 = input("First string: ")
    b6 = input("Second string: ")
    print("The length of LCS is:", fonk1(b5, b6))