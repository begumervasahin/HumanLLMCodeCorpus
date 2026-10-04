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
def fonk3():
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
    for dims in b7:
        b8.append(len(dims) - 1)
        b10 = time()
        b1, b2 = fonk1(dims, len(dims))
        b11 = time()
        print(f"\b12 = {dims}")
        print("\nm table\b8")
        for b5 in range(1, b8[-1] + 1):
            for b3 in range(1, b8[-1] + 1):
                print(f"{b1[b5][b3]:7}", b6 = " ")
            print("")
        print("\ns table\b8")
        for b5 in range(1, b8[-1] + 1):
            for b3 in range(1, b8[-1] + 1):
                print(f"{b2[b5][b3]:7}", b6 = " ")
            print("")
        print("\nAns:", b6 = "")
        fonk2(b2, 1, b8[-1])
        print("")
        b9.append(b11 - b10)
    print("\b8\nn\tElapsed Time")
    for b5 in range(len(b8)):
        print(f"{b8[b5]}\t{b9[b5]:.6f}")
if b13 = = "__main__":
    fonk3()