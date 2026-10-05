import sys
from time import time
def fonk1(p, b10):
    b1 = [[0] * b10 for _ in range(b10)]
    b2 = [[0] * b10 for _ in range(b10)]
    for b5 in range(1, b10):
        b1[b5][b5] = 0
    for chain_length in range(2, b10):
        for b5 in range(1, b10 - chain_length + 1):
            b3 = b5 + chain_length - 1
            b1[b5][b3] = sys.maxsize
            for k in range(b5, b3):
                b4 = b1[b5][k] + b1[k+1][b3] + p[b5-1] * p[k] * p[b3]
                if b4 < b1[b5][b3]:
                    b1[b5][b3] = b4
                    b2[b5][b3] = k
    return b1, b2
def fonk2(b2, b5, b3):
    if b5 = = b3:
        print("A%d" % b5, b6 = "")
    else:
        print("(", b6 = "")
        fonk2(b2, b5, b2[b5][b3])
        fonk2(b2, b2[b5][b3]+1, b3)
        print(")", b6 = "")
b7 = [
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
b8 = []
b9 = []
for dimensions in b7:
    b10 = len(dimensions) - 1
    b8.append(b10)
    b11 = time()
    b4, b12 = fonk1(dimensions, b10 + 1)
    print("\nMatrix Dimensions:", dimensions)
    print("\nCost Matrix:")
    for b5 in range(1, b10 + 1):
        for b3 in range(1, b10 + 1):
            print(b4[b5][b3], b6 = "\t")
        print()
    print("\nSplit Matrix:")
    for b5 in range(1, b10 + 1):
        for b3 in range(1, b10 + 1):
            print(b12[b5][b3], b6 = "\t")
        print()
    print("\nOptimal Parenthesization:", b6 = "")
    fonk2(b12, 1, b10)
    print("")
    b13 = time()
    b9.append(b13 - b11)
print("\b10\nn\tElapsed Time")
for b5 in range(len(b7)):
    print(f"{b8[b5]}\t{b9[b5]}")