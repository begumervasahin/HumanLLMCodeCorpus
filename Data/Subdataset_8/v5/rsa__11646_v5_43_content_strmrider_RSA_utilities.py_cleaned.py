import random
def get_odd_number(a, b):
    rand = random.randrange(a, b)
    if rand % 2 == 0:
        rand += 1
    return rand
def is_composite(n, a, r, s):
    res = pow(a, r, n)
    if res == 1 or res == n - 1:
        return False
    for _ in range(int(s)):
        res = pow(res, 2, n)
        if res == n - 1:
            return False
    return True
def is_prime(n):
    r = n - 1
    s = 0
    while r % 2 == 0:
        r
        s += 1
    limit = (n - 1)
    for _ in range(limit):
        a = random.randint(2, 100)
        if is_composite(n, a, r, s):
            return False
    return True
def generate_prime_number(a, b):
    while True:
        number = get_odd_number(a, b)
        if is_prime(number):
            return number
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def multiplicative_inverse(e, phi):
    x, y = 1, 0
    temp_phi = phi
    while e > 1:
        quotient = e
        e, temp_phi = temp_phi, e % temp_phi
        x, y = y, x - quotient * y
    return x % phi
