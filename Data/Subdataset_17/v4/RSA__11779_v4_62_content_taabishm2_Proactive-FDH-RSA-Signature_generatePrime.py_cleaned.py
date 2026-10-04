import random
import fileOp
def random_n(n):
    return random.randrange(2**(n-1) + 1, 2**n - 1)
def gen_prime_1(n):
    try:
        first_primes_list = fileOp.read_list("FfirstPrimes")
    except Exception as e:
        raise Exception("Couldn't read FfirstPrimes from file") from e
    while True:
        sample = random_n(n)
        for prime in first_primes_list:
            if sample % prime == 0:
                break
            if sample < (first_primes_list[-1]) ** 2 and prime > sample ** 0.5:
                return sample
        else:
            return sample
def miller_rabin_test(n):
    if n in {0, 1, 4, 6, 8, 9}:
        return False
    if n in {2, 3, 5, 7}:
        return True
    s, d = 0, n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True
    for _ in range(20):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
    return True
def gen_prime_2(n):
    while True:
        sample = gen_prime_1(n)
        if miller_rabin_test(sample):
            return sample
def fermat_test(p, a=2):
    return pow(a, p - 1, p) == 1
def crypto_prime(n):
    return number.getPrime(n)
def erik_tews_SSL_prime(n):
    return gensafeprime.generate(n)