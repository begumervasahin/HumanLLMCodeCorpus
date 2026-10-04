from time import time
def lcs(X, Y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print("\nL table")
    for i in range(m+1):
        for j in range(n+1):
            print(str(L[i][j]) + "\t", end="")
        print("")
    index = L[m][n]
    org_index = index
    lcs = [""] * (index+1)
    lcs[index] = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] >= L[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("\nLength of LCS is " + str(org_index))
    print("LCS of " + X + " and " + Y + " is " + "".join(lcs))
el_time = []
mn = []
X = ["AGGTAB","ABRAC", "BACDB","AYUSH","KAMLESH","SUNIL","BIBASH","ARAJU","MANASI","DEEPESH"]
Y = ["GXTXAYB","YABBAD","BDCB","SHAHA","MAHES","UNATTI","SHOWIN","ARUNADHA","ANSI","DISH"]
for i in range(10):
    m = len(X[i])
    n = len(Y[i])
    start_time = time()
    lcs(X[i], Y[i], m, n)
    end_time = time()
    mn.append(m * n)
    el_time.append(end_time - start_time)
print("\nmn\tTime")
for i in range(10):
    print(str(mn[i]) + "\t" + str(el_time[i]))