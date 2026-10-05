import re
def verify_sequence(sequence):
    return re.match("^[ATCG ]*$", sequence)
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
    lcs_string = "".join(lcs_sequence).replace("\0", "")
    return lcs_string, len(lcs_string)
def main():
    s1 = input("Enter the First DNA Sequence\n").upper()
    s2 = input("\nEnter the Querying DNA Sequence\n").upper()
    if verify_sequence(s1) and verify_sequence(s2) and len(s1) >= len(s2):
        lcs_result, length = longest_common_subsequence(s1, s2)
        print(f"\nLongest Common Subsequence of the given two DNA sequences is '{lcs_result}' and its length is: {length}")
    elif len(s1) < len(s2):
        print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain only 'A', 'T', 'C', 'G', or space characters")
if __name__ == "__main__":
    main()