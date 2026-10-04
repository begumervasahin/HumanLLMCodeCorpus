def lcs(a, b):
    matrix = []
    max_length = 0
    for i in range(len(a) + 1):
        row = []
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                row.append('0H')
            else:
                if a[i - 1] != b[j - 1]:
                    top = matrix[i - 1][j]
                    left = row[j - 1]
                    if int(top[:-1]) >= int(left[:-1]):
                        row.append(f'{top[:-1]}U')
                    else:
                        row.append(f'{left[:-1]}S')
                else:
                    diagonal = matrix[i - 1][j - 1]
                    new_value = int(diagonal[:-1]) + 1
                    row.append(f'{new_value}D')
                    if max_length < new_value:
                        max_length = new_value
        matrix.append(row)
    return matrix, max_length
def print_lcs(a, c, i, j):
    lcs_sequence = []
    while i > 0 and j > 0:
        cell = c[i][j]
        if cell[-1] == 'D':
            lcs_sequence.append(a[i - 1])
            i -= 1
            j -= 1
        elif cell[-1] == 'U':
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs_sequence))
a = input("Enter 1st string: ")
b = input("Enter 2nd string: ")
matrix, length = lcs(a, b)
for row in matrix:
    print(" ".join(row))
print(f"Length of longest common subsequence is: {length}")
lcs_sequence = print_lcs(a, matrix, len(a), len(b))
print(f"Longest common subsequence is: {lcs_sequence}")
max_len = max(len(a), len(b))
percent_diff = ((max_len - length) / max_len) * 100
print(f"Percent difference is: {percent_diff:.2f}%")
if percent_diff > 7:
    print("Signature mismatch")
else:
    print("Signature matched")