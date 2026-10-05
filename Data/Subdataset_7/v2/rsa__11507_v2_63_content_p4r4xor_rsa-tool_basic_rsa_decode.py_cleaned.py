def fonk1(b1, b):
    if b1 = = 0:
        return b, 0, 1
    else:
        gcd, x, b2 = fonk1(b % b1, b1)
        return gcd, x - (b
def fonk2(b1, m):
    gcd, x, b2 = fonk1(b1, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
print('--------------------------------------------------------')
print("Please use any of the following to factorize N:")
print("sudo pip install factordb-pycli")
print("Usage: factordb integer_you_want_to_factorize")
print("Or use https:
print("--------------------------------------------------------")
print("----------------------")
print("INPUT")
print("-----------------------")
b3 = int(input("Enter prime_1: "))
b4 = int(input("Enter prime_2: "))
b5 = int(input("Enter b5: "))
b6 = int(input("Enter cipher_text (integer): "))
b7 = fonk2(b5, (b3 - 1) * (b4 - 1))
print("-----------------------")
print("OUTPUT")
print("-----------------------")
print("b7:", b7)
b8 = pow(b6, b7, b3 * b4)
print("b8:", b8)