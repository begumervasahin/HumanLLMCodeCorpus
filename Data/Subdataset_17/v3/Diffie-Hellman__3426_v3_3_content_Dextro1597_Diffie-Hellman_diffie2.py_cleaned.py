def get_user_input(prompt):
    return int(input(prompt))
def compute_public_value(base, secret, prime):
    return pow(base, secret, prime)
def main():
    shared_prime = get_user_input("Enter the value of the shared prime (p): ")
    shared_base = get_user_input("Enter the value of the shared base (q): ")
    alice_secret = get_user_input("Enter Alice's secret key value (a): ")
    bob_secret = get_user_input("Enter Bob's secret key value (b): ")
    print("\nShared Variables:")
    print(f"Shared Prime number: {shared_prime}")
    print(f"Shared Base number: {shared_base}")
    alice_public_value = compute_public_value(shared_base, alice_secret, shared_prime)
    print(f"\nAlice sends value over insecure channel: {alice_public_value}")
    bob_public_value = compute_public_value(shared_base, bob_secret, shared_prime)
    print(f"Bob sends value over insecure channel: {bob_public_value}")
    alice_shared_secret = compute_public_value(bob_public_value, alice_secret, shared_prime)
    print(f"\nValue computed by Alice: {alice_shared_secret}")
    bob_shared_secret = compute_public_value(alice_public_value, bob_secret, shared_prime)
    print(f"Value computed by Bob: {bob_shared_secret}")
if __name__ == "__main__":
    main()