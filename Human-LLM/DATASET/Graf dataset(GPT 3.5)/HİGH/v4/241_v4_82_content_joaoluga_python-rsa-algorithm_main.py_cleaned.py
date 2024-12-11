import sys
from datetime import datetime
from rsa import Rsa
sys.setrecursionlimit(5000)
b1 = "The information security is of great importance to ensure the privacy of communications"
b2 = Rsa()
b3 = datetime.now()
b2.key_gen(b1 = b1, digits=30)
b4 = (datetime.now() - b3).total_seconds()
print('Message: {}\n'.format(b2._message))
print('Public key: {}\n'.format(b2._public_key))
print('Private Key: {}\n'.format(b2._private_key))
print('p: {}'.format(b2._p))
print('q: {}\n\n'.format(b2._q))
print('Encode: {}\n\n'.format(b2._encode))
print('Decode: {}'.format(b2._decode))
print('Performance: {}'.format(b2._performance))
print('Total seconds: {}'.format(b4))