import sys
from datetime import datetime
class Rsa:
    def __init__(self):
        pass
    def key_gen(self, message, digits):
        pass
    def encode(self):
        pass
    def decode(self):
        pass
message = "The information security is of great importance to ensure the privacy of communications"
rsa_code = Rsa()
start = datetime.now()
rsa_code.key_gen(message=message, digits=30)
total_time = (datetime.now() - start).total_seconds()
print('Message: {}\n'.format(message))
print('Public key: {}\n'.format(rsa_code._public_key))
print('Private Key: {}\n'.format(rsa_code._private_key))
print('p: {}'.format(rsa_code._p))
print('q: {}\n\n'.format(rsa_code._q))
print('Encode: {}\n\n'.format(rsa_code.encode()))
print('Decode: {}'.format(rsa_code.decode()))
print('Total seconds: {}'.format(total_time))