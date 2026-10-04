import random
def random_n(n):
    return random.randrange(2**(n-1) + 1, 2**n - 1)
def read_list(file_path):
    try:
        with open(file_path, 'r') as file:
            first_primes_list = list(map(int, file.read().split()))
        return first_primes_list
    except Exception as e:
        raise Exception("Couldn't read first primes from file") from e
def gen_prime_1(n, first_primes_list):
    while True:
        sample = random_n(n)
        for prime in first_primes_list:
            if sample % prime == 0:
                break
            if sample < (first_primes_list[-1]) ** 2:
                if prime > sample ** 0.5:
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
    assert 2**s * d == n - 1
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
def gen_prime_2(n, first_primes_list):
    while True:
        sample = gen_prime_1(n, first_primes_list)
        if not miller_rabin_test(sample):
            continue
        return sample
def fermat_test(p, a=2):
    return pow(a, p-1, p) == 1
def crypto_prime(n):
    from Crypto.Util import number
    return number.getPrime(n)
def erik_tews_SSL_prime(n):
    import gensafeprime
    return gensafeprime.generate(n)
if __name__ == "__main__":
    n_bits = 16
    first_primes_list = read_list("firstPrimes.txt")
    prime1 = gen_prime_1(n_bits, first_primes_list)
    print(f"Generated prime using gen_prime_1: {prime1}")
    prime2 = gen_prime_2(n_bits, first_primes_list)
    print(f"Generated prime using gen_prime_2: {prime2}")
    prime_crypto = crypto_prime(n_bits)
    print(f"Generated prime using crypto_prime: {prime_crypto}")
    prime_erik_tews = erik_tews_SSL_prime(n_bits)
    print(f"Generated prime using erik_tews_SSL_prime: {prime_erik_tews}")