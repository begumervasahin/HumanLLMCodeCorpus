import random
def generate_dna_sequence(length, filename):
    letters = ["A", "C", "T", "G"]
    sequence = ''.join(random.choice(letters) for _ in range(length))
    with open(filename, "w") as file_txt:
        file_txt.write(sequence)
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
    lcs = [""] * (index + 1)
    lcs[index] = ""
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
    print("LCS of X and Y is:", "".join(lcs))
    if len(lcs) > 500:
        print("Matching")
    else:
        print("Not matching")
generate_dna_sequence(1000, "dna-sequence.txt")
generate_dna_sequence(1000, "dna-sequence2.txt")
X = open("dna-sequence.txt", "r").read()
Y = open("dna-sequence2.txt", "r").read()
longest_common_subsequence(X, Y)