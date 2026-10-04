import random
def is_prime(num, count):
    if num == 1:
        return False
    if count >= num:
        count = num - 1
    for _ in range(count):
        a = random.randint(1, num - 1)
        if pow(a, num - 1, num) != 1:
            return False
    return True
def generate_big_prime(n):
    while True:
        p = random.randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
def main():
    prime1 = generate_big_prime(10)
    print("Prime 1:", prime1)
    prime2 = generate_big_prime(10)
    print("Prime 2:", prime2)
    alice_private_key = random.randint(2**10, 2**15)
    bob_private_key = random.randint(2**10, 2**15)
    alice_public_key = pow(prime2, alice_private_key, prime1)
    bob_public_key = pow(prime2, bob_private_key, prime1)
    alice_secret_key = pow(bob_public_key, alice_private_key, prime1)
    bob_secret_key = pow(alice_public_key, bob_private_key, prime1)
    print("Alice Secret Key:", alice_secret_key)
    print("Bob Secret Key:", bob_secret_key)
if __name__ == "__main__":
    main()