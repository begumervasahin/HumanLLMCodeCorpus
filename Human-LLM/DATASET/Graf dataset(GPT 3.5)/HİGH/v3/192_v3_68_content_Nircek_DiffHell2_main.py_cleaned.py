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
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid input. Please enter an integer.")
def fonk3(b8 = b7):
    b9 = fonk2('Enter the number of b9 for prime generation: ')
    b8.b1 = next_prime(getrandbits(b9))
    print(f'Generated prime (b1) is: {hex(b8.b1)}')
    b8.b2 = fonk4(b8.b1)
    print(f'Generated generator (b2) is: {hex(b8.b2)}')
def fonk4(prime):
    while True:
        b10 = randrange(1, prime)
        if powmod(b10, prime
            return b10
def fonk5(b8 = b7):
    b8.b1 = fonk2('Enter the prime (b1): ')
    b8.b2 = fonk2('Enter the generator (b2): ')
def fonk6(b8 = b7):
    b8.b3 = fonk2('Enter the private key (b3): ')
    if b8.b3 >= b8.b1:
        print('Error: Private key (b3) should be less than prime (b1).')
        sys.exit()
    b8.b4 = powmod(b8.b2, b8.b3, b8.b1)
    print(f'Calculated public key (b4) is: {hex(b8.b4)}')
def fonk7(b8 = b7):
    b8.b5 = fonk2('Enter the received public key (b5): ')
    b8.b6 = powmod(b8.b5, b8.b3, b8.b1)
    print(f'Calculated shared key (b6) is: {hex(b8.b6)}')
b11 = '''
    Choose an option:
    1) Generate prime and generator (b1, b2)
    2) Set prime and generator (b1, b2)
    3) Calculate public key (b4)
    4) Calculate shared key (b6)
    q) Quit
'''
b12 = {
    '1': gen_base,
    '2': set_base,
    '3': calc_public,
    '4': calc_common,
    'q': sys.exit
}
def fonk8(b8 = b7):
    while True:
        b13 = '\n'.join(f'{key}: {hex(value)}' for key, value in vars(b8).items() if value is not None)
        print(b13)
        print(b11)
        b14 = input().lower()
        if b14 in b12:
            b12[b14]()
if b15 = = '__main__':
    fonk8()