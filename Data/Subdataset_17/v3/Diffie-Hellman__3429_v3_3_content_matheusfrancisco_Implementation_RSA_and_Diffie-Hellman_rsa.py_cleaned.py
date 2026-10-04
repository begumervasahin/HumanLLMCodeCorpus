import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
class RSA:
    def __init__(self):
        self.n, self.d, self.e = GenParms(n_bits=100, DEBUG=True)
    def encrypt(self, message):
        return [modExp(i, self.e, self.n) for i in message]
    def decrypt(self, message):
        return [modExp(i, self.d, self.n) for i in message]
    def get_public_key(self):
        return self.n, self.e
    def get_private_key(self):
        return self.n, self.d
def main():
    print("Testing RSA Implementation:")
    rsa = RSA()
    print('\nPublic Key:', rsa.get_public_key())
    print('Private Key:', rsa.get_private_key())
    message = [42, 12, 89]
    print('\nOriginal Message:', message)
    encrypted_message = rsa.encrypt(message)
    print('Encrypted Message:', encrypted_message)
    decrypted_message = rsa.decrypt(encrypted_message)
    print('Decrypted Message:', decrypted_message)
if __name__ == '__main__':
    main()