import random
import pickle
import array
import re
from sympy import isprime
class class1:
    def fonk1(self):
        pass
    @staticmethod
    def fonk2(filename):
        with open(filename, 'rb') as file:
            b1 = file.read()
        return b1
    @staticmethod
    def fonk3(filename):
        with open(filename, 'rb') as file:
            b2 = pickle.load(file)
        return b2
    @staticmethod
    def fonk4(filename, b1):
        with open(filename, 'wb') as file:
            file.write(b1)
    @staticmethod
    def fonk5(filename, b1):
        with open(filename, 'wb') as file:
            pickle.dump(b1, file)
    def fonk6(self, b11):
        if not isprime(b11):
            return "P is not prime"
        b3 = random.randrange(2, b11)
        b4 = random.randrange(1, b11 - 1)
        b5 = pow(b3, b4, b11)
        b6 = [b5, b3, b11]
        b7 = [b4, b11]
        self.fonk5("key.pub", b6)
        self.fonk5("key.pri", b7)
        return b6, b7
    def fonk7(self, filename, b6):
        b8 = self.fonk2(filename)
        b9 = list(b8)
        b10 = self.fonk3(b6)
        b5, b3, b11 = b10
        b12 = random.randrange(1, b11 - 1)
        b13 = []
        for plain_int in b9:
            b14 = pow(b3, b12, b11)
            b15 = (pow(b5, b12, b11) * plain_int) % b11
            b13.extend([b14, b15])
        b16 = re.compile(r'\.\w+').findall(filename)
        self.fonk5(f"cipher{b16[-1]}", b13)
        return b13
    def fonk8(self, filename, b7):
        b13 = self.fonk3(filename)
        b17 = self.fonk3(b7)
        b4, b11 = b17
        b9 = []
        for i in range(0, len(b13), 2):
            b14, b15 = b13[i], b13[i + 1]
            b18 = pow(b14, b11 - 1 - b4, b11)
            b19 = (b18 * b15) % b11
            b9.append(b19)
        b16 = re.compile(r'\.\w+').findall(filename)
        self.fonk4(f"out{b16[-1]}", array.array('B', b9).tobytes())
        return b9
if b20 = = '__main__':
    b21 = class1()
    b11 = 233
    b6, b7 = b21.fonk6(b11)
    print("Public Key:", b6)
    print("Private Key:", b7)
    b21.fonk7("plain.txt", "key.pub")
    b21.fonk8("cipher.txt", "key.pri")