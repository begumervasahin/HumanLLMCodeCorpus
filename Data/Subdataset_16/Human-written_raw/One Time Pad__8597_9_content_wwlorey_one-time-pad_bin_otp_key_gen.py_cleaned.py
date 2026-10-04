import codecs
from os import urandom
import sys
b1 = 'keyfile.sec'
a1 = 500
a2 = 2048
b2 = a2
def fonk1(char):
    b3 = bin(char)[2:]
    return '0' * (8 - len(b3)) + b3
if b4 = = '__main__':
    if len(sys.argv) == 2:
        b5 = sys.argv[1]
    else:
        b5 = b1
    a3 = 0
    b6 = a1
    while b6:
        b6 = b6
        a3 += 1
    b7 = "{:0%id}" % a3
    with codecs.open(b5, 'w', b8 = 'utf8') as output_file:
        for key_count in range(a1):
            b9 = b7.format(key_count + 1)
            b10 = urandom(b2)
            b11 = ''
            for char in b10:
                b11 += fonk1(char)
            output_file.write(b9 + ' ' + b11)
            if key_count < a1 - 1:
                output_file.write('\n')
        print('Key written to', b5)