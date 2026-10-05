from time import time
def fonk1(b8, b9):
    b1 = len(b8)
    b2 = len(b9)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b7 in range(1, b2 + 1):
            if b8[i - 1] == b9[b7 - 1]:
                b3[i][b7] = b3[i - 1][b7 - 1] + 1
            else:
                b3[i][b7] = max(b3[i - 1][b7], b3[i][b7 - 1])
    b4 = b3[b1][b2]
    b5 = b4
    b6 = [""] * (b4 + 1)
    i, b7 = b1, b2
    while i > 0 and b7 > 0:
        if b8[i - 1] == b9[b7 - 1]:
            b6[b4 - 1] = b8[i - 1]
            i -= 1
            b7 -= 1
            b4 -= 1
        elif b3[i - 1][b7] >= b3[i][b7 - 1]:
            i -= 1
        else:
            b7 -= 1
    print("\nLength of LCS is", b5)
    print("LCS of '{}' and '{}' is '{}'".format(b8, b9, "".join(b6)))
b8 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b9 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
b10 = []
b11 = []
for i in range(10):
    b12 = time()
    fonk1(b8[i], b9[i])
    b13 = time()
    b10.append(len(b8[i]) * len(b9[i]))
    b11.append(b13 - b12)
print("\nmn\tTime")
for i in range(10):
    print("{}\t{}".format(b10[i], b11[i]))