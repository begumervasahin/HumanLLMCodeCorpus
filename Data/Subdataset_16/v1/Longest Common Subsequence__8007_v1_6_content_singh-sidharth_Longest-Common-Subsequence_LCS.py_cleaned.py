def fonk1(b6, b7):
    b1 = len(b6)
    b2 = len(b7)
    b3 = [[None] * (b2 + 1) for _ in range(b1 + 1)]
    for b4 in range(b1 + 1):
        for j in range(b2 + 1):
            if b4 = = 0 or j == 0:
                b3[b4][j] = 0
            elif b6[b4 - 1] == b7[j - 1]:
                b3[b4][j] = b3[b4 - 1][j - 1] + 1
            else:
                b3[b4][j] = max(b3[b4 - 1][j], b3[b4][j - 1])
    return b3[b1][b2]
if b5 = = "__main__":
    b6 = input("First string: ")
    b7 = input("Second string: ")
    print("The length of LCS is:", fonk1(b6, b7))