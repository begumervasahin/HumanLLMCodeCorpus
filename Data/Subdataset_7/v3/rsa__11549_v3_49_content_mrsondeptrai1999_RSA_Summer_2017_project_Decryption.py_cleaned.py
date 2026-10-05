from fractions import gcd
from random import randint
def fonk1(d, b8, b5, b6):
    return gcd(b8 * d - 1, (b5 - 1)*(b6 - 1)) == (b5 - 1)*(b6 - 1)
def fonk2(b4, b10, b7):
    b1 = [(num ** b10) % b7 for num in b4]
    return b1
def fonk3(b4):
    b2 = [chr(num) for num in b4]
    return b2
def fonk4():
    b3 = input('Please enter the encoded message here in numbers form: ')
    b4 = [int(num) for num in b3.split()]
    b5 = input('Please enter your first password: ')
    b6 = input('Please enter your second password: ')
    b7 = input('Please enter your Public Key number: ')
    b8 = input('Please enter your Private Key number: ')
    b9 = False
    while not b9:
        b10 = randint(0, b7)
        if fonk1(b10, b8, b5, b6):
            b9 = True
    b11 = fonk2(b4, b10, b7)
    b12 = ''.join(fonk3(b11))
    print('Decrypted message: %s' % b12)
    print('\nThank you for using our service!')
if b13 = = "__main__":
    fonk4()