def multiply_matrices(mat1, mat2):
    mod_val = (10**9) + 7
    return [
        (mat1[0] * mat2[0] + mat1[1] * mat2[2]) % mod_val,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % mod_val,
        (mat1[2] * mat2[0] + mat1[3] * mat2[2]) % mod_val,
        (mat1[2] * mat2[1] + mat1[3] * mat2[3]) % mod_val
    ]
def matrix_power(mat, n):
    identity_matrix = [1, 1, 1, 0]
    while n:
        if n & 1:
            identity_matrix = multiply_matrices(identity_matrix, mat)
        mat = multiply_matrices(mat, mat)
        n >>= 1
    return identity_matrix
def main():
    tc = int(input("Enter the number of test cases: "))
    for _ in range(tc):
        f0, f1, n = map(int, input("Enter f0, f1, and n: ").split())
        initial_matrix = [1, 1, 1, 0]
        power_matrix = matrix_power(initial_matrix, n - 1)
        result = (power_matrix[2] * f1 + power_matrix[3] * f0) % ((10**9) + 7)
        print("Result:", result)
if __name__ == "__main__":
    main()