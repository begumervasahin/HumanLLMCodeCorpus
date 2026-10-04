import random
class PublicKey:
    def __init__(self, prime, key, generator):
        self.prime = prime
        self.key = key
        self.generator = generator
    @staticmethod
    def create(prime, key):
        generator = (random.randint(1, prime - 1), random.randint(1, prime - 1))
        return PublicKey(prime, key, generator)
    def __str__(self):
        return f"Public Key:\nPrime: {self.prime}\nKey: {self.key}\nGenerator: {self.generator}"
def generate_random_prime(low, high):
    primes = [num for num in range(low, high) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return random.choice(primes)
def encrypt_message(message, public_key):
    return [(ord(char) * public_key.key) % public_key.prime for char in message]
def decrypt_message(encrypted_message, public_key, private_key):
    return ''.join([chr((char * pow(private_key, -1, public_key.prime)) % public_key.prime) for char in encrypted_message])
def main():
    print("Elliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo")
    print()
    num_zeros = int(input("Enter a number of digits for the prime number (i.e. 3 => 100 < prime < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if num_zeros < 6:
        num_zeros = 6
    low = 10 ** (num_zeros - 1)
    high = low * 10
    prime = generate_random_prime(low, high)
    private_key = random.randint(1, prime - 1)
    public_key = PublicKey.create(prime, private_key)
    print(public_key)
    print()
    while True:
        message = input("Enter a message to be encrypted\n")
        print()
        encrypted_message = encrypt_message(message, public_key)
        print("Encrypted array of points on the curve:\n", encrypted_message)
        print()
        decrypted_message = decrypt_message(encrypted_message, public_key, private_key)
        print("Decrypted string:\n", decrypted_message)
        print()
if __name__ == "__main__":
    main()