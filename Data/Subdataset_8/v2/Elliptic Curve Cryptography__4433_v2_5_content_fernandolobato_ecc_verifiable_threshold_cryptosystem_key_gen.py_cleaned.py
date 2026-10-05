import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
num_keys = 50
directory = 'keys/'
if not os.path.exists(directory):
    os.makedirs(directory)
secret_keys = [threshold.generate_key() for _ in range(num_keys)]
public_keys = [key * SECP256k1.generator for key in secret_keys]
def big_number(num):
    return 'new BigNumber(\'{}\')'.format(num)
def stringify_point(point):
    return big_number(point.x()) + ',' + big_number(point.y())
with open(os.path.join(directory, 'private.js'), 'w') as file:
    secret_keys_js = ','.join([big_number(key) for key in secret_keys])
    file.write('var secretKeys = [{}];'.format(secret_keys_js))
with open(os.path.join(directory, 'private.txt'), 'w') as file:
    file.write('\n'.join(map(str, secret_keys)))
with open(os.path.join(directory, 'public.js'), 'w') as file:
    public_keys_js = ','.join(['[{}]'.format(stringify_point(key)) for key in public_keys])
    file.write('var publicKeys = [{}];'.format(public_keys_js))
with open(os.path.join(directory, 'public.txt'), 'w') as file:
    file.write('\n'.join(['{},{}'.format(key.x(), key.y()) for key in public_keys]))