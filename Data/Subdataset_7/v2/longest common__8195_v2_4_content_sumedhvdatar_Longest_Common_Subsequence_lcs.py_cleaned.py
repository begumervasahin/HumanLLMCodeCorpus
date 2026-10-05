import numpy as np
def fonk1(b1, position_column):
    if b1 = = 1 and position_column == 1:
        return b10
    if b7[b1][position_column] == b7[b1][position_column - 1]:
        fonk1(b1, position_column - 1)
    elif b7[b1][position_column] == b7[b1 - 1][position_column]:
        fonk1(b1 - 1, position_column)
    else:
        b2 = b7[b1 - 1][position_column - 1]
        if b7[b1][position_column] == b2 + 1:
            b10.append(b7[0][position_column])
            fonk1(b1 - 1, position_column - 1)
b3 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
b4 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
b5 = len(b4) + 2
b6 = len(b3) + 2
b7 = [[0 for _ in range(b6)] for _ in range(b5)]
b7[0][0] = "L"
b7[0][1] = "P"
for i, letter in enumerate(b3, b8 = 2):
    b7[0][i] = letter
    b7[1][i] = 0
for i, letter in enumerate(b4, b8 = 2):
    b7[i][0] = letter
    b7[i][1] = 0
for i in range(2, b5):
    for j in range(2, b6):
        if b7[i][0] == b7[0][j]:
            b9 = b7[i - 1][j - 1]
            b7[i][j] = b9 + 1
        else:
            b7[i][j] = max(b7[i][j - 1], b7[i - 1][j])
b10 = []
fonk1(b5 - 1, b6 - 1)
b11 = "".join(str(x) for x in b10)
b11 = b11[::-1]
print("Longest Common Subsequence:", b11)
print("Dynamic Programming Table:")
print(np.matrix(b7))