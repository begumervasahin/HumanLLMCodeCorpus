def problem1():
    x = input("Enter the first sequence with no spaces between characters: ")
    y = input("Enter the second sequence with no spaces between characters: ")
    matrix = [[None] * len(y) for _ in range(len(x))]
    score = calculate_LCS_length(x, y, matrix)
    print(f"The length of the longest common sequence of:\n{x}\nand\n{y}\nis {score}\n")
    print("A longest common subsequence of X and Y is:")
    sequence = find_LCS(x, y, matrix)
    print(sequence)
def find_LCS(sequenceOne, sequenceTwo, array):
    def backtrack(i, j):
        if i == 0 or j == 0:
            return ""
        if sequenceOne[i - 1] == sequenceTwo[j - 1]:
            return backtrack(i - 1, j - 1) + sequenceOne[i - 1]
        top_score = array[i - 2][j - 1] if i >= 2 else None
        left_score = array[i - 1][j - 2] if j >= 2 else None
        if top_score is not None and left_score is not None and top_score >= left_score:
            return backtrack(i - 1, j)
        else:
            return backtrack(i, j - 1)
    return backtrack(len(sequenceOne), len(sequenceTwo))
def calculate_LCS_length(sequenceOne, sequenceTwo, array):
    def lcs_length(i, j):
        if i == 0 or j == 0:
            return 0
        if array[i - 1][j - 1] is not None:
            return array[i - 1][j - 1]
        if sequenceOne[i - 1] == sequenceTwo[j - 1]:
            array[i - 1][j - 1] = lcs_length(i - 1, j - 1) + 1
            return array[i - 1][j - 1]
        else:
            array[i - 1][j - 1] = max(lcs_length(i - 1, j), lcs_length(i, j - 1))
            return array[i - 1][j - 1]
    return lcs_length(len(sequenceOne), len(sequenceTwo))
problem1()