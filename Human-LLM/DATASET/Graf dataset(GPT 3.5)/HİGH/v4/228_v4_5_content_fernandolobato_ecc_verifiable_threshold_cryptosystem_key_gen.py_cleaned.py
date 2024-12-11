import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
a1 = 50
b1 = 'keys/'
if not os.path.exists(b1):
    os.makedirs(b1)
b2 = [threshold.generate_key() for _ in range(a1)]
b3 = [key * SECP256k1.generator for key in b2]
def fonk1(num):
    return 'new BigNumber(\'{}\')'.format(num)
def fonk2(point):
    return fonk1(point.x()) + ',' + fonk1(point.y())
with open(os.path.join(b1, 'private.js'), 'w') as file:
    b4 = ','.join([fonk1(k) for k in b2])
    file.write('var b5 = [{}];'.format(b4))
with open(os.path.join(b1, 'private.txt'), 'w') as file:
    file.write('\n'.join(map(str, b2)))
with open(os.path.join(b1, 'public.js'), 'w') as file:
    b6 = ','.join(['[{}]'.format(fonk2(k)) for k in b3])
    file.write('var b7 = [{}];'.format(b6))
with open(os.path.join(b1, 'public.txt'), 'w') as file:
    file.write('\n'.join(['{},{}'.format(k.x(), k.y()) for k in b3]))