
def calculate_LCS(A, B):
    len_A = len(A)
    len_B = len(B)
    lcs_length_matrix = [[0 for _ in range(len_B + 1)] for _ in range(len_A + 1)]
    parent_matrix = [[0 for _ in range(len_B + 1)] for _ in range(len_A + 1)]
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if A[i - 1] == B[j - 1]:
                lcs_length_matrix[i][j] = lcs_length_matrix[i - 1][j - 1] + 1
                parent_matrix[i][j] = 0
            elif lcs_length_matrix[i][j - 1] >= lcs_length_matrix[i - 1][j]:
                lcs_length_matrix[i][j] = lcs_length_matrix[i][j - 1]
                parent_matrix[i][j] = 1
            else:
                lcs_length_matrix[i][j] = lcs_length_matrix[i - 1][j]
                parent_matrix[i][j] = 2
    i, j = len_A, len_B
    lcs = ''
    while i > 0 and j > 0:
        if parent_matrix[i][j] == 0:
            lcs = A[i - 1] + lcs
            i -= 1
            j -= 1
        elif parent_matrix[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return str(lcs_length_matrix[len_A][len_B]), lcs
input_file_path = "input.txt"
output_file_path = "output.txt"
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()
    first_string = lines[0].strip()
    second_string = lines[1].strip()
lcs_length, lcs_sequence = calculate_LCS(first_string, second_string)
with open(output_file_path, "w") as output_file:
    output_file.write(lcs_length + "\n")
    output_file.write(lcs_sequence)
