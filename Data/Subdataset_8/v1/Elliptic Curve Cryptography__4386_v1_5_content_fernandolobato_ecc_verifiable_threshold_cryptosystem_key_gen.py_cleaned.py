import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
num_keys = 50
directory = 'keys/'
if not os.path.exists(directory):
    os.makedirs(directory)
s_keys = [threshold.generate_key() for _ in range(num_keys)]
p_keys = [k * SECP256k1.generator for k in s_keys]
big_num = lambda num: 'new BigNumber(\'{}\')'.format(num)
stringify_point = lambda p: big_num(p.x()) + ',' + big_num(p.y())
with open(os.path.join(directory, 'private.js'), 'w') as f:
    f.write('var secKeys = [{}];'.format(','.join([big_num(k) for k in s_keys])))
with open(os.path.join(directory, 'private.txt'), 'w') as f:
    f.write('\n'.join(map(str, s_keys)))
with open(os.path.join(directory, 'public.js'), 'w') as f:
    f.write('var pubKeys = [{}];'.format(','.join(['[{}]'.format(stringify_point(k)) for k in p_keys])))
with open(os.path.join(directory, 'public.txt'), 'w') as f:
    f.write('\n'.join(['{},{}'.format(k.x(), k.y()) for k in p_keys]))