def multiply(mat1, mat2):
    MOD = 10**9 + 7
    return [
        (mat1[0] * mat2[0] + mat1[1] * mat2[2]) % MOD,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % MOD,
        (mat1[2] * mat2[0] + mat1[3] * mat2[2]) % MOD,
        (mat1[2] * mat2[1] + mat1[3] * mat2[3]) % MOD
    ]
def power(matrix, exponent):
    identity_matrix = [1, 0, 0, 1]
    base_matrix = matrix[:]
    while exponent > 0:
        if exponent % 2 == 1:
            identity_matrix = multiply(identity_matrix, base_matrix)
        base_matrix = multiply(base_matrix, base_matrix)
        exponent
    return identity_matrix
def fibonacci_mod(f0, f1, n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    transformation_matrix = [1, 1, 1, 0]
    powered_matrix = power(transformation_matrix, n - 1)
    MOD = 10**9 + 7
    return (powered_matrix[0] * f1 + powered_matrix[1] * f0) % MOD
def main():
    num_test_cases = int(input("Enter the number of test cases: "))
    for _ in range(num_test_cases):
        f0, f1, n = map(int, input("Enter f0, f1, n: ").strip().split())
        result = fibonacci_mod(f0, f1, n)
        print(result)
if __name__ == "__main__":
    main()