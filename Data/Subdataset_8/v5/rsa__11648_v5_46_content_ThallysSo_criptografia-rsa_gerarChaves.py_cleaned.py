from cryptography import Cryptography
class Keys(Cryptography):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def generate_keys(self):
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        print("Choose your public key:\n")
        print(str(self.get_coprimes(phi)) + "\n")
        e = int(input())
        d = self.modular_inverse(e, phi)
        public_keys = "(e={}, n={})".format(e, n)
        private_keys = "(d={}, n={})".format(d, n)
        return print("\nPublic keys " + public_keys + "\nPrivate keys " + private_keys + "\n")
    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b
    def modular_inverse(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        print('No modular inverse for the block.\n')
        return None
    def get_coprimes(self, a):
        coprime_list = []
        for x in range(2, a):
            if self.gcd(a, x) == 1 and self.modular_inverse(x, a) is not None:
                coprime_list.append(x)
        for x in coprime_list[:]:
            if x == self.modular_inverse(x, a):
                coprime_list.remove(x)
        return coprime_list