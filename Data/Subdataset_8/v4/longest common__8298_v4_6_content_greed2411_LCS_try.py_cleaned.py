import re
def verify_sequence(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def longest_common_subsequence(X, Y, m, n):
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = "\0"
    i = m
    j = n
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
    lcs_str = "".join(lcs).replace("\0", "")
    return lcs_str, len(lcs_str) - 1
def main():
    s1 = input("Enter the First Sequence\n").upper()
    s2 = input("\nEnter the Querying Sequence\n").upper()
    if verify_sequence(s1) and verify_sequence(s2) and len(s1) >= len(s2):
        print(f"Sequences: {s1}, {s2}")
        lcs_result, lcs_length = longest_common_subsequence(s1, s2, len(s1), len(s2))
        print(f"\nLongest Common Subsequence: {lcs_result}\nLength: {lcs_length}")
    elif not (len(s1) >= len(s2)):
        print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A', 'T', 'C', 'G', ' ' only")
if __name__ == "__main__":
    main()