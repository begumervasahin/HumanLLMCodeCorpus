import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
def fonk1(num):
    return f"new BigNumber('{num}')"
def fonk2(point):
    return f"{fonk1(point.x())},{fonk1(point.y())}"
def fonk3(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
def fonk4(a1):
    b1 = [threshold.generate_key() for _ in range(a1)]
    b2 = [key * SECP256k1.generator for key in b1]
    return b1, b2
def fonk5():
    a1 = 50
    b3 = 'keys/'
    if not os.path.exists(b3):
        os.makedirs(b3)
    b1, b2 = fonk4(a1)
    b4 = 'var secKeys = [{}]'.format(','.join([fonk1(key) for key in b1]))
    b5 = 'var pubKeys = [{}]'.format(','.join([f"[{fonk2(key)}]" for key in b2]))
    b6 = '\n'.join(map(str, b1))
    b7 = '\n'.join([f"{key.x()},{key.y()}" for key in b2])
    fonk3(os.path.join(b3, 'private.js'), b4)
    fonk3(os.path.join(b3, 'public.js'), b5)
    fonk3(os.path.join(b3, 'private.txt'), b6)
    fonk3(os.path.join(b3, 'public.txt'), b7)
if b8 = = "__main__":
    fonk5()