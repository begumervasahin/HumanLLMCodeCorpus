MOD = 10**9 + 7
def multiply(mat1, mat2):
    return [
        (mat1[0] * mat2[0] + mat1[1] * mat2[2]) % MOD,
        (mat1[0] * mat2[1] + mat1[1] * mat2[3]) % MOD,
        (mat1[2] * mat2[0] + mat1[3] * mat2[2]) % MOD,
        (mat1[2] * mat2[1] + mat1[3] * mat2[3]) % MOD
    ]
def power(matrix, exponent):
    result = [1, 0, 0, 1]
    base = matrix[:]
    while exponent > 0:
        if exponent % 2 == 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent
    return result
def fibonacci_mod(f0, f1, n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    transformation_matrix = [1, 1, 1, 0]
    result_matrix = power(transformation_matrix, n - 1)
    return (result_matrix[0] * f1 + result_matrix[1] * f0) % MOD
def main():
    tc = int(input("Enter the number of test cases: "))
    for _ in range(tc):
        f0, f1, n = map(int, input("Enter f0, f1, n: ").strip().split())
        result = fibonacci_mod(f0, f1, n)
        print(result)
if __name__ == "__main__":
    main()