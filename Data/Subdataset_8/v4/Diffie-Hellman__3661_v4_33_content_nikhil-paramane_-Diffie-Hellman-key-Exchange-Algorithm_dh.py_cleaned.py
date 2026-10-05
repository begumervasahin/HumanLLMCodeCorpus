from random import randint
def is_prime(num, count):
    if num == 1:
        return False
    if count >= num:
        count = num - 1
    for _ in range(count):
        a = randint(1, num - 1)
        if pow(a, num - 1, num) != 1:
            return False
    return True
def generate_big_prime(n_bits):
    found_prime = False
    while not found_prime:
        p = randint(2 ** (n_bits - 1), 2 ** n_bits)
        if is_prime(p, 1000):
            return p
prime1 = generate_big_prime(2 ** 10)
prime2 = generate_big_prime(2 ** 10)
alice_private_key = randint(2 ** 10, 2 ** 15)
bob_private_key = randint(2 ** 10, 2 ** 15)
a = pow(prime2, alice_private_key, prime1)
b = pow(prime2, bob_private_key, prime1)
alice_secret_key = pow(b, alice_private_key, prime1)
bob_secret_key = pow(a, bob_private_key, prime1)
print("Prime 1:", prime1)
print("Prime 2:", prime2)
print("Alice's Secret Key:", alice_secret_key)
print("Bob's Secret Key:", bob_secret_key)