import time
def montgomery_multiplication(a, b, n):
    reverse = calculate_reverse(n)
    result = (a * b * reverse) % n
    return result
def calculate_reverse(n):
    reverse = 1
    r = pow(2, n - 1)
    for i in range(1, n + 1):
        if (reverse * r) % n == 1:
            break
        else:
            reverse += 1
    return reverse
def modular_exponentiation(base, exponent, n):
    i = exponent - 1
    x = montgomery_multiplication(base, 1, n)
    while i > 0:
        x = montgomery_multiplication(x, 1, n)
        i -= 1
    return x
def main():
    print(modular_exponentiation(2, 6, 10000000))
if __name__ == "__main__":
    main()