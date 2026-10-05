from random import randint
def is_prime(num, count):
    if num == 1:
        return False
    if count >= num:
        count = num - 1
    for x in range(count):
        a = randint(1, num - 1)
        if pow(a, num-1, num) != 1:
            return False
    return True
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
def generate_keys(n_bits):
    prime1 = generate_big_prime(n_bits)
    prime2 = generate_big_prime(n_bits)
    alice_private_key = randint(2**10, 2**15)
    bob_private_key = randint(2**10, 2**15)
    a = pow(prime2, alice_private_key, prime1)
    b = pow(prime2, bob_private_key, prime1)
    alice_key = pow(b, alice_private_key, prime1)
    bob_key = pow(a, bob_private_key, prime1)
    return prime1, prime2, alice_key, bob_key
if __name__ == "__main__":
    prime1, prime2, alice_key, bob_key = generate_keys(2**10)
    print("Prime 1:", prime1)
    print("Prime 2:", prime2)
    print("Alice Secret key:", alice_key)
    print("Bob Secret key:", bob_key)