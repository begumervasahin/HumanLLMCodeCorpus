import random
import pickle
import array
import re
from base.general import is_prime
class class1:
    def fonk1(self):
        pass
    def fonk2(self, filename):
        with open(filename, 'rb') as file:
            b1 = file.read()
        return b1
    def fonk3(self, filename):
        with open(filename, 'rb') as file:
            b2 = pickle.load(file)
        return b2
    def fonk4(self, filename, b1):
        with open(filename, 'wb') as file:
            file.write(b1)
    def fonk5(self, filename, b1):
        with open(filename, 'wb') as file:
            pickle.dump(b1, file)
    def fonk6(self, b13):
        if not is_prime(b13):
            return "P is not prime"
        b3 = random.randrange(b13)
        b4 = random.randrange(1, b13 - 2)
        b5 = (b3 ** b4) % b13
        b6 = [b5, b3, b13]
        b7 = [b4, b13]
        self.fonk5("key.pub", b6)
        self.fonk5("key.pri", b7)
    def fonk7(self, filename, b6, b7):
        b8 = self.fonk2(filename)
        b9 = list(b8)
        b10 = list(map(int, b8))
        b11 = self.fonk3(b6)
        b12 = self.fonk3(b7)
        b5, b3, b13 = b11
        b4 = b12[0]
        b14 = random.randrange(1, b13 - 2)
        b15 = []
        for a1 in range(len(b10)):
            b16 = (b3 ** b14) % b13
            b17 = ((b5 ** b14) * b10[a1]) % b13
            b15.append(b16)
            b15.append(b17)
        print(b10)
        b18 = re.compile('.\w+').findall(filename)
        print(b18)
        self.fonk5("cipher" + b18[-1], b15)
        print(b15)
    def fonk8(self, filename, b6, b7):
        b15 = self.fonk3(filename)
        b11 = self.fonk3(b6)
        b12 = self.fonk3(b7)
        b5, b3, b13 = b11
        b4 = b12[0]
        b10 = []
        a1 = 0
        while a1 < len(b15):
            b19 = b13 - 1 - b4
            b20 = (b15[a1] ** b19) % b13
            b21 = (b20 * b15[a1 + 1]) % b13
            b10.append(b21)
            a1 += 2
        b18 = re.compile('.\w+').findall(filename)
        self.fonk4("out" + b18[-1], array.array('B', b10).tobytes())
        print(b10)
if b22 = = '__main__':
    b23 = class1()
    b23.fonk6(233)
    b16 = b23.fonk3("key.pub")
    b17 = b23.fonk3("key.pri")
    b23.fonk7("plain.txt", "key.pub", "key.pri")
    b23.fonk8("cipher.txt", "key.pub", "key.pri")