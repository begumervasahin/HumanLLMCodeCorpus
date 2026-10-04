from __future__ import print_function
from string import ascii_lowercase
b1 = list(ascii_lowercase)
def fonk1(string, symbol_table):
    b2 = []
    b3 = symbol_table[:]
    for b6 in string:
        b4 = b3.b4(b6)
        b2.append(b4)
        b3 = [b3.pop(b4)] + b3
    return b2
def fonk2(b2, symbol_table):
    b5 = []
    b3 = symbol_table[:]
    for b4 in b2:
        b6 = b3[b4]
        b5.append(b6)
        b3 = [b3.pop(b4)] + b3
    return ''.join(b5)
if b7 = = '__main__':
    b8 = ['broood', 'bananaaa', 'hiphophiphop']
    for s in b8:
        b9 = fonk1(s, b1)
        print(f'{s:14} encodes to {b9}', b10 = ', ')
        b11 = fonk2(b9, b1)
        print(f'which decodes back to {b11}')