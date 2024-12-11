import numpy as np
def fonk1(b8, b9):
    b1 = len(b9) + 2
    b2 = len(b8) + 2
    b3 = [[0] * b2 for _ in range(b1)]
    b3[0][0], b3[0][1] = "L", "P"
    b3[1][0] = "P"
    for i, letter in enumerate(b8, b4 = 2):
        b3[0][i] = letter
        b3[1][i] = 0
    for i, letter in enumerate(b9, b4 = 2):
        b3[i][0] = letter
        b3[i][1] = 0
    return b3
def fonk2(b3, b8, b9):
    for i in range(2, len(b9) + 2):
        for j in range(2, len(b8) + 2):
            if b3[i][0] == b3[0][j]:
                b3[i][j] = b3[i - 1][j - 1] + 1
            else:
                b3[i][j] = max(b3[i][j - 1], b3[i - 1][j])
def fonk3(b3):
    b5 = []
    b1, b2 = len(b3) - 1, len(b3[0]) - 1
    while b1 > 1 and b2 > 1:
        if b3[b1][b2] == b3[b1][b2 - 1]:
            b2 -= 1
        elif b3[b1][b2] == b3[b1 - 1][b2]:
            b1 -= 1
        else:
            b5.append(b3[0][b2])
            b1, b2 = b1 - 1, b2 - 1
    return ''.join(reversed(b5))
def fonk4(b8, b9):
    b3 = fonk1(b8, b9)
    fonk2(b3, b8, b9)
    b6 = fonk3(b3)
    return b6, b3
if b7 = = "__main__":
    b8 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
    b9 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
    b6, b3 = fonk4(b8, b9)
    print("Longest Common Subsequence:", b6)
    print("Dynamic Programming Table:")
    print(np.matrix(b3))