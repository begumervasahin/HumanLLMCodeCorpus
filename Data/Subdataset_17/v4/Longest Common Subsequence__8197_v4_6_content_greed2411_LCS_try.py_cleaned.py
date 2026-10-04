import re
def verify(sequence):
    return re.match("^[ATCG ]*$", sequence)
def lcs(X, Y, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
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
    i, j = m, n
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
    lcs_string = "".join(lcs_sequence).strip("\0")
    print(f"\n\nLCS of {X} and {Y} is {lcs_string}")
    print(f"Length of LCS: {len(lcs_string)}")
s1 = input("Enter the First Sequence\n").upper()
s2 = input("Enter the Querying Sequence\n").upper()
if verify(s1) and verify(s2) and len(s1) >= len(s2):
    print((s1, s2))
    lcs(s1, s2, len(s1), len(s2))
elif not (len(s1) >= len(s2)):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', or space only")