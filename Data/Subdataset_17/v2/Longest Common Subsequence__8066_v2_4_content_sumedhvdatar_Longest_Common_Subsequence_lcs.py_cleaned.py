import numpy as np
def get_sequence(position_row, position_column):
    if position_row == 1 or position_column == 1:
        return
    if table[position_row][position_column] == table[position_row][position_column-1]:
        get_sequence(position_row, position_column-1)
    elif table[position_row][position_column] == table[position_row-1][position_column]:
        get_sequence(position_row-1, position_column)
    else:
        diagonal_element = table[position_row-1][position_column-1]
        if table[position_row][position_column] == diagonal_element + 1:
            final_sequence.append(table[0][position_column])
            get_sequence(position_row-1, position_column-1)
s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
column = len(s1) + 2
row = len(s2) + 2
table = [[0 for x in range(column)] for y in range(row)]
table[0][2:] = list(s1)
table[1][2:] = [0] * len(s1)
for i, letter in enumerate(s2, start=2):
    table[i][0] = letter
    table[i][1] = 0
for i in range(2, row):
    for j in range(2, column):
        if table[i][0] == table[0][j]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i][j-1], table[i-1][j])
print("Printing the matrix:")
print(np.matrix(table))
final_sequence = []
print("We are sending row " + str(row))
print("We are sending column " + str(column))
get_sequence(row-1, column-1)
s3 = "".join(str(x) for x in final_sequence)
print(s3[::-1])
