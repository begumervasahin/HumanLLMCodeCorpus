import random
import pickle
import array
import re
from base.general import is_prime
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
    def fonk6(self, b9):
        if not is_prime(b9):
            raise ValueError("P is not prime")
        b1 = random.randrange(2, b9)
        b2 = random.randrange(1, b9 - 1)
        b3 = pow(b1, b2, b9)
        b4 = [b3, b1, b9]
        b5 = [b2, b9]
        self.fonk5("key.pub", b4)
        self.fonk5("key.pri", b5)
    def fonk7(self, filename, b4, b5):
        b6 = self.fonk2(filename)
        b7 = list(b6)
        b8 = self.fonk3(b4)
        b3, b1, b9 = b8
        b10 = random.randrange(1, b9 - 1)
        b11 = []
        for plain_int in b7:
            b12 = pow(b1, b10, b9)
            b13 = (pow(b3, b10, b9) * plain_int) % b9
            b11.extend([b12, b13])
        b14 = re.compile(r'\.\w+').findall(filename)
        b15 = f"cipher{b14[-1]}"
        self.fonk5(b15, b11)
    def fonk8(self, filename, b4, b5):
        b11 = self.fonk3(filename)
        b16 = self.fonk3(b5)
        b2, b9 = b16
        b7 = []
        for i in range(0, len(b11), 2):
            b12, b13 = b11[i], b11[i + 1]
            b17 = pow(b12, b9 - 1 - b2, b9)
            b18 = (b17 * b13) % b9
            b7.append(b18)
        b14 = re.compile(r'\.\w+').findall(filename)
        b19 = f"out{b14[-1]}"
        self.fonk4(b19, array.array('B', b7).tobytes())
if b20 = = '__main__':
    b21 = class1()
    b9 = 233
    b21.fonk6(b9)
    b21.fonk7("plain.txt", "key.pub", "key.pri")
    b21.fonk8("cipher.txt", "key.pub", "key.pri")