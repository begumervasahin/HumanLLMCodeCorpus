import sys
from time import time
def fonk1(p, b7):
    b1 = [[0 for x in range(b7)] for x in range(b7)]
    b2 = [[0 for x in range(b7)] for x in range(b7)]
    for b5 in range(1, b7):
        b1[b5][b5] = 0
    for L in range(2, b7):
        for b5 in range(1, b7 - L + 1):
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
    b7 = []
    b8 = []
    b9 = [
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
    for b3 in range(10):
        b7.append(len(b9[b3]) - 1)
        b10 = time()
        b1, b2 = fonk1(b9[b3], len(b9[b3]))
        print(f"\b11 = {b9[b3]}")
        print("\nm table\b7")
        for b5 in range(1, b7[b3] + 1):
            for b3 in range(1, b7[b3] + 1):
                print(f"{b1[b5][b3]:7}", b6 = " ")
            print("")
        print("\ns table\b7")
        for b5 in range(1, b7[b3] + 1):
            for b3 in range(1, b7[b3] + 1):
                print(f"{b2[b5][b3]:7}", b6 = " ")
            print("")
        print("\nAns:", b6 = "")
        fonk2(b2, 1, b7[b3])
        print("")
        b12 = time()
        b8.append(b12 - b10)
    print("\b7\nn\tElapsed Time")
    for b5 in range(10):
        print(f"{b7[b5]}\t{b8[b5]:.6f}")
if b13 = = "__main__":
    fonk3()