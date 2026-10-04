import re
def verify(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs_str = [""] * index
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs_str)
s1 = input("Enter the First Sequence: ").upper()
s2 = input("Enter the Querying Sequence: ").upper()
if verify(s1) and verify(s2):
    if len(s1) >= len(s2):
        print(f"First Sequence: {s1}\nQuerying Sequence: {s2}")
        result = lcs(s1, s2)
        print(f"\nLCS of the given two DNA sequences is {result}\nand length of it is: {len(result)}")
    else:
        print("Querying Sequence should be smaller than or equal to the First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', or spaces only")