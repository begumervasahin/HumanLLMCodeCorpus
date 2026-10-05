from ecc import *
print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
print("*Note* press ctrl-c to exit the loop and the demo\n")
def generate_prime_number(num_zeros):
    min_range = 10 ** (num_zeros - 1)
    max_range = 10 ** num_zeros
    return random_prime(min_range, max_range)
def generate_random_integer(prime_number):
    return randint(1, prime_number - 1)
num_zeros = int(input("Enter the number of digits for the prime number (e.g., 3 => 100 < prime < 1000).\nMinimum is 6\nNumber of Zeros = "))
num_zeros = max(num_zeros, 6)
p = generate_prime_number(num_zeros)
k = generate_random_integer(p)
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
    exit(0)