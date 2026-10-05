from ecc import *
import sys
def fonk1(b3):
    b1 = 10 ** (b3 - 1)
    b2 = (10 ** b3) - 1
    return random_prime(b1, b2)
def fonk2():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* press ctrl-c to exit the loop and the demo\n")
    b3 = int(input("Enter the number of digits for the prime number (e.g., 3 => 100 < prime < 1000).\nMinimum is 6\nNumber of Digits = "))
    b3 = max(6, b3)
    b4 = fonk1(b3)
    b5 = randint(1, b4 - 1)
    b6 = Public_Key.make_public_key(b4, b5)
    print(b6)
    print()
    try:
        while True:
            b7 = input("Enter a b7 to be encrypted\n")
            print()
            b8 = encrypt(b7, b6)
            print("Encrypted array of points on the curve:\n", b8)
            print()
            b9 = decrypt(b8, b6, b5)
            print("Decrypted string:\n", b9)
            print()
    except KeyboardInterrupt:
        print("\nExiting the demo...")
        sys.exit(0)
if b10 = = "__main__":
    fonk2()