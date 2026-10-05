import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
num_keys = 50
directory = 'keys/'
if not os.path.exists(directory):
    os.makedirs(directory)
secret_keys = [threshold.generate_key() for _ in range(num_keys)]
public_keys = [key * SECP256k1.generator for key in secret_keys]
def big_number_string(num):
    return 'new BigNumber(\'{}\')'.format(num)
def point_to_string(point):
    return big_number_string(point.x()) + ',' + big_number_string(point.y())
with open(os.path.join(directory, 'private.js'), 'w') as file:
    secret_keys_js = ','.join([big_number_string(k) for k in secret_keys])
    file.write('var secretKeys = [{}];'.format(secret_keys_js))
with open(os.path.join(directory, 'private.txt'), 'w') as file:
    file.write('\n'.join(map(str, secret_keys)))
with open(os.path.join(directory, 'public.js'), 'w') as file:
    public_keys_js = ','.join(['[{}]'.format(point_to_string(k)) for k in public_keys])
    file.write('var pubKeys = [{}];'.format(public_keys_js))
with open(os.path.join(directory, 'public.txt'), 'w') as file:
    file.write('\n'.join(['{},{}'.format(k.x(), k.y()) for k in public_keys]))
"