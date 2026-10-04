import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
def fonk1(num):
    return f"new BigNumber('{num}')"
def fonk2(point):
    return f"{fonk1(point.x())},{fonk1(point.y())}"
def fonk3():
    a1 = 50
    b1 = 'keys/'
    if not os.path.exists(b1):
        os.makedirs(b1)
    b2 = [threshold.generate_key() for _ in range(a1)]
    b3 = [k * SECP256k1.generator for k in b2]
    with open(os.path.join(b1, 'private.js'), 'w') as private_js_file:
        b4 = 'var secKeys = [{}]'.format(''.join([fonk1(k) + ',' for k in b2])[:-1])
        private_js_file.write(b4)
    with open(os.path.join(b1, 'public.js'), 'w') as public_js_file:
        b5 = 'var pubKeys = [{}]'.format(''.join([f"[{fonk2(k)}]," for k in b3])[:-1])
        public_js_file.write(b5)
    with open(os.path.join(b1, 'private.txt'), 'w') as private_txt_file:
        b6 = ''.join([str(k) + '\n' for k in b2])
        private_txt_file.write(b6)
    with open(os.path.join(b1, 'public.txt'), 'w') as public_txt_file:
        b7 = ''.join([f"{k.x()},{k.y()}\n" for k in b3])
        public_txt_file.write(b7)
if b8 = = "__main__":
    fonk3()