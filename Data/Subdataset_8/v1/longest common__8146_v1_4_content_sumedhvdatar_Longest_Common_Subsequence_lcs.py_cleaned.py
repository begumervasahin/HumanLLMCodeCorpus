import numpy as np
def get_sequence(position_row, position_column):
    if position_row == 1 and position_column == 1:
        return final_sequence
    if table[position_row][position_column] == table[position_row][position_column - 1]:
        get_sequence(position_row, position_column - 1)
    elif table[position_row][position_column] == table[position_row - 1][position_column]:
        get_sequence(position_row - 1, position_column)
    else:
        diagonal_element = table[position_row - 1][position_column - 1]
        if table[position_row][position_column] == diagonal_element + 1:
            final_sequence.append(table[0][position_column])
            get_sequence(position_row - 1, position_column - 1)
s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
row = len(s2) + 2
column = len(s1) + 2
table = [[0 for _ in range(column)] for _ in range(row)]
table[0][0] = "L"
table[0][1] = "P"
for i, letter in enumerate(s1, start=2):
    table[0][i] = letter
    table[1][i] = 0
for i, letter in enumerate(s2, start=2):
    table[i][0] = letter
    table[i][1] = 0
for i in range(2, row):
    for j in range(2, column):
        if table[i][0] == table[0][j]:
            element_in_the_preceding_diagonal = table[i - 1][j - 1]
            table[i][j] = element_in_the_preceding_diagonal + 1
        else:
            table[i][j] = max(table[i][j - 1], table[i - 1][j])
final_sequence = []
get_sequence(row - 1, column - 1)
s3 = "".join(str(x) for x in final_sequence)
s3 = s3[::-1]
print("Longest Common Subsequence:", s3)
print("Dynamic Programming Table:")
print(np.matrix(table))