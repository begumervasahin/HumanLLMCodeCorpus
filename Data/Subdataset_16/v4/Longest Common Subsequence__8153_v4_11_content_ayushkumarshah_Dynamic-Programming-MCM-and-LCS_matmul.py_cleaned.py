import sys
from time import time
def fonk1(p, b8):
    b1 = [[0 for _ in range(b8)] for _ in range(b8)]
    b2 = [[0 for _ in range(b8)] for _ in range(b8)]
    for b5 in range(1, b8):
        b1[b5][b5] = 0
    for L in range(2, b8):
        for b5 in range(1, b8 - L + 1):
            b3 = b5 + L - 1
            b1[b5][b3] = sys.maxsize
            for k in range(b5, b3):
                b4 = b1[b5][k] + b1[k + 1][b3] + p[b5 - 1] * p[k] * p[b3]
                if b4 < b1[b5][b3]:
                    b1[b5][b3] = b4
                    b2[b5][b3] = k
    return b1, b2
def fonk2(b2, b5, b3):
    if b5 = = b3:
        print(f"A{b5}", b6 = "")
    else:
        print("(", b6 = "")
        fonk2(b2, b5, b2[b5][b3])
        fonk2(b2, b2[b5][b3] + 1, b3)
        print(")", b6 = "")
b7 = [
    [2, 3], [3, 4, 6], [1, 3, 6, 7], [5, 4, 6, 2, 7],
    [2, 4, 5, 6, 7, 8], [2, 4, 5, 3, 6, 7, 8], [4, 3, 2, 5, 6, 4, 3, 2],
    [3, 5, 6, 4, 3, 5, 6, 7, 8], [3, 4, 5, 3, 6, 7, 8, 9, 5, 10],
    [2, 4, 5, 7, 8, 2, 4, 10, 12, 5, 6]
]
b8 = []
b9 = []
for dims in b7:
    b10 = len(dims) - 1
    b8.append(b10)
    b11 = time()
    b1, b2 = fonk1(dims, len(dims))
    print(f"\b12 = {dims}")
    print("\nm table\b8")
    for row in b1[:b10]:
        print("\t".join(map(str, row[:b10])))
    print("\ns table\b8")
    for row in b2[:b10]:
        print("\t".join(map(str, row[:b10])))
    print("\nAns:", b6 = "")
    fonk2(b2, 1, b10)
    print("")
    b13 = time()
    b9.append(b13 - b11)
print("\b8\nn\tElapsed Time")
for b5 in range(10):
    print(f"{b8[b5]}\t{b9[b5]}")