def get_input():
    x = input("Enter the first sequence with no spaces between characters: ")
    y = input("Enter the second sequence with no spaces between characters: ")
    return x, y
def initialize_matrix(x, y):
    return [[None for _ in range(len(y))] for _ in range(len(x))]
def longest_common_subsequence(x, y, matrix, i, j):
    if i == 0 or j == 0:
        return 0
    if matrix[i-1][j-1] is not None:
        return matrix[i-1][j-1]
    if x[i-1] == y[j-1]:
        score = longest_common_subsequence(x, y, matrix, i-1, j-1) + 1
    else:
        score = max(
            longest_common_subsequence(x, y, matrix, i-1, j),
            longest_common_subsequence(x, y, matrix, i, j-1)
        )
    matrix[i-1][j-1] = score
    return score
def reconstruct_lcs(x, y, matrix, i, j):
    if i == 0 or j == 0:
        return ""
    if x[i-1] == y[j-1]:
        return reconstruct_lcs(x, y, matrix, i-1, j-1) + x[i-1]
    elif matrix[i-2][j-1] >= matrix[i-1][j-2]:
        return reconstruct_lcs(x, y, matrix, i-1, j)
    else:
        return reconstruct_lcs(x, y, matrix, i, j-1)
def print_lcs_details(x, y, score, sequence):
    print(f"The length of the longest common subsequence of {x} and {y} is {score}")
    print()
    print("A longest common subsequence of X and Y is")
    print(sequence)
def main():
    x, y = get_input()
    matrix = initialize_matrix(x, y)
    score = longest_common_subsequence(x, y, matrix, len(x), len(y))
    sequence = reconstruct_lcs(x, y, matrix, len(x), len(y))
    print_lcs_details(x, y, score, sequence)
if __name__ == "__main__":
    main()