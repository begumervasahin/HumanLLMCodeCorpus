import random
def exponent_mod(base, exp, mod):
    if base == 0:
        return 0
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half_exp = exponent_mod(base, exp
        return (half_exp * half_exp) % mod
    else:
        return (base * exponent_mod(base, exp - 1, mod)) % mod
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def generate_public_key(n, phi):
    candidates = [e for e in range(2, phi) if gcd(e, phi) == 1]
    e = random.choice(candidates)
    return n, e
def generate_private_key(n, phi, e):
    k = 1
    while (k * phi + 1) % e != 0:
        k += 1
    d = (k * phi + 1)
    return n, d
primes = [i for i in range(10, 100) if is_prime(i)]
p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)
n = p * q
phi = (p - 1) * (q - 1)
public_key = generate_public_key(n, phi)
private_key = generate_private_key(n, phi, public_key[1])
print("Public key (n, e):", public_key)
print("Private key (n, d):", private_key)
original_message = 1099
print("Original message:", original_message)
encrypted_message = exponent_mod(original_message, public_key[1], n)
decrypted_message = exponent_mod(encrypted_message, private_key[1], n)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)