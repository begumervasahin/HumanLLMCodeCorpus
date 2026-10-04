import random
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b
def modular_multiplicative_inverse(e, lcm):
    g, x, y = egcd(e, lcm)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    return x % lcm
def key_gen(p, q):
    if p == q:
        raise Exception(f'{p} == {q}')
    if not is_prime(p) or not is_prime(q):
        raise Exception(f'{p} or {q} is not prime')
    n = p * q
    lcm = (p - 1) * (q - 1)
    e = random.randrange(1, lcm)
    while greatest_common_divisor(e, lcm) != 1:
        e = random.randrange(1, lcm)
    d = modular_multiplicative_inverse(e, lcm)
    return (e, n), (d, n)
def encrypt(public_key, plaintext):
    key, n = public_key
    return [(ord(char) ** key) % n for char in plaintext]
def decrypt(private_key, ciphertext):
    key, n = private_key
    return ''.join([chr((char ** key) % n) for char in ciphertext])
if __name__ == '__main__':
    p = int(input('Input a prime number: '))
    q = int(input('Input another different prime number: '))
    public_key, private_key = key_gen(p, q)
    print(f'Public key = {public_key}')
    print(f'Private key = {private_key}')
    message = input('Input a message: ')
    encrypted_message = encrypt(private_key, message)
    print(f'Encrypted message = {"".join(map(str, encrypted_message))}')
    decrypted_message = decrypt(public_key, encrypted_message)
    print(f'Decrypted message = {decrypted_message}')