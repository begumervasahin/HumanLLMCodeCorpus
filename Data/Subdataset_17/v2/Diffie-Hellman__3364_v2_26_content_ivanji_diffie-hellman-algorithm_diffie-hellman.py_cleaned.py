def calculate_shared_key(base, secret, prime):
    return pow(base, secret, prime)
def main():
    shared_base = 47
    shared_prime = 199
    print(f"g is equal to {shared_base} & p is equal to {shared_prime}")
    print("--------------------------")
    alice_secret = 6
    bob_secret = 2
    print("Alice performs the following operation: g^a mod p and sends result (A) to Bob")
    A = calculate_shared_key(shared_base, alice_secret, shared_prime)
    print(f"Alice's result (A): {A}")
    print("--------------------------")
    print("Bob performs the same operation and sends result (B) to Alice")
    B = calculate_shared_key(shared_base, bob_secret, shared_prime)
    print(f"Bob's result (B): {B}")
    print("--------------------------")
    print("Alice now performs the same operation using calculated result (B) from Bob")
    alice_shared_key = calculate_shared_key(B, alice_secret, shared_prime)
    print(f"Alice's shared key: {alice_shared_key}")
    print("--------------------------")
    print("Bob now performs the same operation using calculated result (A) from Alice")
    bob_shared_key = calculate_shared_key(A, bob_secret, shared_prime)
    print(f"Bob's shared key: {bob_shared_key}")
    print("--------------------------")
    assert alice_shared_key == bob_shared_key, "Shared keys do not match!"
    print(f"Shared Key is equal to {alice_shared_key}.")
    print("Now try this with large prime numbers!")
if __name__ == "__main__":
    main()