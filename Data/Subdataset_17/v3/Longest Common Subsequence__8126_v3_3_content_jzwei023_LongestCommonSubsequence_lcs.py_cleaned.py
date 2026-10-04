def calculate_LCS(A, B):
    n = len(A)
    m = len(B)
    opt = [[0] * (m + 1) for _ in range(n + 1)]
    pi = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                opt[i][j] = opt[i - 1][j - 1] + 1
                pi[i][j] = 0
            elif opt[i][j - 1] >= opt[i - 1][j]:
                opt[i][j] = opt[i][j - 1]
                pi[i][j] = 1
            else:
                opt[i][j] = opt[i - 1][j]
                pi[i][j] = 2
    i, j = n, m
    LCS = []
    while i > 0 and j > 0:
        if pi[i][j] == 0:
            LCS.append(A[i - 1])
            i -= 1
            j -= 1
        elif pi[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return str(opt[n][m]), ''.join(reversed(LCS))
def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines[0].strip(), lines[1].strip()
def write_output(file_path, length, sequence):
    with open(file_path, "w") as file:
        file.write(length + "\n")
        file.write(sequence)
input_file = "input.txt"
output_file = "output.txt"
A, B = read_input(input_file)
length, sequence = calculate_LCS(A, B)
write_output(output_file, length, sequence)