import random
from Crypto.Util import number
def generate_prime(bits=9):
    return number.getPrime(bits, None)
def generate_random_base(min_value=5, max_value=200):
    return random.randint(min_value, max_value)
def generate_private_key(prime):
    return random.randint(0, prime - 1)
def compute_public_key(base, private_key, prime):
    return pow(base, private_key, prime)
def compute_shared_secret(public_key, private_key, prime):
    return pow(public_key, private_key, prime)
def brute_force_private_key(public_key, base, prime):
    for possible_private_key in range(prime):
        if compute_public_key(base, possible_private_key, prime) == public_key:
            return possible_private_key
    return None
def main():
    prime = generate_prime()
    base = generate_random_base()
    alice_private_key = generate_private_key(prime)
    bob_private_key = generate_private_key(prime)
    alice_public_key = compute_public_key(base, alice_private_key, prime)
    bob_public_key = compute_public_key(base, bob_private_key, prime)
    print(f"g : {base}")
    print(f"p : {prime}")
    print(f"Alice's public key: {alice_public_key}")
    print(f"Bob's public key: {bob_public_key}")
    alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, prime)
    bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, prime)
    if alice_shared_secret != bob_shared_secret:
        print("Woah! Something is terribly wrong.")
    else:
        print(f"Alice's and Bob's shared secret: {alice_shared_secret}")
    print("\n---Brute force---")
    brute_forced_private_key = brute_force_private_key(alice_public_key, base, prime)
    brute_forced_secret = compute_shared_secret(bob_public_key, brute_forced_private_key, prime)
    print(f"\nFound! Alice's and Bob's shared secret: {brute_forced_secret}")
if __name__ == "__main__":
    main()