import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def egcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        q, r = divmod(a, b)
        s, t = egcd(b, r)
        return (t, s - q * t)
def multinv(a, n):
    x, y = egcd(a, n)
    return x % n if gcd(a, n) == 1 else None
def generate_coprime(phi):
    while True:
        e = random.randint(2, phi)
        if gcd(e, phi) == 1:
            return e
def generate_keypair(p, q):
    if (p, q) == (2, 3) or (p, q) == (3, 2):
        return "Choose a different value for 'p' and 'q'"
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_coprime(phi)
    d = multinv(e, phi)
    return {'public_key': (e, n), 'private_key': (d, n)}
def encrypt(plaintext, public_key):
    e, mod = public_key
    ciphertext = [hex(pow(byte, e, mod)).split('x')[1] for byte in plaintext]
    return ciphertext, mod
def decrypt(ciphertext, private_key):
    d, mod = private_key
    decrypted = bytes([pow(int(byte, 16), d, mod) for byte in ciphertext])
    return decrypted.decode()
plaintext = b'Hello, World!'
p = 61
q = 53
keypair = generate_keypair(p, q)
print("Public key:", keypair['public_key'])
print("Private key:", keypair['private_key'])
encrypted, modulus = encrypt(plaintext, keypair['public_key'])
print("\nEncrypted:", encrypted)
decrypted = decrypt(encrypted, keypair['private_key'])
print("Decrypted:", decrypted)