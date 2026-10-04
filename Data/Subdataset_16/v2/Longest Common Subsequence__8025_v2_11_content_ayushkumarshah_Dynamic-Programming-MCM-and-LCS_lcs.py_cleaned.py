from time import time
def fonk1(b10, b11):
    m, b1 = len(b10), len(b11)
    b2 = [[0] * (b1 + 1) for _ in range(m + 1)]
    for b3 in range(m + 1):
        for b6 in range(b1 + 1):
            if b3 = = 0 or b6 == 0:
                b2[b3][b6] = 0
            elif b10[b3 - 1] == b11[b6 - 1]:
                b2[b3][b6] = b2[b3 - 1][b6 - 1] + 1
            else:
                b2[b3][b6] = max(b2[b3 - 1][b6], b2[b3][b6 - 1])
    print("\nL table")
    for row in b2:
        print("\t".join(map(str, row)))
    b4 = b2[m][b1]
    b5 = [""] * (b4 + 1)
    b5[b4] = ""
    b3, b6 = m, b1
    while b3 > 0 and b6 > 0:
        if b10[b3 - 1] == b11[b6 - 1]:
            b5[b4 - 1] = b10[b3 - 1]
            b3 -= 1
            b6 -= 1
            b4 -= 1
        elif b2[b3 - 1][b6] >= b2[b3][b6 - 1]:
            b3 -= 1
        else:
            b6 -= 1
    b7 = "".join(b5)
    print(f"\nLength of LCS is {len(b7)}")
    print(f"LCS of {b10} and {b11} is {b7}")
b8 = []
b9 = []
b10 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b11 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
for x_str, y_str in zip(b10, b11):
    m, b1 = len(x_str), len(y_str)
    b12 = time()
    fonk1(x_str, y_str)
    b13 = time()
    b9.append(m * b1)
    b8.append(b13 - b12)
print("\nmn\tTime")
for m_n, elapsed in zip(b9, b8):
    print(f"{m_n}\t{elapsed}")