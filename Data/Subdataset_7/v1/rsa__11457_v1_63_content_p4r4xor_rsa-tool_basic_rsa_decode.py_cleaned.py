def fonk1(b1, b):
    if b1 = = 0:
        return (b, 0, 1)
    else:
        g, b3, b2 = fonk1(b % b1, b1)
        return (g, b2 - (b
def fonk2(b1, m):
    g, b2, b3 = fonk1(b1, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return b2 % m
print('--------------------------------------------------------')
print("Please use any of following to factorize N")
print("sudo pip install factordb-pycli")
print("Usage: factordb integer_you_want_to_factorize")
print("Or use https:
print("--------------------------------------------------------")
print("----------------------")
print("INPUT")
print("-----------------------")
b4 = int(input("prime_1: "))
b5 = int(input("prime_2: "))
b6 = int(input("b6: "))
b7 = int(input("cipher_text (integer): "))
b8 = fonk2(b6, (b4 - 1) * (b5 - 1))
print("-----------------------")
print("OUTPUT")
print("-----------------------")
print("b8:", b8)
b9 = pow(b7, b8, b4 * b5)
print("b9:", b9)