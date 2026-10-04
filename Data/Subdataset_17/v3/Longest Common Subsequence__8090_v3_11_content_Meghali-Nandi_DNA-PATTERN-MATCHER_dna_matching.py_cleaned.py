import random
def generate_random_dna_sequence(length):
    letters = ["a", "c", "t", "g"]
    return ''.join(random.choice(letters) for _ in range(length))
def write_sequence_to_file(filename, sequence):
    with open(filename, "w") as file:
        file.write(sequence)
def read_sequence_from_file(filename):
    with open(filename, "r") as file:
        return file.read()
def find_lcs(X, Y):
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
    lcs_sequence = [""] * (index + 1)
    lcs_sequence[index] = ""
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
    lcs_str = "".join(lcs_sequence)
    print(f"LCS of the sequences is: {lcs_str}")
    print("Matching" if len(lcs_str) > 500 else "Not matching")
def main():
    length = 1000
    sequence1 = generate_random_dna_sequence(length)
    sequence2 = generate_random_dna_sequence(length)
    write_sequence_to_file("dna-sequence.txt", sequence1)
    write_sequence_to_file("dna-sequence2.txt", sequence2)
    X = read_sequence_from_file("dna-sequence.txt")
    Y = read_sequence_from_file("dna-sequence2.txt")
    find_lcs(X, Y)
if __name__ == "__main__":
    main()