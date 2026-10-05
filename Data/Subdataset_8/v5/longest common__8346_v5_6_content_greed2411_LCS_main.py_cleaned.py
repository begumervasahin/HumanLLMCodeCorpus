import re
def verify_sequence(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def find_lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    lcs_length = L[m][n]
    lcs = [''] * (lcs_length + 1)
    lcs[lcs_length] = '\0'
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print(f"\n\nLCS of {X} and {Y} is {''.join(lcs)}\nand its length is: {len(''.join(lcs)) - 1}")
sequence1 = input("Enter the First Sequence\n").upper()
sequence2 = input("\nEnter the Querying Sequence\n").upper()
if verify_sequence(sequence1) and verify_sequence(sequence2) and len(sequence1) >= len(sequence2):
    print(sequence1, sequence2)
    find_lcs(sequence1, sequence2)
elif len(sequence1) < len(sequence2):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', or space characters only")