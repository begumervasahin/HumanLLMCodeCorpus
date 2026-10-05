import re
def verify_sequence(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def find_lcs(X, Y, m, n):
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    lcs_length = L[m][n]
    lcs = [""] * (lcs_length + 1)
    lcs[lcs_length] = "\0"
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[lcs_length-1] = X[i-1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    print("\n\nLCS of " + X + " and " + Y + " is " + "".join(lcs) +
          " \nand length of it is : " + str(len("".join(lcs))-1))
sequence1 = input("Enter the First Sequence\n").upper()
sequence2 = input("\nEnter the Querying Sequence\n").upper()
if (verify_sequence(sequence1) and verify_sequence(sequence2)) and (len(sequence1) >= len(sequence2)):
    print(sequence1, sequence2)
    m = len(sequence1)
    n = len(sequence2)
    find_lcs(sequence1, sequence2, m, n)
elif not (len(sequence1) >= len(sequence2)):
    print("Querying Sequence should be smaller than First Sequence")
else:
    print("The Sequences should contain 'A', 'T', 'C', 'G', or space characters only")