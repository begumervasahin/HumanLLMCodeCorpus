import sys
def fast_exponentiation(base, exponent, modulo):
    result = 1
    base_mod = base % modulo
    exp = exponent
    while exp > 0:
        if exp % 2 == 0:
            base_mod = (base_mod * base_mod) % modulo
            exp
        else:
            result = (result * base_mod) % modulo
            exp -= 1
    return result
def input_secret_and_calculate(base, prime):
    secret = int(input(f"Enter your secret value (less than {prime}): "))
    public_key = fast_exponentiation(base, secret, prime)
    print(f"Calculating public key 'y'... Done! 'y' = {public_key}")
    return secret, public_key
def exchange_public_keys(user_a, user_b):
    print("Exchanging public keys...")
    user_b['received'] = user_a['public']
    user_a['received'] = user_b['public']
    print("Public keys exchanged successfully!")
def generate_shared_secret(user):
    print("Generating shared secret key 'k'...")
    shared_secret = fast_exponentiation(user['received'], user['secret'], prime_number)
    print(f"Shared secret key 'k' generated! 'k' = {shared_secret}")
    return shared_secret
def main():
    global prime_number, alpha
    prime_number = int(input("Enter the prime number 'p': "))
    alpha = int(input("Enter the primitive root 'alpha': "))
    print()
    user_a = {'name': 'User A'}
    user_b = {'name': 'User B'}
    user_a['secret'], user_a['public'] = input_secret_and_calculate(alpha, prime_number)
    user_b['secret'], user_b['public'] = input_secret_and_calculate(alpha, prime_number)
    exchange_public_keys(user_a, user_b)
    user_a['key'] = generate_shared_secret(user_a)
    user_b['key'] = generate_shared_secret(user_b)
    print("\nComparing shared secret keys...")
    if user_a['key'] == user_b['key']:
        print("SUCCESS! The generated keys match!")
    else:
        print("ERROR! The generated keys DO NOT match!")
if __name__ == "__main__":
    main()
    sys.exit(0)