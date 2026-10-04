from time import time
def fonk1(b7, b8):
    m, b1 = len(b7), len(b8)
    b2 = [[0] * (b1 + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for b5 in range(1, b1 + 1):
            if b7[i - 1] == b8[b5 - 1]:
                b2[i][b5] = b2[i - 1][b5 - 1] + 1
            else:
                b2[i][b5] = max(b2[i - 1][b5], b2[i][b5 - 1])
    print("\nLCS table")
    for row in b2:
        print("\t".join(map(str, row)))
    b3 = b2[m][b1]
    b4 = [""] * (b3 + 1)
    b4[b3] = ""
    i, b5 = m, b1
    while i > 0 and b5 > 0:
        if b7[i - 1] == b8[b5 - 1]:
            b4[b3 - 1] = b7[i - 1]
            i -= 1
            b5 -= 1
            b3 -= 1
        elif b2[i - 1][b5] >= b2[i][b5 - 1]:
            i -= 1
        else:
            b5 -= 1
    b6 = "".join(b4)
    print(f"\nLength of LCS: {len(b6)}")
    print(f"LCS of {b7} and {b8}: {b6}")
b7 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b8 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
b9 = []
b10 = []
for x_str, y_str in zip(b7, b8):
    m, b1 = len(x_str), len(y_str)
    b11 = time()
    fonk1(x_str, y_str)
    b12 = time()
    b10.append(m * b1)
    b9.append(b12 - b11)
print("\nComplexity\tTime")
for complexity, elapsed in zip(b10, b9):
    print(f"{complexity}\t{elapsed:.6f}")