from ecc import *
import sys
print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
print("*Note* press ctrl-c to exit the loop and the demo\n")
b1 = int(input("Enter a number of digits for the prime number (i.e., 3 => 100 < prime < 1000).\nMinimum is 6\nNumber of Zeros = "))
if b1 < 6:
    b1 = 6
a1 = 1
for i in range(1, b1):
    a1 *= 10
b2 = a1 * 10
b3 = random_prime(a1, b2)
b4 = randint(1, b3 - 1)
b5 = Public_Key.make_public_key(b3, b4)
print(b5)
print()
try:
    while True:
        b6 = input("Enter a b6 to be encrypted\n")
        print()
        b7 = encrypt(b6, b5)
        print("Encrypted array of points on the curve:\n", b7)
        print()
        b8 = decrypt(b7, b5, b4)
        print("Decrypted string:\n", b8)
        print()
except KeyboardInterrupt:
    print("\nExiting the demo...")
    sys.exit(0)