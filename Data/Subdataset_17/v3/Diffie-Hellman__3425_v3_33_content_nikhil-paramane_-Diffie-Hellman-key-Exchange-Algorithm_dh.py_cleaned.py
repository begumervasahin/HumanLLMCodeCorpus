import random
def is_prime(num, iterations):
    if num <= 1:
        return False
    if iterations >= num:
        iterations = num - 1
    for _ in range(iterations):
        a = random.randint(1, num - 1)
        if pow(a, num - 1, num) != 1:
            return False
    return True
def generate_large_prime(bit_length):
    while True:
        candidate = random.randint(2**(bit_length-1), 2**bit_length - 1)
        if is_prime(candidate, 1000):
            return candidate
def generate_private_key(bit_length):
    return random.randint(2**(bit_length-1), 2**bit_length - 1)
def generate_public_key(base, private_key, modulus):
    return pow(base, private_key, modulus)
def generate_shared_key(public_key, private_key, modulus):
    return pow(public_key, private_key, modulus)
def main():
    bit_length = 10
    prime1 = generate_large_prime(bit_length)
    print("Prime 1:", prime1)
    prime2 = generate_large_prime(bit_length)
    print("Prime 2:", prime2)
    alice_private_key = generate_private_key(15)
    bob_private_key = generate_private_key(15)
    alice_public_key = generate_public_key(prime2, alice_private_key, prime1)
    bob_public_key = generate_public_key(prime2, bob_private_key, prime1)
    alice_shared_key = generate_shared_key(bob_public_key, alice_private_key, prime1)
    bob_shared_key = generate_shared_key(alice_public_key, bob_private_key, prime1)
    print("Alice's Shared Secret Key:", alice_shared_key)
    print("Bob's Shared Secret Key:", bob_shared_key)
if __name__ == "__main__":
    main()