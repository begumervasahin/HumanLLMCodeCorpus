def longest_common_sequence():
    x = input("Enter the first sequence with no spaces between characters: ")
    y = input("Enter the second sequence with no spaces between characters: ")
    matrix = [[None] * len(y) for _ in range(len(x))]
    length = calculate_LCS(x, y, matrix, len(x), len(y))
    print(f"The length of the longest common sequence of\n{x}\nand\n{y}\nis {length}")
    print()
    print("A longest common subsequence of X and Y is:")
    sequence = find_LCS(x, y, matrix, len(x), len(y))
    print(sequence)
def find_LCS(sequence_one, sequence_two, matrix, i, j):
    if i == 0 or j == 0:
        return ""
    if sequence_one[i - 1] == sequence_two[j - 1]:
        return find_LCS(sequence_one, sequence_two, matrix, i - 1, j - 1) + sequence_one[i - 1]
    else:
        top_score = matrix[i - 2][j - 1] if i >= 2 else None
        left_score = matrix[i - 1][j - 2] if j >= 2 else None
        if top_score is not None and left_score is not None and top_score >= left_score:
            return find_LCS(sequence_one, sequence_two, matrix, i - 1, j)
        else:
            return find_LCS(sequence_one, sequence_two, matrix, i, j - 1)
def calculate_LCS(sequence_one, sequence_two, matrix, i, j):
    if i == 0 or j == 0:
        return 0
    elif matrix[i - 1][j - 1] is not None:
        return matrix[i - 1][j - 1]
    if sequence_one[i - 1] == sequence_two[j - 1]:
        if matrix[i - 1][j - 1] is not None:
            return 1 + matrix[i - 1][j - 1]
        else:
            score = calculate_LCS(sequence_one, sequence_two, matrix, i - 1, j - 1) + 1
            matrix[i - 1][j - 1] = score
            return score
    else:
        score = max(calculate_LCS(sequence_one, sequence_two, matrix, i - 1, j),
                    calculate_LCS(sequence_one, sequence_two, matrix, i, j - 1))
        matrix[i - 1][j - 1] = score
        return score
longest_common_sequence()