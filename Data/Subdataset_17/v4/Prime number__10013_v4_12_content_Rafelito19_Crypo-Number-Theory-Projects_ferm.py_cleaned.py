def simple_modular_exponentiation(x, e, m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y
def is_prime_trial_division(num):
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
def chinese_test(num):
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
        passed_test = chinese_test(n)
        if passed_test and not is_prime_trial_division(n):
            print(f"{n} passed the Chinese test but it is not prime")
        n += 1
if __name__ == "__main__":
    main()