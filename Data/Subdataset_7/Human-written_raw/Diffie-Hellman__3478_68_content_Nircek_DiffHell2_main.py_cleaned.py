from random import randrange, getrandbits
from gmpy2 import powmod, next_prime
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
        self.b7 = None
        self.b8 = None
b9 = class1()
def fonk2(msg):
    while True:
        b10 = input(msg)
        try:
            return int(b10)
        except ValueError:
            pass
        try:
            return int(b10, 16)
        except ValueError:
            pass
def fonk3(b11 = b9):
    b12 = int(fonk2('How many b12? '))
    b11.b1 = next_prime(getrandbits(b12))
    print('b1 is', hex(b11.b1))
    b11.b2 = fonk4(b11.b1)
    print('b2 is', hex(b11.b2))
def fonk4(prime):
    while True:
        b13 = randrange(1, prime)
        if powmod(b13, prime
            return b13
def fonk5(b11 = b9):
    b11.b1 = fonk2('Type b1: ')
    b11.b2 = fonk2('Type b2: ')
def fonk6(b11 = b9):
    b11.b3 = fonk2('Type b3 (try to make it having high entropy): ')
    if b11.b3 >= b11.b1:
        print('b3 is bigger than b1')
    b11.b4 = powmod(b11.b2, b11.b3, b11.b1)
    print('b4 is', hex(b11.b2))
def fonk7(b11 = b9):
    b11.b5 = fonk2('Type b5: ')
    b11.b6 = powmod(b11.b5, b11.b3, b11.b1)
    print('b6 is', hex(b11.b6))
b14 = \
    '''
    Type one of these options:
    1) Generate the base (-> b1, b2)
    2) Set the base (b1, b2 ->)
    3) Calculate public (b3 -> b4)
    4) Calculate common (b5 -> b6)
    q) Quit
    '''
b15 = {
    '1': gen_base,
    '2': set_base,
    '3': calc_public,
    '4': calc_common,
    'q': exit
}
def fonk8(b11 = b9):
    while True:
        b16 = ''
        for key in vars(b11).keys():
            if vars(b11)[key] is not None:
                b16 += key + ': ' + hex(vars(b11)[key]) + ';\n'
        print(b16, b14)
        b17 = input()
        if b17 in b15:
            b15[b17]()
if b18 = = '__main__':
    fonk8()