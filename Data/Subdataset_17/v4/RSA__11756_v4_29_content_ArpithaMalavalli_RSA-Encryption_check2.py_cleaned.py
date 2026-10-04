import random
def exponent_mod(A, B, C):
    if A == 0:
        return 0
    if B == 0:
        return 1
    if B % 2 == 0:
        y = exponent_mod(A, B
        y = (y * y) % C
    else:
        y = A % C
        y = (y * exponent_mod(A, B - 1, C) % C) % C
    return (int)((y + C) % C)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def gen_public_key(n, phi):
    list_random_e = [i for i in range(1, phi) if (n % i != 0 and gcd(i, phi) == 1)]
    e = random.choice(list_random_e)
    return (n, e)
def gen_private_key(n, phi, e):
    list_random_k = [i for i in range(1, phi) if (((i * phi) + 1) % e == 0)]
    k = random.choice(list_random_k)
    d = ((k * phi) + 1)
    return (n, d)
primes = [i for i in range(10, 100) if is_prime(i)]
p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)
n = p * q
phi = (p - 1) * (q - 1)
public_key = gen_public_key(n, phi)
private_key = gen_private_key(n, phi, public_key[1])
print("Public key (n, e):", public_key)
print("Private key (n, d):", private_key)
msg = 1099
print("Original message:", msg)
encrypted_msg = exponent_mod(msg, public_key[1], n)
decrypted_msg = exponent_mod(encrypted_msg, private_key[1], n)
print("Encrypted message:", encrypted_msg)
print("Decrypted message:", decrypted_msg)