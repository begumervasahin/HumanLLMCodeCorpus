import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
a1 = 50
b1 = 'keys/'
if not os.path.exists(b1):
    os.makedirs(b1)
b2 = [threshold.generate_key() for i in range(a1)];
b3 = list(map(lambda x: x * SECP256k1.generator , b2))
b4 = lambda num: 'new BigNumber(\'{}\')'.format(num)
b5 = lambda p: b4(p.x()) + ',' + b4(p.y())
open(os.path.join(b1, 'private.js'), 'w').write('var b6 = [{}]'.format(''.join([ b4(k) + ',' for k in b2])[:-1]))
open(os.path.join(b1, 'public.js'), 'w').write('var b7 = [{}]'.format(''.join([ '[{}],'.format(b5(k)) for k in b3])[:-1]))
open(os.path.join(b1, 'private.txt'), 'w').write('{}'.format(''.join([ str(k) + '\n' for k in b2])))
open(os.path.join(b1, 'public.txt'), 'w').write('{}'.format(''.join([ '{},{}\n'.format(k.x(), k.y()) for k in b3])[:-1]))