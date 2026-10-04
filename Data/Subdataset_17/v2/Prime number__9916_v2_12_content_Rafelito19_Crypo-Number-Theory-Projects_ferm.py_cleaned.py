def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result
def is_prime_trial_division(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def chinese_primality_test(num):
    base = 2
    if gcd(base, num) != 1:
        return False
    if modular_exponentiation(base, num - 1, num) != 1:
        return False
    return True
def main():
    bound = 100000
    for n in range(2, bound):
        if chinese_primality_test(n) and not is_prime_trial_division(n):
            print(f"{n} passed the Chinese test but it is not prime")
if __name__ == "__main__":
    main()