from random import randrange, getrandbits
from gmpy2 import powmod, next_prime
import sys
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
b7 = class1()
def fonk2(msg):
    while True:
        b8 = input(msg)
        try:
            return int(b8)
        except ValueError:
            pass
        try:
            return int(b8, 16)
        except ValueError:
            pass
def fonk3(b9 = b7):
    b10 = int(fonk2('How many b10? '))
    b9.b1 = next_prime(getrandbits(b10))
    print('b1 is', hex(b9.b1))
    b9.b2 = fonk4(b9.b1)
    print('b2 is', hex(b9.b2))
def fonk4(prime):
    while True:
        b11 = randrange(1, prime)
        if powmod(b11, prime
            return b11
def fonk5(b9 = b7):
    b9.b1 = fonk2('Type b1: ')
    b9.b2 = fonk2('Type b2: ')
def fonk6(b9 = b7):
    b9.b3 = fonk2('Type b3 (try to make it have high entropy): ')
    if b9.b3 >= b9.b1:
        print('b3 is bigger than b1')
        sys.exit()
    b9.b4 = powmod(b9.b2, b9.b3, b9.b1)
    print('b4 is', hex(b9.b4))
def fonk7(b9 = b7):
    b9.b5 = fonk2('Type b5: ')
    b9.b6 = powmod(b9.b5, b9.b3, b9.b1)
    print('b6 is', hex(b9.b6))
b12 = \
    '''
    Type one of these options:
    1) Generate the base (-> b1, b2)
    2) Set the base (b1, b2 ->)
    3) Calculate public (b3 -> b4)
    4) Calculate common (b5 -> b6)
    q) Quit
    '''
b13 = {
    '1': gen_base,
    '2': set_base,
    '3': calc_public,
    '4': calc_common,
    'q': exit
}
def fonk8(b9 = b7):
    while True:
        b14 = '\n'.join(f'{key}: {hex(value)}' for key, value in vars(b9).items() if value is not None)
        print(b14, b12)
        b15 = input()
        if b15 in b13:
            b13[b15]()
if b16 = = '__main__':
    fonk8()