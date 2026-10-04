import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
class class1:
    def fonk1(self):
        self.n, self.d, self.b1 = GenParms(n_bits=100, DEBUG=True)
    def fonk2(self, b3):
        return [modExp(i, self.b1, self.n) for i in b3]
    def fonk3(self, b3):
        return [modExp(i, self.d, self.n) for i in b3]
    def fonk4(self):
        return self.n, self.b1
    def fonk5(self):
        return self.n, self.d
def fonk6():
    print("Testing class1 Implementation:")
    b2 = class1()
    print('\nPublic Key:', b2.fonk4())
    print('Private Key:', b2.fonk5())
    b3 = [42, 12, 89]
    print('\nOriginal Message:', b3)
    b4 = b2.fonk2(b3)
    print('Encrypted Message:', b4)
    b5 = b2.fonk3(b4)
    print('Decrypted Message:', b5)
    print('\nFinal Decrypted Message:', b5)
if b6 = = '__main__':
    fonk6()