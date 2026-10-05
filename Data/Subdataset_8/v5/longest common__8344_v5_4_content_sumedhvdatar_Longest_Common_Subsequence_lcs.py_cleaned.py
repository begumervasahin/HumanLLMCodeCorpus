import numpy as np
def get_longest_common_subsequence(row, column):
    if row == 1 and column == 1:
        return final_sequence
    if table[row][column] == table[row][column - 1]:
        get_longest_common_subsequence(row, column - 1)
    elif table[row][column] == table[row - 1][column]:
        get_longest_common_subsequence(row - 1, column)
    else:
        diagonal_element = table[row - 1][column - 1]
        if table[row][column] == diagonal_element + 1:
            final_sequence.append(table[0][column])
            get_longest_common_subsequence(row - 1, column - 1)
s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
row = len(s2) + 2
column = len(s1) + 2
table = [['' for _ in range(column)] for _ in range(row)]
table[0][0] = "L"
table[0][1] = "P"
table[1][0] = "P"
for i, letter in enumerate(s1, start=2):
    table[0][i] = letter
    table[1][i] = 0
for i, letter in enumerate(s2, start=2):
    table[i][0] = letter
    table[i][1] = 0
for i in range(2, row):
    for j in range(2, column):
        if table[i][0] == table[0][j]:
            prev_diagonal_element = table[i - 1][j - 1]
            table[i][j] = prev_diagonal_element + 1
        else:
            table[i][j] = max(table[i][j - 1], table[i - 1][j])
print("LCS Matrix:")
print(np.matrix(table))
final_sequence = []
print("Row: ", row)
print("Column: ", column)
result = get_longest_common_subsequence(row - 1, column - 1)
lcs_string = "".join(str(x) for x in final_sequence)
print("Longest Common Subsequence (LCS):", lcs_string[::-1])