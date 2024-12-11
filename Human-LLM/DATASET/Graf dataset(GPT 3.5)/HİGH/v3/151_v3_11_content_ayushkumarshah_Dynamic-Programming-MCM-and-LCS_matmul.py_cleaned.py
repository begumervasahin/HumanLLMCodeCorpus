import sys
from time import time
def fonk1(size):
    return [[0] * size for _ in range(size)]
def fonk2(p):
    b1 = len(p) - 1
    b2 = fonk1(b1)
    b3 = fonk1(b1)
    for i in range(1, b1):
        b2[i][i] = 0
    for chain_length in range(2, b1 + 1):
        for start_matrix in range(1, b1 - chain_length + 2):
            b4 = start_matrix + chain_length - 1
            b2[start_matrix][b4] = sys.maxsize
            for k in range(start_matrix, b4):
                b5 = b2[start_matrix][k] + b2[k + 1][b4] + p[start_matrix - 1] * p[k] * p[b4]
                if b5 < b2[start_matrix][b4]:
                    b2[start_matrix][b4] = b5
                    b3[start_matrix][b4] = k
    return b2, b3
def fonk3(b3, b6, b7):
    if b6 = = b7:
        print("A%d" % b6, b7 = "")
    else:
        print("(", b7 = "")
        fonk3(b3, b6, b3[b6][b7])
        fonk3(b3, b3[b6][b7] + 1, b7)
        print(")", b7 = "")
b8 = [
    [2, 3],
    [3, 4, 6],
    [1, 3, 6, 7],
    [5, 4, 6, 2, 7],
    [2, 4, 5, 6, 7, 8],
    [2, 4, 5, 3, 6, 7, 8],
    [4, 3, 2, 5, 6, 4, 3, 2],
    [3, 5, 6, 4, 3, 5, 6, 7, 8],
    [3, 4, 5, 3, 6, 7, 8, 9, 5, 10],
    [2, 4, 5, 7, 8, 2, 4, 10, 12, 5, 6]
]
b9 = []
b10 = []
for dimension in b8:
    b11 = len(dimension) - 1
    b9.append(b11)
    b12 = time()
    b5, b13 = fonk2(dimension)
    print("\nMatrix Dimensions: " + str(dimension))
    print("\nOptimal Cost Matrix:\n")
    for i in range(b11):
        for j in range(b11):
            print(str(b5[i][j]) + "\t", b7 = "")
        print("")
    print("\nSplit Matrix:\n")
    for i in range(b11):
        for j in range(b11):
            print(str(b13[i][j]) + "\t", b7 = "")
        print("")
    print("\nOptimal Parenthesization:", b7 = "")
    fonk3(b13, 1, b11)
    print("")
    b14 = time()
    b10.append(b14 - b12)
print("\n\nMatrix Dimensions\tElapsed Time")
for i in range(len(b8)):
    print(str(b9[i]) + "\t\t\t" + str(b10[i]))