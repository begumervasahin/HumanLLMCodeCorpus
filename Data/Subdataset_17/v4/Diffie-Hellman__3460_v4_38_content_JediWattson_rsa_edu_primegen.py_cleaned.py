import random
def miller_rabin_primality_test(n, k=100):
    if n in (2, 3):
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        d
        s += 1
    for _ in range(k):
        a = random.SystemRandom().randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def generate_random_prime(bits):
    assert bits >= 2, "Bit length must be at least 2."
    while True:
        prime_candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if miller_rabin_primality_test(prime_candidate):
            return prime_candidate
def main():
    bits = 16
    prime_number = generate_random_prime(bits)
    print(f"Random {bits}-bit prime number: {prime_number}")
if __name__ == '__main__':
    main()