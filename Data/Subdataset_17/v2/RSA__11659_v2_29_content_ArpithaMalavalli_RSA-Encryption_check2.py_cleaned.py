import random
letters = {chr(i + 97): i for i in range(26)}
numbers = {i: chr(i + 97) for i in range(26)}
def exponentMod(A, B, C):
    if A == 0:
        return 0
    if B == 0:
        return 1
    if B % 2 == 0:
        y = exponentMod(A, B
        y = (y * y) % C
    else:
        y = A % C
        y = (y * exponentMod(A, B - 1, C) % C) % C
    return int((y + C) % C)
def isPrime(n):
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
    print("k =", k)
    d = ((k * phi) + 1)
    return (n, d)
primes = [i for i in range(10, 100) if isPrime(i)]
p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)
print("p =", p)
print("q =", q)
n = p * q
phi = (p - 1) * (q - 1)
public_key = gen_public_key(n, phi)
print("Public key (n, e):", public_key)
private_key = gen_private_key(n, phi, public_key[1])
print("Private key (n, d):", private_key)
z = input("Enter what has to be encrypted: ")
msg = 1099
print("Original message:", msg)
c = exponentMod(msg, public_key[1], n)
decryp = exponentMod(c, private_key[1], n)
print("Encrypted message:", c)
print("Decrypted message:", decryp)
msg = 0
i = 0
for ch in z[::-1]:
    msg += letters[ch] * (26 ** i)
    i += 1
print("Encoded message:", msg)
c = exponentMod(msg, public_key[1], n)
decryp = exponentMod(c, private_key[1], n)
dmsg = ""
while decryp > 0:
    r = decryp % 26
    dmsg += numbers[r]
    decryp
print("The decrypted message is:", dmsg[::-1])