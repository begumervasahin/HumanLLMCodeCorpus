import re
def verify(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def compute_lcs_matrix(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L
def backtrack_lcs(X, Y, L):
    m, n = len(X), len(Y)
    index = L[m][n]
    lcs = [""] * index
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs)
def lcs(X, Y):
    L = compute_lcs_matrix(X, Y)
    lcs_result = backtrack_lcs(X, Y, L)
    print(f"\n\nLCS of {X} and {Y} is {lcs_result} \nand length of it is: {len(lcs_result)}")
def main():
    s1 = input("Enter the First Sequence\n").upper()
    s2 = input("\nEnter the Querying Sequence\n").upper()
    if verify(s1) and verify(s2):
        if len(s1) >= len(s2):
            lcs(s1, s2)
        else:
            print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A', 'T', 'C', 'G', ' ' only")
if __name__ == "__main__":
    main()