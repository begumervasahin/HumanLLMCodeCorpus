import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
class RSA:
    def __init__(self):
        self.n, self.d, self.e = GenParms(n_bits=100, DEBUG=True)
    def encryption(self, msg):
        encrypted_message = [modExp(i, self.e, self.n) for i in msg]
        print('\nMensagem criptografada:', encrypted_message)
        return encrypted_message
    def decryption(self, msg):
        decrypted_message = [modExp(i, self.d, self.n) for i in msg]
        print('Mensagem Decriptografada:', decrypted_message)
        return decrypted_message
    def public_key(self):
        return self.n, self.e
    def private_key(self):
        return self.n, self.d
if __name__ == '__main__':
    print("Rotina de testes:")
    rsa = RSA()
    print('Public Key:', rsa.public_key())
    print('Private Key:', rsa.private_key())