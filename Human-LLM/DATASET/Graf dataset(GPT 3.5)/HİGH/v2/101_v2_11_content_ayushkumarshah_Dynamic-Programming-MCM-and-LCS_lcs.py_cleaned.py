from time import time
def fonk1(b8, b9):
    b1 = len(b8)
    b2 = len(b9)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for b6 in range(1, b1 + 1):
        for b7 in range(1, b2 + 1):
            if b8[b6 - 1] == b9[b7 - 1]:
                b3[b6][b7] = b3[b6 - 1][b7 - 1] + 1
            else:
                b3[b6][b7] = max(b3[b6 - 1][b7], b3[b6][b7 - 1])
    b4 = b3[b1][b2]
    b5 = [""] * (b4 + 1)
    b6 = b1
    b7 = b2
    while b6 > 0 and b7 > 0:
        if b8[b6 - 1] == b9[b7 - 1]:
            b5[b4 - 1] = b8[b6 - 1]
            b6 -= 1
            b7 -= 1
            b4 -= 1
        elif b3[b6 - 1][b7] >= b3[b6][b7 - 1]:
            b6 -= 1
        else:
            b7 -= 1
    print("\nLength of LCS is", b3[b1][b2])
    print("LCS of", b8, "and", b9, "is", "".join(b5))
b8 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b9 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
for b6 in range(10):
    b10 = time()
    fonk1(b8[b6], b9[b6])
    b11 = time()
    print("Time taken:", b11 - b10)