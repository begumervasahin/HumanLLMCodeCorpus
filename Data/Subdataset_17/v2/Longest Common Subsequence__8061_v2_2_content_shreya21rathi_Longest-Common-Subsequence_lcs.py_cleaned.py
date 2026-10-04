def lcs(a, b):
    matrix = []
    max_len = 0
    for i in range(len(a) + 1):
        row = []
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                row.append('0H')
            else:
                if a[i - 1] != b[j - 1]:
                    up = matrix[i - 1][j]
                    left = row[j - 1]
                    if int(up[:-1]) >= int(left[:-1]):
                        row.append(f'{up[:-1]}U')
                    else:
                        row.append(f'{left[:-1]}S')
                else:
                    diagonal = matrix[i - 1][j - 1]
                    new_len = int(diagonal[:-1]) + 1
                    row.append(f'{new_len}D')
                    if max_len < new_len:
                        max_len = new_len
        matrix.append(row)
    return matrix, max_len
def construct_lcs(a, matrix, i, j):
    lcs_list = []
    while i > 0 and j > 0:
        cell = matrix[i][j]
        if cell[-1] == 'D':
            lcs_list.append(a[i - 1])
            i -= 1
            j -= 1
        elif cell[-1] == 'U':
            i -= 1
        else:
            j -= 1
    return "".join(lcs_list[::-1])
def main():
    a = input("Enter 1st string: ")
    b = input("Enter 2nd string: ")
    matrix, length = lcs(a, b)
    for row in matrix:
        for cell in row:
            print(cell + " ", end="")
        print()
    print(f"Length of longest common subsequence is: {length}")
    lcs_string = construct_lcs(a, matrix, len(a), len(b))
    print(f"Longest Common Subsequence is: {lcs_string}")
    max_len = max(len(a), len(b))
    percent_diff = ((max_len - length) / max_len) * 100
    print(f"Percent difference is: {percent_diff:.2f} %")
    if percent_diff > 7:
        print("Signature mismatch")
    else:
        print("Signature matched")
if __name__ == "__main__":
    main()