import sys
from datetime import datetime
from b2 import Rsa
sys.setrecursionlimit(5000)
def fonk1():
    b1 = "The information security is of great importance to ensure the privacy of communications"
    b2 = Rsa()
    b3 = datetime.now()
    b2.key_gen(b1 = b1, digits=30)
    b4 = (datetime.now() - b3).total_seconds()
    print(f'Message: {b2._message}\n')
    print(f'Public Key: {b2._public_key}\n')
    print(f'Private Key: {b2._private_key}\n')
    print(f'Prime p: {b2._p}')
    print(f'Prime q: {b2._q}\n')
    print(f'Encoded Message: {b2._encode}\n')
    print(f'Decoded Message: {b2._decode}\n')
    print(f'Performance: {b2._performance}')
    print(f'Total Time for Key Generation: {b4} seconds')
if b5 = = "__main__":
    fonk1()