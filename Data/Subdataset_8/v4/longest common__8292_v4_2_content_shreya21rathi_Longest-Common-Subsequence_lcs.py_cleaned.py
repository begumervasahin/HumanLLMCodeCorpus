def longest_common_subsequence(a, b):
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
                        row.append('{0}U'.format(top[:-1]))
                    else:
                        row.append('{0}S'.format(left[:-1]))
                else:
                    diagonal = matrix[i - 1][j - 1]
                    row.append('{0}D'.format(str(int(diagonal[:-1]) + 1)))
                    if max_length < int(diagonal[:-1]) + 1:
                        max_length = int(diagonal[:-1]) + 1
        matrix.append(row)
    return matrix, max_length
def print_lcs(a, c, i, j):
    lcs_list = []
    x = c[i][j]
    if i == 0 or j == 0:
        print("".join(lcs_list[::-1]))
        return lcs_list
    if x[-1] == 'D':
        lcs_list.append(a[i - 1])
        print_lcs(a, c, i - 1, j - 1)
    elif x[-1] == 'U':
        print_lcs(a, c, i - 1, j)
    else:
        print_lcs(a, c, i, j - 1)
a = input("Enter 1st string:")
b = input("Enter 2nd string:")
matrix, length = longest_common_subsequence(a, b)
for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        print(matrix[i][j] + " ", end="")
    print()
print("Length of the longest common subsequence is:", length)
print_lcs(a, matrix, len(a), len(b))
max_length = max(len(a), len(b))
percent_difference = ((max_length - length) / max_length) * 100
print("Percent difference is: %.2f%%" % percent_difference)
if percent_difference > 7:
    print("Signature mismatch")
else:
    print("Signature matched")