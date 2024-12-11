from time import time
def fonk1(b9, b10, b11, b12):
    b1 = [[0 for x in range(b12+1)] for x in range(b11+1)]
    for b2 in range(b11+1):
        for b6 in range(b12+1):
            if b2 = = 0 or b6 == 0:
                b1[b2][b6] = 0
            elif b9[b2-1] == b10[b6-1]:
                b1[b2][b6] = b1[b2-1][b6-1] + 1
            else:
                b1[b2][b6] = max(b1[b2-1][b6], b1[b2][b6-1])
    b3 = b1[b11][b12]
    b4 = b3
    b5 = [""] * (b3+1)
    b5[b3] = ""
    b2 = b11
    b6 = b12
    while b2 > 0 and b6 > 0:
        if b9[b2-1] == b10[b6-1]:
            b5[b3-1] = b9[b2-1]
            b2 -= 1
            b6 -= 1
            b3 -= 1
        elif b1[b2-1][b6] >= b1[b2][b6-1]:
            b2 -= 1
        else:
            b6 -= 1
    print ("\nLength of LCS is " + str(b4))
    print ("LCS of " + b9 + " and " + b10 + " is " + "".join(b5))
b7 = []
b8 = []
b9 = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
b10 = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
for b2 in range(10):
    b11 = len(b9[b2])
    b12 = len(b10[b2])
    b13 = time()
    fonk1(b9[b2], b10[b2], b11, b12)
    b14 = time()
    b8.append(b11*b12)
    b7.append(b14 - b13)
print("\nmn\tTime")
for b2 in range(10):
    print(str(b8[b2]) + "\t" + str(b7[b2]))