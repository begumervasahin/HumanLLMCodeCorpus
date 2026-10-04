import random
class Public_Key:
    def __init__(self, p, k, g):
        self.p = p
        self.k = k
        self.g = g
    @staticmethod
    def make_public_key(p, k):
        g = (random.randint(1, p-1), random.randint(1, p-1))
        return Public_Key(p, k, g)
    def __str__(self):
        return f"Public Key:\nPrime: {self.p}\nKey: {self.k}\nGenerator: {self.g}"
def random_prime(low, high):
    primes = [num for num in range(low, high) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return random.choice(primes)
def randint(low, high):
    return random.randint(low, high)
def encrypt(message, public_key):
    return [(ord(char) * public_key.k) % public_key.p for char in message]
def decrypt(encrypted_message, public_key, k):
    return ''.join([chr((char * pow(k, -1, public_key.p)) % public_key.p) for char in encrypted_message])
def main():
    print("Elliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* press ctrl-c to exit the loop and the demo")
    print()
    numZeros = int(input("Enter a number of digits for the prime number (i.e. 3 => 100 < prime < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if numZeros < 6:
        numZeros = 6
    low = 10 ** (numZeros - 1)
    high = low * 10
    p = random_prime(low, high)
    k = randint(1, p - 1)
    public_key = Public_Key.make_public_key(p, k)
    print(public_key)
    print()
    while True:
        s = input("Enter a message to be encrypted\n")
        print()
        encrypted = encrypt(s, public_key)
        print("Encrypted array of points on the curve:\n", encrypted)
        print()
        print("Decrypted string:\n", decrypt(encrypted, public_key, k))
        print()
if __name__ == "__main__":
    main()