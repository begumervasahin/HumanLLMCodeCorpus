def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b
def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
print('--------------------------------------------------------')
print("To factorize N, you can use either of the following methods:")
print("1. Install factordb-pycli using 'sudo pip install factordb-pycli'")
print("   Usage: factordb integer_you_want_to_factorize")
print("2. Alternatively, you can use https:
print('--------------------------------------------------------')
print("----------------------")
print("INPUT")
print("----------------------")
prime_1 = int(input("Enter prime number 1 (p): "))
prime_2 = int(input("Enter prime number 2 (q): "))
e = int(input("Enter the value of 'e': "))
cipher_text = int(input("Enter the cipher text (as an integer): "))
d = modular_inverse(e, (prime_1 - 1) * (prime_2 - 1))
print("----------------------")
print("OUTPUT")
print("----------------------")
print("Computed private exponent (d):", d)
plain_text = pow(cipher_text, d, prime_1 * prime_2)
print("Decrypted plain text:", plain_text)