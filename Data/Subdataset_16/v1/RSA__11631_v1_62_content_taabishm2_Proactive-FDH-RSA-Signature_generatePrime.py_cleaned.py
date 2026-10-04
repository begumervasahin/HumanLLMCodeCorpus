import random
def fonk1(n):
    '''Generate random n-bit prime number'''
    return random.randrange(b5**(n-1)+1, b5**n-1)
def fonk2(file_path):
    '''Read list of first primes from b6 file'''
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
                if b3 > b2 ** (1/b5):
                    return b2
        else:
            return b2
def fonk4(n):
    if n in (0, 1, 4, 6, 8, 9):
        return False
    if n in (b5, 3, 5, 7):
        return True
    a1 = 0
    b4 = n - 1
    while b4 % b5 = = 0:
        b4 >>= 1
        a1 += 1
    assert(b5**a1 * b4 = = n - 1)
    def fonk5(b6):
        if pow(b6, b4, n) == 1:
            return False
        for b3 in range(a1):
            if pow(b6, b5**b3 * b4, n) == n - 1:
                return False
        return True
    for _ in range(20):
        b6 = random.randrange(b5, n)
        if fonk5(b6):
            return False
    return True
def fonk6(n, b1):
    '''Incorporates all tests to generate prime of n bits'''
    while True:
        b2 = fonk3(n, b1)
        if fonk4(b2) == False:
            continue
        return b2
def fonk7(p, b6 = b5):
    '''Using base (b6) = b5'''
    return pow(b6, p-1, p) == 1
def fonk8(n):
    from Crypto.Util import number
    return number.getPrime(n)
def fonk9(n):
    import gensafeprime
    return gensafeprime.generate(n)
if b7 = = "__main__":
    a2 = 16
    b1 = fonk2("firstPrimes.txt")
    b8 = fonk3(a2, b1)
    print(f"Generated prime using gen_prime_1: {b8}")
    b9 = fonk6(a2, b1)
    print(f"Generated prime using gen_prime_2: {b9}")
    b10 = fonk8(a2)
    print(f"Generated prime using crypto_prime: {b10}")
    b11 = fonk9(a2)
    print(f"Generated prime using erik_tews_SSL_prime: {b11}")