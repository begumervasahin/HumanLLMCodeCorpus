import random
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def egcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        (q, r) = divmod(a, b)
        (s, t) = egcd(b, r)
        return (t, s - q * t)
def multinv(a, n):
    (x, y) = egcd(a, n)
    return x % n
def rande(phi):
    new_e = random.randint(2, phi)
    while gcd(new_e, phi) != 1:
        new_e = random.randint(2, phi)
    return new_e
def genkey(p, q):
    if (p, q) == (2, 3) or (p, q) == (3, 2):
        return "Choose a different value for 'p' and 'q'"
    n = p * q
    phi = (p - 1) * (q - 1)
    e = rande(phi)
    d = multinv(e, phi)
    return ((e, d), n)
def encrypt(bstr, p, q):
    (keys, mod) = genkey(p, q)
    print("Private key:", keys[0])
    print("Public key:", keys[1])
    print("Public modulus:", mod, '\n')
    return [hex(pow(b, keys[0], mod)).split('x')[1] for b in bstr]
def decrypt(arr, exp, mod):
    return bytes([pow(int(b, 16), exp, mod) for b in arr])
plaintext = b'Hello, World!'
p = 61
q = 53
encrypted = encrypt(plaintext, p, q)
print("Encrypted:", encrypted)
decrypted = decrypt(encrypted, 17, p * q)
print("Decrypted:", decrypted.decode())