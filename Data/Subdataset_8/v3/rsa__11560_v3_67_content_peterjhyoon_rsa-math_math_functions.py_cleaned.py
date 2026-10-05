
def is_prime(n):
    assert type(n) == int, "Input must be an integer"
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def divisor(n):
    return [i for i in range(1, n + 1) if n % i == 0]
def prime_factor(x):
    factors = []
    if is_prime(x):
        factors.append(x)
    for i in divisor(x):
        if i == 1:
            continue
        if is_prime(i):
            factors.append(i)
    return factors
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def relatively_prime(a, b):
    return gcd(a, b) == 1
def common_factor(a, b):
    return [elem for elem in divisor(a) if elem in divisor(b)]
print("Is 7 prime?", is_prime(7))
print("Divisors of 12:", divisor(12))
print("Prime factors of 24:", prime_factor(24))
print("GCD of 24 and 36:", gcd(24, 36))
print("Are 24 and 35 relatively prime?", relatively_prime(24, 35))
print("Common factors of 24 and 36:", common_factor(24, 36))
