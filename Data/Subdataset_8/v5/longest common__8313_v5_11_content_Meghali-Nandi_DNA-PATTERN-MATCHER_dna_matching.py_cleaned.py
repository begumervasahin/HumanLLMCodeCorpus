import random
def generate_random_dna_sequence(length):
    nucleotides = ["A", "C", "T", "G"]
    return ''.join(random.choice(nucleotides) for _ in range(length))
def write_dna_sequence_to_file(sequence, filename):
    with open(filename, "a") as file_txt:
        file_txt.write(sequence)
def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs = [""] * (index + 1)
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
    print("Longest Common Subsequence of X and Y is:", "".join(lcs))
    if len(lcs) > 500:
        print("Matching")
    else:
        print("Not matching")
sequence1 = generate_random_dna_sequence(1000)
sequence2 = generate_random_dna_sequence(1000)
write_dna_sequence_to_file(sequence1, "dna-sequence.txt")
write_dna_sequence_to_file(sequence2, "dna-sequence2.txt")
with open("dna-sequence.txt", "r") as file_txt:
    X = file_txt.read()
with open("dna-sequence2.txt", "r") as file_txt:
    Y = file_txt.read()
longest_common_subsequence(X, Y)