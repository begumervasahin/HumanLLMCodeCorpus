def fonk1(b6, key, alphabet):
    b1 = []
    b2 = len(alphabet)
    for p, k in zip(b6, key):
        b3 = alphabet.index(p)
        b4 = alphabet.index(k)
        b5 = (b3 + b4) % b2
        b1.append(alphabet[b5])
    return ''.join(b1)
def fonk2(b1, key, alphabet):
    b6 = []
    b2 = len(alphabet)
    for c, k in zip(b1, key):
        b5 = alphabet.index(c)
        b4 = alphabet.index(k)
        b3 = (b5 - b4) % b2
        b6.append(alphabet[b3])
    return ''.join(b6)
import unittest
from otp import encrypt, decrypt
class class1(unittest.TestCase):
    def fonk3(self):
        self.assertEqual("EQNVZ", fonk1("HELLO", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    def fonk4(self):
        self.assertEqual("HELLO", fonk2("EQNVZ", "XMCKL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
if b7 = = '__main__':
    unittest.main()