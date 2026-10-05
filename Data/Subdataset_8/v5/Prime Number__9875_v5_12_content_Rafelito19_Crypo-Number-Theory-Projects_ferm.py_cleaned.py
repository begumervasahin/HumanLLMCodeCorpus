def simple_modular_exponentiation(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent
        base = (base * base) % modulus
    return result
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 2, 2):
        if num % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def chinese_remainder_theorem_test(num):
    a = 2
    if gcd(a, num) != 1:
        return False
    if simple_modular_exponentiation(a, num - 1, num) != 1:
        return False
    return True
def main():
    bound = 100000
    n = 2
    while n < bound:
        passed_test = chinese_remainder_theorem_test(n)
        if passed_test and not is_prime(n):
            print(n, "passed the Chinese Remainder Theorem test but it is not prime")
        n += 1
if __name__ == "__main__":
    main()