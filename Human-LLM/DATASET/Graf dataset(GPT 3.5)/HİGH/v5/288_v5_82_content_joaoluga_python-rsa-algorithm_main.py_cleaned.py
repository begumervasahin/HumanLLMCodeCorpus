import sys
from datetime import datetime
from b1 import Rsa
def fonk1(b3, digits):
    b1 = Rsa()
    b2 = datetime.now()
    b1.key_gen(b3 = b3, digits=digits)
    b4 = (datetime.now() - b2).total_seconds()
    return b1, b4
def fonk2(b1):
    print('Message: {}\n'.format(b1._message))
    print('Public Key: {}\n'.format(b1._public_key))
    print('Private Key: {}\n'.format(b1._private_key))
    print('p: {}'.format(b1._p))
    print('q: {}\n'.format(b1._q))
    print('Encode: {}\n'.format(b1._encode))
    print('Decode: {}\n'.format(b1._decode))
    print('Performance: {}\n'.format(b1._performance))
def fonk3():
    sys.setrecursionlimit(5000)
    b3 = "The information security is of great importance to ensure the privacy of communications"
    b1, b4 = fonk1(b3=b3, digits=30)
    fonk2(b1)
    print('Total seconds: {}'.format(b4))
if b5 = = "__main__":
    fonk3()