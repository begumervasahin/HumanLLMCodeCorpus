from ecc import random_prime, Public_Key, encrypt, decrypt
import random
def fonk1():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo\n")
    b1 = int(input("Enter a number of digits for the b4 number (i.e. 3 => 100 < b4 < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if b1 < 6:
        b1 = 6
    b2 = 10 ** (b1 - 1)
    b3 = b2 * 10
    b4 = random_prime(b2, b3)
    b5 = random.randint(1, b4 - 1)
    b6 = Public_Key.make_public_key(b4, b5)
    print(b6)
    print()
    while True:
        b7 = input("Enter a b7 to be encrypted\n")
        print()
        b8 = encrypt(b7, b6)
        print("Encrypted array of points on the curve:\n", b8)
        print()
        b9 = decrypt(b8, b6, b5)
        print("Decrypted string:\n", b9)
        print()
if b10 = = "__main__":
    fonk1()