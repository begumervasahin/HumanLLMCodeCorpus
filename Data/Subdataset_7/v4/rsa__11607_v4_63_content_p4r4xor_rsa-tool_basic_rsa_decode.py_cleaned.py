def fonk1(b1, b):
    if b1 = = 0:
        return (b, 0, 1)
    else:
        gcd, x, b2 = fonk1(b % b1, b1)
        return (gcd, b2 - (b
def fonk2(b1, m):
    gcd, x, b2 = fonk1(b1, m)
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
b3 = int(input("Enter prime number 1 (p): "))
b4 = int(input("Enter prime number 2 (q): "))
b5 = int(input("Enter the value of 'b5': "))
b6 = int(input("Enter the cipher text (as an integer): "))
b7 = fonk2(b5, (b3 - 1) * (b4 - 1))
print("----------------------")
print("OUTPUT")
print("----------------------")
print("Computed private exponent (b7):", b7)
b8 = pow(b6, b7, b3 * b4)
print("Decrypted plain text:", b8)