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
def main():
    user_a = {}
    user_b = {}
    prime_number = int(input("Enter the prime number 'p': "))
    alpha = int(input("Enter the number 'alpha': "))
    print()
    user_a['secret'] = int(input("User A: Enter your secret 'xA': "))
    print("Calculating 'yA' for User A... ", end="")
    user_a['public'] = fast_exponentiation(alpha, user_a['secret'], prime_number)
    print("'yA' =", user_a['public'])
    print()
    user_b['secret'] = int(input("User B: Enter your secret 'xB': "))
    print("Calculating 'yB' for User B... ", end="")
    user_b['public'] = fast_exponentiation(alpha, user_b['secret'], prime_number)
    print("'yB' =", user_b['public'])
    print()
    print("Sending 'yA' to User B... ", end="")
    user_b['received'] = user_a['public']
    print("Done!")
    print("Sending 'yB' to User A... ", end="")
    user_a['received'] = user_b['public']
    print("Done!")
    print()
    print("Generating key 'k' for User A... ", end="")
    user_a['key'] = fast_exponentiation(user_a['received'], user_a['secret'], prime_number)
    print("'k' =", user_a['key'])
    print("Generating key 'k' for User B... ", end="")
    user_b['key'] = fast_exponentiation(user_b['received'], user_b['secret'], prime_number)
    print("'k' =", user_b['key'])
    print()
    if user_a['key'] == user_b['key']:
        print("SUCCESS! The generated keys match!")
    else:
        print("ERROR! The generated keys DO NOT match!")
    sys.exit(0)
if __name__ == "__main__":
    main()