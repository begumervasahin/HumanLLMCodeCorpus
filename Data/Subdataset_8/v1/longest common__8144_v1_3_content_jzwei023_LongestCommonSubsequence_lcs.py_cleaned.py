def calculate_LCS(A, B):
    n = len(A)
    m = len(B)
    opt = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    pi = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
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
    lcs = ''
    while i > 0 and j > 0:
        if pi[i][j] == 0:
            lcs = A[i - 1] + lcs
            i -= 1
            j -= 1
        elif pi[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return str(opt[n][m]), lcs
input_file = "input.txt"
output_file = "output.txt"
with open(input_file, "r") as file_in:
    lines = file_in.readlines()
    A = lines[0].strip()
    B = lines[1].strip()
length, sequence = calculate_LCS(A, B)
with open(output_file, "w") as file_out:
    file_out.write(length + "\n")
    file_out.write(sequence)