import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
class class1:
    def fonk1(self):
        self.n, self.d, self.b1 = GenParms(n_bits=100, DEBUG=True)
    def fonk2(self, msg):
        b2 = [modExp(i, self.b1, self.n) for i in msg]
        print('\nMensagem criptografada:', b2)
        return b2
    def fonk3(self, msg):
        b3 = [modExp(i, self.d, self.n) for i in msg]
        print('Mensagem Decriptografada:', b3)
        return b3
    def fonk4(self):
        return self.n, self.b1
    def fonk5(self):
        return self.n, self.d
if b4 = = '__main__':
    print("Rotina de testes:")
    b5 = class1()
    print('Public Key:', b5.fonk4())
    print('Private Key:', b5.fonk5())