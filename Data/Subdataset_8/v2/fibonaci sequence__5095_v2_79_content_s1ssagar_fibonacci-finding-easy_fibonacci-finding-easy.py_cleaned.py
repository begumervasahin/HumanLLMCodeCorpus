def multiply_matrices(matrix1, matrix2):
    modulus = (10 ** 9) + 7
    result = [
        (matrix1[0] * matrix2[0] + matrix1[1] * matrix2[2]) % modulus,
        (matrix1[0] * matrix2[1] + matrix1[1] * matrix2[3]) % modulus,
        (matrix1[2] * matrix2[0] + matrix1[3] * matrix2[2]) % modulus,
        (matrix1[2] * matrix2[1] + matrix1[3] * matrix2[3]) % modulus
    ]
    return result
def matrix_power(matrix, exponent):
    identity_matrix = [1, 1, 1, 0]
    while exponent:
        if exponent & 1:
            identity_matrix = multiply_matrices(identity_matrix, matrix)
        matrix = multiply_matrices(matrix, matrix)
        exponent >>= 1
    return identity_matrix
def main():
    num_test_cases = int(input("Enter the number of test cases: "))
    for _ in range(num_test_cases):
        f0, f1, n = map(int, input("Enter f0, f1, and n: ").split())
        initial_matrix = [1, 1, 1, 0]
        power_matrix = matrix_power(initial_matrix, n - 1)
        result = (power_matrix[2] * f1 + power_matrix[3] * f0) % ((10 ** 9) + 7)
        print("Result:", result)
if __name__ == "__main__":
    main()