def initialize_matrix(a, b):
    matrix = [['0H' for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    return matrix
def longest_common_subsequence(a, b):
    matrix = initialize_matrix(a, b)
    max_length = 0
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] != b[j-1]:
                top = matrix[i-1][j]
                left = matrix[i][j-1]
                if int(top[:-1]) >= int(left[:-1]):
                    matrix[i][j] = '{0}U'.format(top[:-1])
                else:
                    matrix[i][j] = '{0}S'.format(left[:-1])
            else:
                diagonal = matrix[i - 1][j - 1]
                matrix[i][j] = '{0}D'.format(str(int(diagonal[:-1]) + 1))
                if max_length < int(diagonal[:-1]) + 1:
                    max_length = int(diagonal[:-1]) + 1
    return matrix, max_length
def get_lcs_sequence(a, matrix):
    lcs_list = []
    i, j = len(a), len(matrix[0]) - 1
    while i > 0 and j > 0:
        cell = matrix[i][j]
        if cell[-1] == 'D':
            lcs_list.append(a[i-1])
            i -= 1
            j -= 1
        elif cell[-1] == 'U':
            i -= 1
        else:
            j -= 1
    return ''.join(lcs_list[::-1])
def calculate_percent_difference(a, b, length):
    max_length = max(len(a), len(b))
    percent_difference = ((max_length - length) / max_length) * 100
    return percent_difference
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
def main():
    a = input("Enter 1st string:")
    b = input("Enter 2nd string:")
    matrix, length = longest_common_subsequence(a, b)
    print_matrix(matrix)
    print("Length of the longest common subsequence is:", length)
    lcs_sequence = get_lcs_sequence(a, matrix)
    print("Longest common subsequence is:", lcs_sequence)
    percent_difference = calculate_percent_difference(a, b, length)
    print("Percent difference is: %.2f%%" % percent_difference)
    if percent_difference > 7:
        print("Signature mismatch")
    else:
        print("Signature matched")
if __name__ == "__main__":
    main()