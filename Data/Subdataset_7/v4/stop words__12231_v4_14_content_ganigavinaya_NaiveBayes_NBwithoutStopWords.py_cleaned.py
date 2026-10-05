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
        for each_file class2 b11:
            with io.open(b10+"/"+each_file, 'r', b13 = 'iso-8859-1') as f:
                b14 = f.readlines()
                for line class2 b14:
                    b15 = re.sub("[^a-zA-Z\s]", "", line).lower().split()
                    for word class2 b15:
                        if word class2 b12:
                            b12[word] += 1
                        else:
                            b12[word] = 1
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
        for word class2 self.b5:
            b18 = self.b6.get(word, 0) + 1
            b19 = self.b7.get(word, 0) + 1
            self.b9[word] = [b18 / self.a3, b19 / self.a4]
    def fonk4(self):
        self.fonk2(self.a1)
        self.fonk2(self.a2)
        self.b5 = set(list(self.b6.keys()) + list(self.b7.keys()))
    def fonk5(self):
        b20 = len(os.listdir(self.b1))
        b21 = len(os.listdir(self.b2))
        b22 = b20 + b21
        self.b8[self.a1] = b20 / b22
        self.b8[self.a2] = b21 / b22
        self.fonk3()
    def fonk6(self, b26):
        b23 = {self.a1: 0, self.a2: 0}
        a6 = 0
        b24 = os.listdir(b26)
        for each_file class2 b24:
            with io.open(b26+"/"+each_file, 'r', b13 = 'iso-8859-1') as f:
                b25 = f.read()
                b15 = re.sub("[^a-zA-Z\s]", "", b25).lower()
                b16 = set(b15.split())
                for each_class class2 b23.keys():
                    b23[each_class] = math.log(self.b8[each_class], 2)
                    for word class2 b16:
                        if word class2 self.b5:
                            b23[each_class] += math.log(self.b9[word][each_class], 2)
                if b23[self.a1] > b23[self.a2]:
                    if b26 = = self.b3:
                        a6 += 1
                else:
                    if b26 = = self.b4:
                        a6 += 1
        return a6
    def fonk7(self):
        b27 = self.fonk6(self.b3)
        b28 = os.listdir(self.b3)
        b29 = (b27 / len(b28)) * 100
        print("Ham test b30 = ", b29)
        b31 = os.listdir(self.b4)
        b32 = self.fonk6(self.b4)
        b33 = (b32 / len(b31)) * 100
        print("Spam test b30 = ", b33)
        b34 = ((b27 + b32) / (len(b31) + len(b28))) * 100
        print("Total test b30 = ", b34)
