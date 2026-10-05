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
    def fonk3(self, path, b14):
        with io.open(path, 'r', b8 = 'iso-8859-1') as f:
            b9 = f.readlines()
            for line in b9:
                b10 = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in b10:
                    b14[word] = b14.get(word, 0) + 1
    def fonk4(self):
        b11 = {}
        self.fonk5(self.b1, b11)
        b12 = {}
        self.fonk5(self.b2, b12)
        self.b6 = set(b11.keys()).union(b12.keys())
        self.b5 = {word: 0.0 for word in self.b6}
    def fonk5(self, b26, b14):
        for file_name in os.listdir(b26):
            b13 = os.path.join(b26, file_name)
            self.fonk3(b13, b14)
    def fonk6(self, b26, classification):
        for file_name in os.listdir(b26):
            b13 = os.path.join(b26, file_name)
            b14 = {}
            self.fonk3(b13, b14)
            self.b7.append({'file_name': b13, 'token': b14, 'class': classification})
    def fonk7(self):
        for _ in range(500):
            self.fonk8()
            self.fonk10()
    def fonk8(self):
        for b7 in self.b7:
            b15 = b7["token"]
            a3 = 1
            for token in b15:
                a3 += b15[token] * self.b5[token]
            b7["error"] = self.fonk9(a3)
    def fonk9(self, x):
        b16 = 1 + np.exp(-x)
        return 1 / b16
    def fonk10(self):
        for token in self.b5.keys():
            a4 = 0
            for b7 in self.b7:
                b15 = b7["token"]
                b17 = b7["class"]
                if token in b15:
                    b18 = b17 - b7["error"]
                    a4 += b15[token] * b18
            self.b5[token] += ((a4 * self.a1) - (self.a1 * self.a2 * self.b5[token]))
    def fonk11(self):
        b19 = self.fonk12(self.b3, threshold=0.5)
        b20 = self.fonk12(self.b4, threshold=0.5)
        b21 = (b19 / len(os.listdir(self.b3))) * 100
        b22 = (b20 / len(os.listdir(self.b4))) * 100
        b23 = ((b19 + b20) / (len(os.listdir(self.b3)) + len(os.listdir(self.b4)))) * 100
        print("Ham accuracy is ", b21)
        print("Spam accuracy is ", b22)
        print("Total accuracy is ", b23)
    def fonk12(self, b26, threshold):
        a5 = 0
        for file_name in os.listdir(b26):
            b13 = os.path.join(b26, file_name)
            b24 = {}
            a3 = 0
            self.fonk3(b13, b24)
            for token in b24:
                if token in self.b5:
                    a3 += self.b5[token] * b24[token]
            b25 = self.fonk9(a3)
            if (b25 > threshold and b26 = = self.b3) or (b25 < threshold and b26 == self.b4):
                a5 += 1
        return a5
