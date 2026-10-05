import os
import re
import io
import math
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.a1 = 0
        self.a2 = 1
        self.b5 = []
        self.b6 = {}
        self.a3 = 0
        self.b7 = {}
        self.a4 = 0
        self.b8 = {}
        self.b9 = {}
    def fonk2(self, b17):
        b10 = self.b1 if b17 == self.a1 else self.b2
        b11 = os.listdir(b10)
        b12 = {}
        a5 = 0
        for file_name in b11:
            with io.open(os.b10.join(b10, file_name), 'r', b13 = 'iso-8859-1') as f:
                b14 = f.readlines()
                for line in b14:
                    b15 = re.sub("[^a-zA-Z\s]", "", line).lower().split()
                    for word in b15:
                        b12[word] = b12.get(word, 0) + 1
                        a5 += 1
        b16 = list(b12.keys())
        a5 += len(b16)
        if b17 = = self.a1:
            self.b6 = b12
            self.a3 = a5
        else:
            self.b7 = b12
            self.a4 = a5
    def fonk3(self):
        for word in self.b5:
            b18 = self.b6.get(word, 0) + 1
            b19 = self.b7.get(word, 0) + 1
            self.b9[word] = [b18 / self.a3, b19 / self.a4]
    def fonk4(self):
        b20 = len(os.listdir(self.b1))
        b21 = len(os.listdir(self.b2))
        b22 = b20 + b21
        self.b8[self.a1] = b20 / b22
        self.b8[self.a2] = b21 / b22
        self.fonk2(self.a1)
        self.fonk2(self.a2)
        self.b5 = set(self.b6.keys()).union(self.b7.keys())
        self.fonk3()
    def fonk5(self, b10):
        a6 = 0
        b23 = os.listdir(b10)
        for file_name in b23:
            with io.open(os.b10.join(b10, file_name), 'r', b13 = 'iso-8859-1') as f:
                b24 = f.read()
                b15 = re.sub("[^a-zA-Z\s]", "", b24).lower().split()
                b25 = set(b15)
                b26 = {self.a1: math.log2(self.b8[self.a1]),
                         self.a2: math.log2(self.b8[self.a2])}
                for word in b25:
                    if word in self.b5:
                        b26[self.a1] += math.log2(self.b9[word][self.a1])
                        b26[self.a2] += math.log2(self.b9[word][self.a2])
                b27 = max(b26, key=b26.get)
                if b27 = = self.a1 and b10 == self.b3:
                    a6 += 1
                elif b27 = = self.a2 and b10 == self.b4:
                    a6 += 1
        return a6
    def fonk6(self):
        b28 = self.fonk5(self.b3)
        b29 = (b28 / len(os.listdir(self.b3))) * 100
        print("Ham test b30 = ", b29)
        b31 = self.fonk5(self.b4)
        b32 = (b31 / len(os.listdir(self.b4))) * 100
        print("Spam test b30 = ", b32)
        b33 = ((b28 + b31) / (len(os.listdir(self.b3)) + len(os.listdir(self.b4)))) * 100
        print("Total test b30 = ", b33)
