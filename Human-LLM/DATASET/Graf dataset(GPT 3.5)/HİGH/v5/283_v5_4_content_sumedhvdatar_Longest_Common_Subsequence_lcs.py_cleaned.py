import numpy as np
def fonk1(b1, b5):
    if b1 = = 1 and b5 == 1:
        return b9
    if b6[b1][b5] == b6[b1][b5 - 1]:
        fonk1(b1, b5 - 1)
    elif b6[b1][b5] == b6[b1 - 1][b5]:
        fonk1(b1 - 1, b5)
    else:
        b2 = b6[b1 - 1][b5 - 1]
        if b6[b1][b5] == b2 + 1:
            b9.append(b6[0][b5])
            fonk1(b1 - 1, b5 - 1)
b3 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
b4 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
b1 = len(b4) + 2
b5 = len(b3) + 2
b6 = [['' for _ in range(b5)] for _ in range(b1)]
b6[0][0] = "L"
b6[0][1] = "P"
b6[1][0] = "P"
for i, letter in enumerate(b3, b7 = 2):
    b6[0][i] = letter
    b6[1][i] = 0
for i, letter in enumerate(b4, b7 = 2):
    b6[i][0] = letter
    b6[i][1] = 0
for i in range(2, b1):
    for j in range(2, b5):
        if b6[i][0] == b6[0][j]:
            b8 = b6[i - 1][j - 1]
            b6[i][j] = b8 + 1
        else:
            b6[i][j] = max(b6[i][j - 1], b6[i - 1][j])
print("LCS Matrix:")
print(np.matrix(b6))
b9 = []
print("Row: ", b1)
print("Column: ", b5)
b10 = fonk1(b1 - 1, b5 - 1)
b11 = "".join(str(x) for x in b9)
print("Longest Common Subsequence (LCS):", b11[::-1])