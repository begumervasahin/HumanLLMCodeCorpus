import secrets
import sympy
def is_prime(num):
    return sympy.isprime(num)
def mulinv(e, totient):
    g, x, y = egcd(e, totient)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % totient
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b
class Rsa:
    def __init__(self):
        self.__q = 0
        self.__p = 0
        self.__n = 0
        self.__e = 3
        self.__d = 0
        self.__minPrime = 0
        self.__maxPrime = 1000
    def file_setup(self, file_control):
        self.__p = int(file_control.keys[0])
        self.__q = int(file_control.keys[1])
        self.__d = int(file_control.keys[2])
        self.__e = int(file_control.keys[3])
        self.__n = int(file_control.keys[4])
        return self.__e, self.__n
    def setup(self):
        primes = [i for i in range(self.__minPrime, self.__maxPrime) if is_prime(i)]
        self.__p = secrets.choice(primes)
        while (self.__p - 5) % 6 != 0:
            self.__p = secrets.choice(primes)
        self.__q = secrets.choice(primes)
        while (self.__q - 5) % 6 != 0 or (self.__p == self.__q):
            self.__q = secrets.choice(primes)
        self.__n = self.__p * self.__q
        totient = (self.__p - 1) * (self.__q - 1)
        self.__d = mulinv(self.__e, totient)
        return self.__e, self.__n
    def encrypt(self, msg):
        encoded_msg = [pow(ord(char), self.__e, self.__n) for char in msg]
        return ' '.join(map(str, encoded_msg))
    def decrypt(self, encrypted_msg):
        encrypted_list = map(int, encrypted_msg.split())
        decrypted_list = [chr(pow(num, self.__d, self.__n)) for num in encrypted_list]
        return ''.join(decrypted_list)
    def get_public_n(self):
        return self.__n
    def keys_toString(self):
        keys = [self.__p, self.__q, self.__d, self.__e, self.__n]
        return ' '.join(map(str, keys))
if __name__ == "__main__":
    rsa = Rsa()
    public_keys = rsa.setup()
    print(f"Public keys: {public_keys}")
    message = "Hello, World!"
    encrypted_message = rsa.encrypt(message)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = rsa.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")