from time import time
def fonk1(b7, b8):
    b1 = len(b7)
    b2 = len(b8)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b6 in range(1, b2 + 1):
            if b7[i - 1] == b8[b6 - 1]:
                b3[i][b6] = b3[i - 1][b6 - 1] + 1
            else:
                b3[i][b6] = max(b3[i - 1][b6], b3[i][b6 - 1])
    b4 = b3[b1][b2]
    b5 = [""] * (b4 + 1)
    i, b6 = b1, b2
    while i > 0 and b6 > 0:
        if b7[i - 1] == b8[b6 - 1]:
            b5[b4 - 1] = b7[i - 1]
            i -= 1
            b6 -= 1
            b4 -= 1
        elif b3[i - 1][b6] >= b3[i][b6 - 1]:
            i -= 1
        else:
            b6 -= 1
    print("\nLength of LCS is", b3[b1][b2])
    print("LCS of '{}' and '{}' is '{}'".format(b7, b8, "".join(b5)))
b7 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b8 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
for i in range(10):
    b9 = time()
    fonk1(b7[i], b8[i])
    b10 = time()
    print("Time taken:", b10 - b9)