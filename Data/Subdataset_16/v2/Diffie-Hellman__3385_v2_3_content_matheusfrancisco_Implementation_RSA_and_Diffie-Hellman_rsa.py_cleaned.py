import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
class class1:
    def fonk1(self):
        self.n, self.d, self.b1 = GenParms(n_bits=100, DEBUG=True)
    def fonk2(self, b5):
        b2 = [modExp(i, self.b1, self.n) for i in b5]
        print('\nEncrypted Message:', b2)
        return b2
    def fonk3(self, b5):
        b3 = [modExp(i, self.d, self.n) for i in b5]
        print('Decrypted Message:', b3)
        return b3
    def fonk4(self):
        return self.n, self.b1
    def fonk5(self):
        return self.n, self.d
def fonk6():
    print("Testing class1 Implementation:")
    b4 = class1()
    print('\nPublic Key:', b4.fonk4())
    print('Private Key:', b4.fonk5())
    b5 = [42, 12, 89]
    b2 = b4.fonk2(b5)
    b3 = b4.fonk3(b2)
    print('\nOriginal Message:', b5)
    print('Encrypted Message:', b2)
    print('Decrypted Message:', b3)
if b6 = = '__main__':
    fonk6()