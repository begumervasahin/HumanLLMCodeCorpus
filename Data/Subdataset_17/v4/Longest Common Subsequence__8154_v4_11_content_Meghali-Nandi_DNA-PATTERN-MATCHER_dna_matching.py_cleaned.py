import random
def generate_random_dna_sequence(length, filename):
    letters = ["a", "c", "t", "g"]
    sequence = ''.join(random.choice(letters) for _ in range(length))
    with open(filename, "a") as file:
        file.write(sequence)
def find_lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    index = L[m][n]
    lcs = [""] * (index+1)
    lcs[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs)
def main():
    length = 1000
    generate_random_dna_sequence(length, "dna-sequence.txt")
    generate_random_dna_sequence(length, "dna-sequence2.txt")
    X = open("dna-sequence.txt", "r").read()
    Y = open("dna-sequence2.txt", "r").read()
    lcs_result = find_lcs(X, Y)
    print(f"LCS of the DNA sequences is {lcs_result}")
    if len(lcs_result) > 500:
        print("Matching")
    else:
        print("Not matching")
if __name__ == "__main__":
    main()