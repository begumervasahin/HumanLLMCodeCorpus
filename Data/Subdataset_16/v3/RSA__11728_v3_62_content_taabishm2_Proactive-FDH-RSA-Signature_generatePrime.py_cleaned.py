import random
def fonk1(n):
    return random.randrange(b5**(n-1) + 1, b5**n - 1)
def fonk2(file_path):
    try:
        with open(file_path, 'r') as file:
            b1 = list(map(int, file.read().split()))
        return b1
    except Exception as e:
        raise Exception("Couldn't read first primes from file") from e
def fonk3(b3, b1):
    for b2 in b1:
        if b3 % b2 = = 0:
            return False
        if b3 < b2 ** b5:
            return True
    return True
def fonk4(n, b1):
    while True:
        b3 = fonk1(n)
        if fonk3(b3, b1):
            return b3
def fonk5(n):
    if n in {0, 1, 4, 6, 8, 9}:
        return False
    if n in {b5, 3, 5, 7}:
        return True
    s, b4 = 0, n - 1
    while b4 % b5 = = 0:
        b4 >>= 1
        s += 1
    assert b5**s * b4 = = n - 1
    def fonk6(b6):
        if pow(b6, b4, n) == 1:
            return False
        for i in range(s):
            if pow(b6, b5**i * b4, n) == n - 1:
                return False
        return True
    for _ in range(20):
        b6 = random.randrange(b5, n)
        if fonk6(b6):
            return False
    return True
def fonk7(n, b1):
    while True:
        b3 = fonk4(n, b1)
        if fonk5(b3):
            return b3
def fonk8(p, b6 = b5):
    return pow(b6, p-1, p) == 1
def fonk9(n):
    from Crypto.Util import number
    return number.getPrime(n)
def fonk10(n):
    import gensafeprime
    return gensafeprime.generate(n)
if b7 = = "__main__":
    a1 = 16
    b1 = fonk2("firstPrimes.txt")
    b8 = fonk4(a1, b1)
    print(f"Generated b2 using gen_prime_1: {b8}")
    b9 = fonk7(a1, b1)
    print(f"Generated b2 using gen_prime_2: {b9}")
    b10 = fonk9(a1)
    print(f"Generated b2 using crypto_prime: {b10}")
    b11 = fonk10(a1)
    print(f"Generated b2 using erik_tews_SSL_prime: {b11}")