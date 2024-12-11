from fractions import gcd
from random import randint
def fonk1(d, b7, b5, b6):
    return gcd(b7 * d - 1, (b5 - 1)*(b6 - 1)) == (b5 - 1)*(b6 - 1)
def fonk2(input1, b9, b2):
    b1 = []
    for C in input1:
        b1.append((C**b9) % b2)
    return b1
def fonk3(input2):
    b2 = []
    for C in input2:
        b2.append(chr(C))
    return b2
def fonk4():
    b3 = raw_input('Please b9 in the encoded message here in numbers form: ')
    b4 = b3.split()
    b4 = [int(a) for a in b4]
    b5 = input('Please b9 in your first password: ')
    b6 = input('Please b9 in your second password: ')
    b2 = input('please enter your Public Key number: ')
    b7 = input('please enter your Private Key number: ')
    b8 = True
    while b8:
        b9 = randint(0, b2)
        if fonk1(b9, b7, b5, b6):
            b8 = False
    b10 = fonk2(b4, b9, b2)
    b11 = ''.join(fonk3(b10))
    print('Decrypted message: %s' % b11)
    print('\nThank you for trusting our service!')
if b12 = = "__main__":
    fonk4()