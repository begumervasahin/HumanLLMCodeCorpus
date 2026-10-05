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
    user_a['x'] = int(input("User A: Enter your secret 'xA': "))
    print("Calculating 'yA' for User A... ", end="")
    user_a['y'] = fast_exponentiation(alpha, user_a['x'], prime_number)
    print("'yA' =", user_a['y'])
    print()
    user_b['x'] = int(input("User B: Enter your secret 'xB': "))
    print("Calculating 'yB' for User B... ", end="")
    user_b['y'] = fast_exponentiation(alpha, user_b['x'], prime_number)
    print("'yB' =", user_b['y'])
    print()
    print("Sending 'yA' to User B... ", end="")
    user_b['y_prim'] = user_a['y']
    print("Done!")
    print("Sending 'yB' to User A... ", end="")
    user_a['y_prim'] = user_b['y']
    print("Done!")
    print()
    print("Generating key 'k' for User A... ", end="")
    user_a['k'] = fast_exponentiation(user_a['y_prim'], user_a['x'], prime_number)
    print("'k' =", user_a['k'])
    print("Generating key 'k' for User B... ", end="")
    user_b['k'] = fast_exponentiation(user_b['y_prim'], user_b['x'], prime_number)
    print("'k' =", user_b['k'])
    print()
    if user_a['k'] == user_b['k']:
        print("SUCCESS! The generated keys match!")
    else:
        print("ERROR! The generated keys DO NOT match!")
    sys.exit(0)
if __name__ == "__main__":
    main()