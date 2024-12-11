import random
import pickle
import array
import re
from base.general import is_prime
class class1:
    def fonk1(self, filename):
        with open(filename, 'rb') as file:
            b1 = file.read()
        return b1
    def fonk2(self, filename):
        with open(filename, 'rb') as file:
            b2 = pickle.load(file)
        return b2
    def fonk3(self, filename, b1):
        with open(filename, 'wb') as file:
            file.write(b1)
    def fonk4(self, filename, b1):
        with open(filename, 'wb') as file:
            pickle.dump(b1, file)
    def fonk5(self, b13):
        if not is_prime(b13):
            return "P is not prime"
        b3 = random.randrange(b13)
        b4 = random.randrange(1, b13 - 2)
        b5 = pow(b3, b4, b13)
        b6 = [b5, b3, b13]
        b7 = [b4, b13]
        self.fonk4("key.pub", b6)
        self.fonk4("key.pri", b7)
    def fonk6(self, filename, b6, b7):
        b8 = self.fonk1(filename)
        b9 = list(b8)
        b10 = list(map(int, b8))
        b11 = self.fonk2(b6)
        b12 = self.fonk2(b7)
        b5, b3, b13 = b11
        b4, b14 = b12
        b15 = random.randrange(1, b13 - 2)
        b16 = []
        for a1 in range(len(b10)):
            b17 = pow(b3, b15, b13)
            b18 = (pow(b5, b15, b13) * b10[a1]) % b13
            b16.append(b17)
            b16.append(b18)
        print(b10)
        b19 = re.findall('.\w+', filename)
        print(b19)
        self.fonk4("cipher" + b19[-1], b16)
        print(b16)
    def fonk7(self, filename, b6, b7):
        b16 = self.fonk2(filename)
        b11 = self.fonk2(b6)
        b12 = self.fonk2(b7)
        b5, b3, b13 = b11
        b4, b14 = b12
        b10 = []
        a1 = 0
        while a1 < len(b16):
            b20 = b13 - 1 - b4
            b21 = pow(b16[a1], b20, b13)
            b22 = (b21 * b16[a1 + 1]) % b13
            b10.append(b22)
            a1 += 2
        b19 = re.findall('.\w+', filename)
        self.fonk3("out" + b19[-1], array.array('B', b10).tobytes())
        print(b10)
if b23 = = '__main__':
    b24 = class1()
    b24.fonk5(233)
    b17 = b24.fonk2("key.pub")
    b18 = b24.fonk2("key.pri")
    b24.fonk6("plain.txt", "key.pub", "key.pri")
    b24.fonk7("cipher.txt", "key.pub", "key.pri")