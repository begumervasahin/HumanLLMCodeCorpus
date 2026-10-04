from ecc import random_prime, Public_Key, encrypt, decrypt
import random
def main():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo\n")
    num_zeros = int(input("Enter a number of digits for the prime number (i.e. 3 => 100 < prime < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if num_zeros < 6:
        num_zeros = 6
    low = 10 ** (num_zeros - 1)
    high = low * 10
    prime = random_prime(low, high)
    private_key = random.randint(1, prime - 1)
    public_key = Public_Key.make_public_key(prime, private_key)
    print(public_key)
    print()
    while True:
        message = input("Enter a message to be encrypted\n")
        print()
        encrypted_message = encrypt(message, public_key)
        print("Encrypted array of points on the curve:\n", encrypted_message)
        print()
        decrypted_message = decrypt(encrypted_message, public_key, private_key)
        print("Decrypted string:\n", decrypted_message)
        print()
if __name__ == "__main__":
    main()