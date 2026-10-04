import numpy as np
def fonk1(b1, position_column):
    if b1 = = 1 or position_column == 1:
        return
    if b7[b1][position_column] == b7[b1][position_column-1]:
        fonk1(b1, position_column-1)
    elif b7[b1][position_column] == b7[b1-1][position_column]:
        fonk1(b1-1, position_column)
    else:
        b2 = b7[b1-1][position_column-1]
        if b7[b1][position_column] == b2 + 1:
            b9.append(b7[0][position_column])
            fonk1(b1-1, position_column-1)
b3 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
b4 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
b5 = len(b3) + 2
b6 = len(b4) + 2
b7 = [[0] * b5 for _ in range(b6)]
b7[0][2:] = list(b3)
b7[1][2:] = [0] * len(b3)
for i, letter in enumerate(b4, b8 = 2):
    b7[i][0] = letter
    b7[i][1] = 0
for i in range(2, b6):
    for j in range(2, b5):
        if b7[i][0] == b7[0][j]:
            b7[i][j] = b7[i-1][j-1] + 1
        else:
            b7[i][j] = max(b7[i][j-1], b7[i-1][j])
print("Printing the matrix:")
print(np.matrix(b7))
b9 = []
print("We are sending row " + str(b6))
print("We are sending column " + str(b5))
fonk1(b6-1, b5-1)
b10 = "".join(b9)[::-1]
print("Longest Common Subsequence:", b10)