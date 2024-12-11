import os
import sys
import getopt
import logging
b1 = logging.getLogger()
b1.setLevel(logging.INFO)
b2 = logging.StreamHandler()
b2.setLevel(logging.DEBUG)
b1.addHandler(b2)
a1 = 2048
def fonk1(plaintext, key):
    if len(plaintext) != len(key):
        raise IndexError('Plaintext and key should be the same size')
    return bytes(map(lambda x, y: x ^ y, plaintext, key))
if b3 = = '__main__':
    try:
        opts, b4 = getopt.gnu_getopt(sys.argv[1:], 'db:', ['decrypt', 'buffer-size='])
    except getopt.GetoptError as err:
        b1.error('Error getting command line options: %s', err.msg)
        sys.exit(2)
    b5 = a1
    b6 = False
    for opt, arg in opts:
        if opt in ('-d', '--decrypt'):
            b6 = True
        elif opt in ('-b', '--buffer-size'):
            b5 = int(arg)
    for filename in b4:
        if not b6:
            b7 = filename + '.otp'
            b8 = filename + '.otpk'
            with open(filename, 'rb') as fplain, open(b7, 'wb') as fcipher, open(b8, 'wb') as fkey:
                while True:
                    b9 = fplain.read(b5)
                    if not b9:
                        break
                    b10 = os.urandom(len(b9))
                    fcipher.write(fonk1(b9, b10))
                    fkey.write(b10)
        else:
            b11 = os.path.splitext(filename)[0]
            b8 = b11 + '.otpk'
            with open(filename, 'rb') as fcipher, open(b11, 'wb') as fplain, open(b8, 'rb') as fkey:
                while True:
                    b12 = fcipher.read(b5)
                    if not b12:
                        break
                    fplain.write(fonk1(b12, fkey.read(len(b12)))))