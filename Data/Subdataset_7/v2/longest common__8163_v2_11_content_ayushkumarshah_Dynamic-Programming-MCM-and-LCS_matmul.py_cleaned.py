import sys
from time import time
def fonk1(p):
    b1 = len(p) - 1
    b2 = [[0] * b1 for _ in range(b1)]
    b3 = [[0] * b1 for _ in range(b1)]
    for b6 in range(1, b1):
        b2[b6][b6] = 0
    for l in range(2, b1 + 1):
        for b6 in range(1, b1 - l + 2):
            b4 = b6 + l - 1
            b2[b6][b4] = sys.maxsize
            for k in range(b6, b4):
                b5 = b2[b6][k] + b2[k + 1][b4] + p[b6 - 1] * p[k] * p[b4]
                if b5 < b2[b6][b4]:
                    b2[b6][b4] = b5
                    b3[b6][b4] = k
    return b2, b3
def fonk2(b3, b6, b4):
    if b6 = = b4:
        print("A%d" % b6, b7 = "")
    else:
        print("(", b7 = "")
        fonk2(b3, b6, b3[b6][b4])
        fonk2(b3, b3[b6][b4] + 1, b4)
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
b1 = []
b9 = []
for b4 in range(10):
    b1.append(len(b8[b4]) - 1)
    b10 = time()
    b2, b3 = fonk1(b8[b4])
    print("\b11 = " + str(b8[b4]))
    print("\nOptimal Cost Matrix:\b1")
    for b6 in range(b1[b4]):
        for b4 in range(b1[b4]):
            print(str(b2[b6][b4]) + "\t", b7 = "")
        print("")
    print("\nSplit Matrix:\b1")
    for b6 in range(b1[b4]):
        for b4 in range(b1[b4]):
            print(str(b3[b6][b4]) + "\t", b7 = "")
        print("")
    print("\nOptimal Parenthesization:", b7 = "")
    fonk2(b3, 1, b1[b4])
    print("")
    b12 = time()
    b9.append(b12 - b10)
print("\b1\nn\tElapsed Time")
for b6 in range(10):
    print(str(b1[b6]) + "\t" + str(b9[b6]))