def lcs(sequence_one, sequence_two, matrix, i, j):
    if i == 0 or j == 0:
        return 0
    if matrix[i - 1][j - 1] is not None:
        return matrix[i - 1][j - 1]
    if sequence_one[i - 1] == sequence_two[j - 1]:
        score = lcs(sequence_one, sequence_two, matrix, i - 1, j - 1) + 1
    else:
        score = max(lcs(sequence_one, sequence_two, matrix, i - 1, j),
                    lcs(sequence_one, sequence_two, matrix, i, j - 1))
    matrix[i - 1][j - 1] = score
    return score
def reconstruct_lcs(sequence_one, sequence_two, matrix, i, j):
    if i == 0 or j == 0:
        return ""
    if sequence_one[i - 1] == sequence_two[j - 1]:
        return reconstruct_lcs(sequence_one, sequence_two, matrix, i - 1, j - 1) + sequence_one[i - 1]
    else:
        top_score = matrix[i - 2][j - 1] if i - 2 >= 0 else None
        left_score = matrix[i - 1][j - 2] if j - 2 >= 0 else None
        if top_score is not None and left_score is not None and top_score >= left_score:
            return reconstruct_lcs(sequence_one, sequence_two, matrix, i - 1, j)
        else:
            return reconstruct_lcs(sequence_one, sequence_two, matrix, i, j - 1)
def get_user_input():
    x = input("Enter the first sequence with no spaces between characters: ")
    y = input("Enter the second sequence with no spaces between characters: ")
    return x, y
def initialize_matrix(x, y):
    return [[None] * len(y) for _ in range(len(x))]
def display_results(x, y, score, sequence):
    print(f"The length of the longest common subsequence of {x} and {y} is {score}\n")
    print("A longest common subsequence of X and Y is")
    print(sequence)
def main():
    x, y = get_user_input()
    matrix = initialize_matrix(x, y)
    score = lcs(x, y, matrix, len(x), len(y))
    sequence = reconstruct_lcs(x, y, matrix, len(x), len(y))
    display_results(x, y, score, sequence)
def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(elem) if elem is not None else '-' for elem in row]))
    print()
if __name__ == "__main__":
    main()