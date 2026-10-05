from math import sqrt, ceil, gcd
from sympy.ntheory import is_primitive_root, nextprime
from secrets import randbits
class DiffieHellman:
    def __init__(self, key_size, secret, key=None):
        self.key_size = key_size
        self.secret = secret
        if key is None:
            self.generate_public_secret()
        else:
            self.prime, self.g = key
    def get_common(self):
        return self.prime, self.g
    def generate_prime(self):
        self.prime = nextprime(randbits(self.key_size))
    def generate_public_secret(self):
        self.generate_prime()
        self.find_primitive_root_mod()
    def find_primitive_root_mod(self):
        for x in range(2, self.prime):
            if is_primitive_root(x, self.prime):
                self.g = x
                break
    def compute_shared(self):
        return pow(self.g, self.secret, self.prime)
    def get_shared_secret(self, shared):
        return pow(shared, self.secret, self.prime)
if __name__ == "__main__":
    key_size = 512
    secret = 123456789
    alice = DiffieHellman(key_size, secret)
    bob = DiffieHellman(key_size, secret)
    alice_public = alice.get_common()
    bob_public = bob.get_common()
    alice_shared_secret = alice.get_shared_secret(bob_public[1])
    bob_shared_secret = bob.get_shared_secret(alice_public[1])
    print("Alice's shared secret:", alice_shared_secret)
    print("Bob's shared secret:", bob_shared_secret)