import sys
from datetime import datetime
class class1:
    def fonk1(self):
        pass
    def fonk2(self, b1, digits):
        pass
    def fonk3(self):
        pass
    def fonk4(self):
        pass
b1 = "The information security is of great importance to ensure the privacy of communications"
b2 = class1()
b3 = datetime.now()
b2.fonk2(b1 = b1, digits=30)
b4 = (datetime.now() - b3).total_seconds()
print('Message: {}\n'.format(b1))
print('Public key: {}\n'.format(b2._public_key))
print('Private Key: {}\n'.format(b2._private_key))
print('p: {}'.format(b2._p))
print('q: {}\n\n'.format(b2._q))
print('Encode: {}\n\n'.format(b2.fonk3()))
print('Decode: {}'.format(b2.fonk4()))
print('Total seconds: {}'.format(b4))