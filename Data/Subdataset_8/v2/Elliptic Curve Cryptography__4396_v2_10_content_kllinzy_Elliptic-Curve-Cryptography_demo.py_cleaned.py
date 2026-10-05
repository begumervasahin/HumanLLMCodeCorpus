from ecc import *
import sys
print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
print("*Note* press ctrl-c to exit the loop and the demo\n")
num_zeros = int(input("Enter the number of digits for the prime number (e.g., 3 => 100 < prime < 1000).\nMinimum is 6\nNumber of Zeros = "))
if num_zeros < 6:
    num_zeros = 6
low = 1
for i in range(1, num_zeros):
    low *= 10
high = low * 10
p = random_prime(low, high)
k = randint(1, p - 1)
public_key = Public_Key.make_public_key(p, k)
print(public_key)
print()
try:
    while True:
        message = input("Enter a message to be encrypted\n")
        print()
        encrypted_points = encrypt(message, public_key)
        print("Encrypted array of points on the curve:\n", encrypted_points)
        print()
        decrypted_message = decrypt(encrypted_points, public_key, k)
        print("Decrypted string:\n", decrypted_message)
        print()
except KeyboardInterrupt:
    print("\nExiting the demo...")
    sys.exit(0)