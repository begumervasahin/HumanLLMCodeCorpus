import random
def generate_prime(bits=1024):
    while True:
        candidate_prime = random.getrandbits(bits)
        if is_prime(candidate_prime):
            return candidate_prime
def is_prime(n, rounds=50):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    t = n - 1
    s = 0
    while t % 2 == 0:
        s += 1
        t
    for _ in range(rounds):
        a = random.randint(1, n - 1)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        if x != n - 1:
            return False
    return True
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
def find_modular_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
if __name__ == "__main__":
    prime_number = generate_prime()
    print("Generated Prime Number:", prime_number)
    print("Is Prime?", is_prime(prime_number))
    num_a = random.randint(1, 1000)
    num_m = random.randint(1, 1000)
    print("Finding modular inverse of", num_a, "mod", num_m)
    modular_inverse = find_modular_inverse(num_a, num_m)
    print("Modular Inverse:", modular_inverse)