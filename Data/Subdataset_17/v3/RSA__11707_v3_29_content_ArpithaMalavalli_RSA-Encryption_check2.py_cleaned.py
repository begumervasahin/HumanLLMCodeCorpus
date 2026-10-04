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
    return (y + C) % C
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def gen_public_key(n, phi):
    e_candidates = [i for i in range(2, phi) if gcd(i, phi) == 1]
    e = random.choice(e_candidates)
    return (n, e)
def gen_private_key(n, phi, e):
    k = 1
    while (k * phi + 1) % e != 0:
        k += 1
    d = (k * phi + 1)
    return (n, d)
def generate_primes(start, end):
    return [i for i in range(start, end) if isPrime(i)]
def main():
    primes = generate_primes(10, 100)
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
    encrypted_msg = exponentMod(msg, public_key[1], n)
    decrypted_msg = exponentMod(encrypted_msg, private_key[1], n)
    print("Encrypted message:", encrypted_msg)
    print("Decrypted message:", decrypted_msg)
    encoded_msg = 0
    for i, ch in enumerate(z[::-1]):
        encoded_msg += letters[ch] * (26 ** i)
    print("Encoded message:", encoded_msg)
    encrypted_msg = exponentMod(encoded_msg, public_key[1], n)
    decrypted_msg = exponentMod(encrypted_msg, private_key[1], n)
    decoded_msg = ""
    while decrypted_msg > 0:
        r = decrypted_msg % 26
        decoded_msg += numbers[r]
        decrypted_msg
    print("The decrypted message is:", decoded_msg[::-1])
if __name__ == "__main__":
    main()