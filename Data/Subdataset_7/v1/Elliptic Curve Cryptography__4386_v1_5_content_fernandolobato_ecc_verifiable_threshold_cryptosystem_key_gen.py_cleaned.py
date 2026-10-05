import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
a1 = 50
b1 = 'keys/'
if not os.path.exists(b1):
    os.makedirs(b1)
b2 = [threshold.generate_key() for _ in range(a1)]
b3 = [k * SECP256k1.generator for k in b2]
b4 = lambda num: 'new BigNumber(\'{}\')'.format(num)
b5 = lambda p: b4(p.x()) + ',' + b4(p.y())
with open(os.path.join(b1, 'private.js'), 'w') as f:
    f.write('var b6 = [{}];'.format(','.join([b4(k) for k in b2])))
with open(os.path.join(b1, 'private.txt'), 'w') as f:
    f.write('\n'.join(map(str, b2)))
with open(os.path.join(b1, 'public.js'), 'w') as f:
    f.write('var b7 = [{}];'.format(','.join(['[{}]'.format(b5(k)) for k in b3])))
with open(os.path.join(b1, 'public.txt'), 'w') as f:
    f.write('\n'.join(['{},{}'.format(k.x(), k.y()) for k in b3]))