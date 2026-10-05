from ecc import *
import sys
def generate_prime_number(num_digits):
    min_value = 10 ** (num_digits - 1)
    max_value = (10 ** num_digits) - 1
    return random_prime(min_value, max_value)
def main():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* press ctrl-c to exit the loop and the demo\n")
    num_digits = int(input("Enter the number of digits for the prime number (e.g., 3 => 100 < prime < 1000).\nMinimum is 6\nNumber of Digits = "))
    num_digits = max(6, num_digits)
    p = generate_prime_number(num_digits)
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
if __name__ == "__main__":
    main()