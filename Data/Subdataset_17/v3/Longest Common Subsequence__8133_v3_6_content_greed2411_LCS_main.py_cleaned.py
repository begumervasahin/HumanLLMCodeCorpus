import re
def verify(sequence):
    return bool(re.match("^[ATCG ]*$", sequence))
def compute_lcs(X, Y):
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
    lcs_sequence = [""] * index
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
    return "".join(lcs_sequence)
def main():
    first_sequence = input("Enter the First Sequence\n").upper()
    query_sequence = input("Enter the Querying Sequence\n").upper()
    if verify(first_sequence) and verify(query_sequence):
        if len(first_sequence) >= len(query_sequence):
            lcs_result = compute_lcs(first_sequence, query_sequence)
            print(f"\n\nLCS of {first_sequence} and {query_sequence} is {lcs_result} \nand length of it is: {len(lcs_result)}")
        else:
            print("Querying Sequence should be smaller than First Sequence")
    else:
        print("The Sequences should contain 'A', 'T', 'C', 'G', ' ' only")
if __name__ == "__main__":
    main()