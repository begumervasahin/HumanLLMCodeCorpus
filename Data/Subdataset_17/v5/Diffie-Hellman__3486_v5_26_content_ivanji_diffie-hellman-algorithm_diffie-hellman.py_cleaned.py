def calculate_shared_key(base, secret, prime):
    return pow(base, secret, prime)
def display_key_exchange_info(role, result, shared_key=None):
    print("--------------------------")
    if shared_key is not None:
        print(f"{role} performs the operation using the received result and calculates the shared key: {shared_key}")
    else:
        print(f"{role} calculates the result and sends it: {result}")
def main():
    shared_base = 47
    shared_prime = 199
    print(f"g is equal to {shared_base} & p is equal to {shared_prime}")
    print("--------------------------")
    alice_secret = 6
    bob_secret = 2
    print("Alice performs the following operation: g^a mod p and sends result (A) to Bob")
    alice_result = calculate_shared_key(shared_base, alice_secret, shared_prime)
    display_key_exchange_info("Alice", alice_result)
    print("Bob performs the same operation and sends result (B) to Alice")
    bob_result = calculate_shared_key(shared_base, bob_secret, shared_prime)
    display_key_exchange_info("Bob", bob_result)
    print("Alice now performs the same operation using the calculated result (B) from Bob")
    alice_shared_key = calculate_shared_key(bob_result, alice_secret, shared_prime)
    display_key_exchange_info("Alice", bob_result, alice_shared_key)
    print("Bob now performs the same operation using the calculated result (A) from Alice")
    bob_shared_key = calculate_shared_key(alice_result, bob_secret, shared_prime)
    display_key_exchange_info("Bob", alice_result, bob_shared_key)
    print("--------------------------")
    assert alice_shared_key == bob_shared_key, "Shared keys do not match!"
    print(f"Shared Key is equal to {alice_shared_key}.")
    print("Now try this with large prime numbers!")
if __name__ == "__main__":
    main()