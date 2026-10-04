import secrets
import math_functions
class RSA:
    def __init__(self):
        self._p = 0
        self._q = 0
        self._n = 0
        self._e = 3
        self._d = 0
        self._min_prime = 0
        self._max_prime = 1000
    def file_setup(self, file_control):
        self._p = int(file_control.keys[0])
        self._q = int(file_control.keys[1])
        self._d = int(file_control.keys[2])
        self._e = int(file_control.keys[3])
        self._n = int(file_control.keys[4])
        return self._e, self._n
    def setup(self):
        primes = self._generate_primes(self._min_prime, self._max_prime)
        self._p = self._select_prime(primes)
        self._q = self._select_prime(primes, exclude=self._p)
        self._n = self._p * self._q
        totient = (self._p - 1) * (self._q - 1)
        self._d = math_functions.mulinv(self._e, totient)
        return self._e, self._n
    def _generate_primes(self, start, end):
        return [i for i in range(start, end) if math_functions.is_prime(i)]
    def _select_prime(self, primes, exclude=None):
        prime = secrets.choice(primes)
        while not self._is_valid_prime(prime, exclude):
            prime = secrets.choice(primes)
        return prime
    def _is_valid_prime(self, prime, exclude):
        return (prime - 5) % 6 == 0 and prime != exclude
    def encrypt(self, msg):
        encoded_msg = [pow(ord(char), self._e, self._n) for char in msg]
        return ' '.join(map(str, encoded_msg))
    def decrypt(self, encrypted_msg):
        encrypted_list = map(int, encrypted_msg.split())
        decrypted_list = [chr(pow(char, self._d, self._n)) for char in encrypted_list]
        return ''.join(decrypted_list)
    def get_public_n(self):
        return self._n
    def keys_to_string(self):
        keys = [self._p, self._q, self._d, self._e, self._n]
        return ' '.join(map(str, keys))