import random
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b
def modular_multiplicative_inverse(e, lcm):
    g, x, y = egcd(e, lcm)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    return x % lcm
def key_gen(p, q):
    if p == q:
        raise ValueError('The two prime numbers must be different.')
    if not is_prime(p) or not is_prime(q):
        raise ValueError('Both numbers must be prime.')
    n = p * q
    lcm = (p - 1) * (q - 1)
    e = random.randrange(1, lcm)
    while greatest_common_divisor(e, lcm) != 1:
        e = random.randrange(1, lcm)
    d = modular_multiplicative_inverse(e, lcm)
    return (e, n), (d, n)
def encrypt(pk, plaintext):
    key, n = pk
    return [(ord(char) ** key) % n for char in plaintext]
def decrypt(pk, cipher):
    key, n = pk
    return ''.join([chr((char ** key) % n) for char in cipher])
if __name__ == '__main__':
    try:
        prime1 = int(input('Input a prime number: '))
        prime2 = int(input('Input another different prime number: '))
        public_key, private_key = key_gen(prime1, prime2)
        print(f'Public key = {public_key}')
        print(f'Private key = {private_key}')
        message = input('Input a message: ')
        encrypted_msg = encrypt(private_key, message)
        encrypted_msg_str = ' '.join(map(str, encrypted_msg))
        print(f'Encrypted message = {encrypted_msg_str}')
        decrypted_msg = decrypt(public_key, encrypted_msg)
        print(f'Decrypted message = {decrypted_msg}')
    except Exception as e:
        print(f'Error: {e}')