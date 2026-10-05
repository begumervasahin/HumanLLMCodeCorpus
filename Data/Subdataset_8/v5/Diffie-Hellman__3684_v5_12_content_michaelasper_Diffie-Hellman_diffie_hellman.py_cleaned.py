from sympy.ntheory import is_primitive_root, nextprime
from secrets import randbits
class DiffieHellman:
    def __init__(self, key_size, secret, key=None):
        self.key_size = key_size
        self.secret = secret
        if key is None:
            self.generate_public_secret()
        else:
            self.prime, self.base = key
    def get_common(self):
        return self.prime, self.base
    def generate_prime(self):
        self.prime = nextprime(randbits(self.key_size))
    def generate_public_secret(self):
        self.generate_prime()
        self.find_primitive_root_mod()
    def find_primitive_root_mod(self):
        for x in range(2, self.prime):
            if is_primitive_root(x, self.prime):
                self.base = x
                break
    def compute_shared(self):
        return pow(self.base, self.secret, self.prime)
    def get_shared_secret(self, shared):
        return pow(shared, self.secret, self.prime)