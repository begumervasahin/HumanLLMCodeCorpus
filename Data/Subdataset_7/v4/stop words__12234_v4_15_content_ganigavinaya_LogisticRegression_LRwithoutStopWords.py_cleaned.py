import os
import io
import re
import numpy as np
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = {}
        self.b6 = []
        self.a1 = 0.0001
        self.a2 = 5
        self.b7 = []
    def fonk2(self):
        self.fonk4()
        self.fonk6(self.b1, 1.0)
        self.fonk6(self.b2, 0.0)
    def fonk3(self, path, b15):
        with io.open(path, 'r', b8 = 'iso-8859-1') as f:
            b9 = f.readlines()
            for line in b9:
                b10 = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in b10:
                    if word in b15:
                        b15[word] += 1
                    else:
                        b15[word] = 1
    def fonk4(self):
        b11 = {}
        self.fonk5(self.b1, b11)
        b12 = {}
        self.fonk5(self.b2, b12)
        self.b6 = set(b11.keys()).union(b12.keys())
        for word in self.b6:
            self.b5[word] = 0.0
    def fonk5(self, b27, b15):
        b13 = os.listdir(b27)
        for file_name in b13:
            b14 = os.path.join(b27, file_name)
            self.fonk3(b14, b15)
    def fonk6(self, b27, classification):
        b13 = os.listdir(b27)
        for file_name in b13:
            b14 = os.path.join(b27, file_name)
            b15 = {}
            self.fonk3(b14, b15)
            self.b7.append({'fileName': b14, 'token': b15, 'class': classification})
    def fonk7(self):
        for _ in range(500):
            self.fonk8()
            self.fonk10()
    def fonk8(self):
        for b7 in self.b7:
            b16 = b7["token"]
            a3 = 1
            for token in b16:
                a3 += b16[token] * self.b5[token]
            b7["error"] = self.fonk9(a3)
    def fonk9(self, x):
        b17 = 1 + np.exp(-x)
        return 1 / b17
    def fonk10(self):
        for token in self.b5.keys():
            a4 = 0
            for b7 in self.b7:
                b16 = b7["token"]
                b18 = b7["class"]
                if token in b16:
                    b19 = b18 - b7["error"]
                    a4 += b16[token] * b19
            self.b5[token] += ((a4 * self.a1) - (self.a1 * self.a2 * self.b5[token]))
    def fonk11(self):
        b20 = self.fonk12(self.b3, threshold=0.5)
        b21 = self.fonk12(self.b4, threshold=0.5)
        b22 = (b20 / len(os.listdir(self.b3))) * 100
        b23 = (b21 / len(os.listdir(self.b4))) * 100
        b24 = ((b20 + b21) / (len(os.listdir(self.b3)) + len(os.listdir(self.b4)))) * 100
        print("Ham accuracy is ", b22)
        print("Spam accuracy is ", b23)
        print("Total accuracy is ", b24)
    def fonk12(self, b27, threshold):
        a5 = 0
        b13 = os.listdir(b27)
        for file_name in b13:
            b14 = os.path.join(b27, file_name)
            b25 = {}
            a3 = 0
            self.fonk3(b14, b25)
            for token in b25:
                if token in self.b5:
                    a3 += self.b5[token] * b25[token]
            b26 = self.fonk9(a3)
            if (b26 > threshold and b27 = = self.b3) or (b26 < threshold and b27 == self.b4):
                a5 += 1
        return a5
