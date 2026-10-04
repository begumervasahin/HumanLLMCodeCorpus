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
            return file.read()
    @staticmethod
    def fonk3(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    @staticmethod
    def fonk4(filename, data):
        with open(filename, 'wb') as file:
            file.write(data)
    @staticmethod
    def fonk5(filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    def fonk6(self, b8):
        if not isprime(b8):
            raise ValueError("P is not prime")
        b1 = random.randrange(2, b8)
        b2 = random.randrange(1, b8 - 1)
        b3 = pow(b1, b2, b8)
        b4 = [b3, b1, b8]
        b5 = [b2, b8]
        self.fonk5("key.pub", b4)
        self.fonk5("key.pri", b5)
        return b4, b5
    def fonk7(self, filename, b4):
        b6 = self.fonk2(filename)
        b7 = list(b6)
        b3, b1, b8 = self.fonk3(b4)
        b9 = random.randrange(1, b8 - 1)
        b10 = []
        for plain_int in b7:
            b11 = pow(b1, b9, b8)
            b12 = (pow(b3, b9, b8) * plain_int) % b8
            b10.extend([b11, b12])
        b13 = re.compile(r'\.\w+').findall(filename)
        b14 = f"cipher{b13[-1]}"
        self.fonk5(b14, b10)
        return b10
    def fonk8(self, filename, b5):
        b10 = self.fonk3(filename)
        b2, b8 = self.fonk3(b5)
        b7 = []
        for i in range(0, len(b10), 2):
            b11, b12 = b10[i], b10[i + 1]
            b15 = pow(b11, b8 - 1 - b2, b8)
            b16 = (b15 * b12) % b8
            b7.append(b16)
        b13 = re.compile(r'\.\w+').findall(filename)
        b17 = f"out{b13[-1]}"
        self.fonk4(b17, array.array('B', b7).tobytes())
        return b7
if b18 = = '__main__':
    b19 = class1()
    b8 = 233
    b4, b5 = b19.fonk6(b8)
    print("Public Key:", b4)
    print("Private Key:", b5)
    b19.fonk7("plain.txt", "key.pub")
    b19.fonk8("cipher.txt", "key.pri")