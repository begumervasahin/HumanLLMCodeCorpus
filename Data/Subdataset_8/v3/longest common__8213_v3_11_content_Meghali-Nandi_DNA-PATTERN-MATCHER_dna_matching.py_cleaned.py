import random
def generate_dna_sequence(length, filename):
    nucleotides = ["A", "C", "T", "G"]
    sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    with open(filename, "w") as file_txt:
        file_txt.write(sequence)
def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif lcs_lengths[i - 1][j] > lcs_lengths[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("Longest Common Subsequence of X and Y is:", "".join(reversed(lcs)))
    if len(lcs) > 500:
        print("Matching")
    else:
        print("Not matching")
generate_dna_sequence(1000, "dna-sequence.txt")
generate_dna_sequence(1000, "dna-sequence2.txt")
X = open("dna-sequence.txt", "r").read()
Y = open("dna-sequence2.txt", "r").read()
longest_common_subsequence(X, Y)