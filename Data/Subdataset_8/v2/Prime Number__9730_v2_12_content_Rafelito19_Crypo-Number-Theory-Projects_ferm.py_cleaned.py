def simple_modular_exponentiation(x, e, m):
    base = x
    exponent = e
    result = 1
    while exponent > 0:
        if exponent % 2 == 0:
            base = (base * base) % m
            exponent = exponent / 2
        else:
            result = (base * result) % m
            exponent = exponent - 1
    return result
def trial_division(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for divisor in range(3, int(num ** 0.5) + 2, 2):
        if num % divisor == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def chinese_remainder_test(num):
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
        if chinese_remainder_test(n) and not trial_division(n):
            print(f"{n} passed the Chinese remainder test but it is not prime")
        n += 1
if __name__ == "__main__":
    main()