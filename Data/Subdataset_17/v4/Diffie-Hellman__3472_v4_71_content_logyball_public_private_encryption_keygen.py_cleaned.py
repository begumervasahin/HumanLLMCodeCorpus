from random import randint, seed, getrandbits
from millerrabin import isPrime
GENERATOR = 2
def fake_32_bit_int(num):
    return num % 4294967295
def generate_prime(bit_length=31):
    while True:
        random_num = getrandbits(bit_length)
        if random_num % 12 != 5:
            continue
        prime_candidate = (2 * random_num) + 1
        if isPrime(prime_candidate) and prime_candidate > 2147483648:
            return prime_candidate
def generate_private_key(user_seed, prime):
    seed(user_seed)
    return randint(1, prime - 2)
def compute_e2(private_key, prime, generator=GENERATOR):
    return pow(generator, private_key, prime)
def generate_keys(user_seed=None):
    prime = generate_prime()
    private_key = generate_private_key(user_seed, prime)
    e2 = compute_e2(private_key, prime)
    return {
        'd': private_key,
        'p': prime,
        'g': GENERATOR,
        'e2': e2
    }
if __name__ == '__main__':
    keys = generate_keys(user_seed='user-defined-seed')
    print("Generated Keys:")
    print(f"Private Key (d): {keys['d']}")
    print(f"Prime (p): {keys['p']}")
    print(f"Generator (g): {keys['g']}")
    print(f"e2: {keys['e2']}")