def multiply_matrices(matrix1, matrix2):
    modulus = (10 ** 9) + 7
    a, b, c, d = matrix1
    e, f, g, h = matrix2
    result = [
        (a * e + b * g) % modulus,
        (a * f + b * h) % modulus,
        (c * e + d * g) % modulus,
        (c * f + d * h) % modulus
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