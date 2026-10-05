from time import time
def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    org_index = index
    lcs = [""] * (index + 1)
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("\nLength of LCS is", org_index)
    print("LCS of '{}' and '{}' is '{}'".format(X, Y, "".join(lcs)))
X = ["AGGTAB", "ABRAC", "BACDB", "AYUSH", "KAMLESH", "SUNIL", "BIBASH", "ARAJU", "MANASI", "DEEPESH"]
Y = ["GXTXAYB", "YABBAD", "BDCB", "SHAHA", "MAHES", "UNATTI", "SHOWIN", "ARUNADHA", "ANSI", "DISH"]
mn = []
el_time = []
for i in range(10):
    start_time = time()
    longest_common_subsequence(X[i], Y[i])
    end_time = time()
    mn.append(len(X[i]) * len(Y[i]))
    el_time.append(end_time - start_time)
print("\nmn\tTime")
for i in range(10):
    print("{}\t{}".format(mn[i], el_time[i]))