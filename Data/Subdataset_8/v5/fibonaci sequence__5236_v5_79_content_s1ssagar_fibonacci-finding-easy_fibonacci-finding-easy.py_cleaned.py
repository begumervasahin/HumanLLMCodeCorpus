MODULUS = (10 ** 9) + 7
def multiply_matrices(mat1, mat2):
    result = [
        (mat1[0] * mat2[0] + mat1[1] * mat2[2]) % MODULUS,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % MODULUS,
        (mat1[2] * mat2[0] + mat1[3] * mat2[2]) % MODULUS,
        (mat1[2] * mat2[1] + mat1[3] * mat2[3]) % MODULUS
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
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        f0, f1, n = map(int, input("Enter f0, f1, and n: ").split())
        initial_matrix = [1, 1, 1, 0]
        power_matrix = matrix_power(initial_matrix, n - 1)
        result = (power_matrix[2] * f1 + power_matrix[3] * f0) % MODULUS
        print("Result:", result)
if __name__ == "__main__":
    main()