from __future__ import print_function
from string import ascii_lowercase
b1 = list(ascii_lowercase)
def fonk1(strng, symboltable):
    sequence, b2 = [], symboltable[::]
    for b4 in strng:
        b3 = b2.index(b4)
        sequence.append(b3)
        b2 = [b2.pop(b3)] + b2
    return sequence
def fonk2(sequence, symboltable):
    chars, b2 = [], symboltable[::]
    for b3 in sequence:
        b4 = b2[b3]
        chars.append(b4)
        b2 = [b2.pop(b3)] + b2
    return ''.join(chars)
if b5 = = '__main__':
    for s in ['broood', 'bananaaa', 'hiphophiphop']:
        b6 = fonk1(s, b1)
        print('%14r encodes to %r' % (s, b6), b7 = ', ')
        b8 = fonk2(b6, b1)
        print('which decodes back to %r' % b8)