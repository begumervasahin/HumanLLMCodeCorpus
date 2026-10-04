import sys
from time import time
def fonk1(p):
    b1 = len(p)
    b2 = [[0 for _ in range(b1)] for _ in range(b1)]
    b3 = [[0 for _ in range(b1)] for _ in range(b1)]
    for L in range(2, b1):
        for b6 in range(1, b1 - L + 1):
            b4 = b6 + L - 1
            b2[b6][b4] = sys.maxsize
            for k in range(b6, b4):
                b5 = b2[b6][k] + b2[k + 1][b4] + p[b6 - 1] * p[k] * p[b4]
                if b5 < b2[b6][b4]:
                    b2[b6][b4] = b5
                    b3[b6][b4] = k
    return b2, b3
def fonk2(b3, b6, b4):
    if b6 = = b4:
        print(f"A{b6}", b7 = "")
    else:
        print("(", b7 = "")
        fonk2(b3, b6, b3[b6][b4])
        fonk2(b3, b3[b6][b4] + 1, b4)
        print(")", b7 = "")
def fonk3(dims):
    b1 = len(dims) - 1
    b8 = time()
    b2, b3 = fonk1(dims)
    b9 = time()
    print(f"\b10 = {dims}")
    print("\nm table\b1")
    for b6 in range(1, b1 + 1):
        for b4 in range(1, b1 + 1):
            print(f"{b2[b6][b4]:7}", b7 = " ")
        print("")
    print("\ns table\b1")
    for b6 in range(1, b1 + 1):
        for b4 in range(1, b1 + 1):
            print(f"{b3[b6][b4]:7}", b7 = " ")
        print("")
    print("\nAns:", b7 = "")
    fonk2(b3, 1, b1)
    print("")
    return b1, b9 - b8
def fonk4():
    b11 = [
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
    b12 = [fonk3(dims) for dims in b11]
    print("\b1\nn\tElapsed Time")
    for b1, elapsed_time in b12:
        print(f"{b1}\t{elapsed_time:.6f}")
if b13 = = "__main__":
    fonk4()