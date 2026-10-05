import re
def verify(s):
    return re.match("^[ATCG ]*$", s)
def lcs(X, Y, m, n):
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
    lcs_sequence = [""] * (index + 1)
    lcs_sequence[index] = "\0"
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs_string = "".join(lcs_sequence).replace("\0", "")
    return lcs_string, len(lcs_string)
s1 = input("Enter the First Sequence\n").upper()
s2 = input("\nEnter the Querying Sequence\n").upper()
if verify(s1) and verify(s2) and len(s1) >= len(s2):
    lcs_result, length = lcs(s1, s2, len(s1), len(s2))
    print(f"\nLCS of the given two DNA sequences is {lcs_result} and its length is: {length}")
elif len(s1) < len(s2):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain only 'A', 'T', 'C', 'G', or space characters")