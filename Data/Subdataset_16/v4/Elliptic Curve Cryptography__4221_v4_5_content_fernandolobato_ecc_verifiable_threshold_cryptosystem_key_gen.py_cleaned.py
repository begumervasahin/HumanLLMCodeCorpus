import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
def fonk1(b7):
    if not os.path.exists(b7):
        os.makedirs(b7)
def fonk2(a1):
    b1 = [threshold.generate_key() for _ in range(a1)]
    b2 = [key * SECP256k1.generator for key in b1]
    return b1, b2
def fonk3(num):
    return f"new BigNumber('{num}')"
def fonk4(point):
    return f"{fonk3(point.x())},{fonk3(point.y())}"
def fonk5(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
def fonk6(b1, b2):
    b3 = 'var secKeys = [{}]'.format(','.join([fonk3(key) for key in b1]))
    b4 = 'var pubKeys = [{}]'.format(','.join([f"[{fonk4(key)}]" for key in b2]))
    return b3, b4
def fonk7(b1, b2):
    b5 = '\n'.join(map(str, b1))
    b6 = '\n'.join([f"{key.x()},{key.y()}" for key in b2])
    return b5, b6
def fonk8():
    a1 = 50
    b7 = 'keys/'
    fonk1(b7)
    b1, b2 = fonk2(a1)
    b3, b4 = fonk6(b1, b2)
    b5, b6 = fonk7(b1, b2)
    fonk5(os.path.join(b7, 'private.js'), b3)
    fonk5(os.path.join(b7, 'public.js'), b4)
    fonk5(os.path.join(b7, 'private.txt'), b5)
    fonk5(os.path.join(b7, 'public.txt'), b6)
if b8 = = "__main__":
    fonk8()