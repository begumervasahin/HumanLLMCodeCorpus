from time import time
def fonk1(b9, b10):
    b1 = len(b9)
    b2 = len(b10)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for b6 in range(1, b2 + 1):
            if b9[i - 1] == b10[b6 - 1]:
                b3[i][b6] = b3[i - 1][b6 - 1] + 1
            else:
                b3[i][b6] = max(b3[i - 1][b6], b3[i][b6 - 1])
    print("\nL table")
    for row in b3:
        print("\t".join(map(str, row)))
    b4 = b3[b1][b2]
    b5 = [""] * (b4 + 1)
    b5[b4] = ""
    i, b6 = b1, b2
    while i > 0 and b6 > 0:
        if b9[i - 1] == b10[b6 - 1]:
            b5[b4 - 1] = b9[i - 1]
            i -= 1
            b6 -= 1
            b4 -= 1
        elif b3[i - 1][b6] >= b3[i][b6 - 1]:
            i -= 1
        else:
            b6 -= 1
    print(f"\nLength of LCS is {b3[b1][b2]}")
    print(f"LCS of {b9} and {b10} is {''.join(b5)}")
b7 = []
b8 = []
b9 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b10 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
for i in range(10):
    b11 = time()
    fonk1(b9[i], b10[i])
    b12 = time()
    b8.append(len(b9[i]) * len(b10[i]))
    b7.append(b12 - b11)
print("\nmn\tTime")
for mn_val, time_val in zip(b8, b7):
    print(f"{mn_val}\t{time_val:.5f}")