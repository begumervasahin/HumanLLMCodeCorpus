
b1 = input('Please enter the encoded message here in numbers form: ')
b2 = b1.split()
b2 = [int(a) for a in b2]
b3 = input('Please enter your first password: ')
b4 = input('Please enter your second password: ')
b5 = input('Please enter your Public Key number: ')
b6 = input('Please enter your Private Key number: ')
from fractions import gcd
from random import randint
def fonk1(d):
    if gcd(b6 * d - 1, (b3 - 1) * (b4 - 1)) == (b3 - 1) * (b4 - 1):
        return True
    else:
        return False
b7 = True
while b7:
    b8 = randint(0, b5)
    if fonk1(b8):
        b7 = False
    else:
        pass
def fonk2(input1):
    b9 = []
    for C in input1:
        b9.append((C ** b8) % b5)
    return b9
b10 = fonk2(b2)
def fonk3(input2):
    b11 = []
    for char_code in input2:
        b11.append(chr(char_code))
    return b11
b12 = ''.join(fonk3(b10))
print('\nDecrypted message:', b12)
print('\nThank you for trusting our service!')