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
def fonk3(n, b1):
    while True:
        b2 = fonk1(n)
        for b3 in b1:
            if b2 % b3 = = 0:
                break
            if b2 < (b1[-1]) ** b5:
                if b3 > b2 ** 0.5:
                    return b2
        else:
            return b2
def fonk4(n):
    if n in {0, 1, 4, 6, 8, 9}:
        return False
    if n in {b5, 3, 5, 7}:
        return True
    s, b4 = 0, n - 1
    while b4 % b5 = = 0:
        b4 >>= 1
        s += 1
    assert b5**s * b4 = = n - 1
    def fonk5(b6):
        if pow(b6, b4, n) == 1:
            return False
        for i in range(s):
            if pow(b6, b5**i * b4, n) == n - 1:
                return False
        return True
    for _ in range(20):
        b6 = random.randrange(b5, n)
        if fonk5(b6):
            return False
    return True
def fonk6(n, b1):
    while True:
        b2 = fonk3(n, b1)
        if not fonk4(b2):
            continue
        return b2
def fonk7(p, b6 = b5):
    return pow(b6, p-1, p) == 1
def fonk8(n):
    from Crypto.Util import number
    return number.getPrime(n)
def fonk9(n):
    import gensafeprime
    return gensafeprime.generate(n)
if b7 = = "__main__":
    a1 = 16
    b1 = fonk2("firstPrimes.txt")
    b8 = fonk3(a1, b1)
    print(f"Generated b3 using gen_prime_1: {b8}")
    b9 = fonk6(a1, b1)
    print(f"Generated b3 using gen_prime_2: {b9}")
    b10 = fonk8(a1)
    print(f"Generated b3 using crypto_prime: {b10}")
    b11 = fonk9(a1)
    print(f"Generated b3 using erik_tews_SSL_prime: {b11}")