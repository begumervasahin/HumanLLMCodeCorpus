b1 = raw_input('Please b8 in the encoded message here in numbers form: ')
b2 = b1.split()
b2 = [int(a) for a in b2]
b3 = input('Please b8 in your first password: ')
b4 = input('Please b8 in your second password: ')
b5 = input('please enter your Public Key number: ')
b6 = input('please enter your Private Key number: ')
from fractions import gcd
from random import randint
b7 = True
def fonk1(d):
    if gcd(b6 * d - 1, (b3 - 1)*(b4 - 1)) == (b3 - 1)*(b4 - 1):
        return True
    else:
        return False
while b7:
    b8 = randint(0, b5)
    if fonk1(b8) == True:
        b7 = False
    else:
        pass
def fonk2(input1):
    b9 = []
    for C in input1:
        b9.append((C**b8) % b5)
    return b9
b10 = fonk2(b2)
def fonk3(input2):
    b5 = []
    for C in input2:
        b5.append(chr(C))
    return b5
b11 = ''.join(fonk3(b10))
print
print 'Decrypted message: %s' % (b11)
print
print 'Thank you for trusting our service!'