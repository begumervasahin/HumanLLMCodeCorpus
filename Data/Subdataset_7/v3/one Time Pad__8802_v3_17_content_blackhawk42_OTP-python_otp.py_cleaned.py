import os
import sys
import getopt
import logging
logging.basicConfig(b1 = logging.INFO, format='%(message)s')
b2 = logging.getLogger()
a1 = 2048
def fonk1(plaintext, key):
    if len(plaintext) != len(key):
        raise IndexError('Plaintext and key should be the same size')
    return bytes(map(lambda x, y: x ^ y, plaintext, key))
def fonk2(b10, b11):
    for filename in b10:
        b3 = filename + '.otp'
        b4 = filename + '.otpk'
        with open(filename, 'rb') as fplain, open(b3, 'wb') as fcipher, open(b4, 'wb') as fkey:
            while True:
                b5 = fplain.read(b11)
                if not b5:
                    break
                b6 = os.urandom(len(b5))
                fcipher.write(fonk1(b5, b6))
                fkey.write(b6)
def fonk3(b10, b11):
    for filename in b10:
        b7 = os.path.splitext(filename)[0]
        b4 = b7 + '.otpk'
        with open(filename, 'rb') as fcipher, open(b7, 'wb') as fplain, open(b4, 'rb') as fkey:
            while True:
                b8 = fcipher.read(b11)
                if not b8:
                    break
                fplain.write(fonk1(b8, fkey.read(len(b8)))))
if b9 = = '__main__':
    try:
        opts, b10 = getopt.getopt(sys.argv[1:], 'db:', ['decrypt', 'buffer-size='])
    except getopt.GetoptError as err:
        b2.error(f'Error getting command line options: {err}')
        sys.exit(2)
    b11 = a1
    b12 = False
    for opt, arg in opts:
        if opt in ('-d', '--decrypt'):
            b12 = True
        elif opt in ('-b', '--buffer-size'):
            b11 = int(arg)
    if not b12:
        fonk2(b10, b11)
    else:
        fonk3(b10, b11)