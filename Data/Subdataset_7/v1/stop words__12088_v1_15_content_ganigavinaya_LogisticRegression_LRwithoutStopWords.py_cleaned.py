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
        self.fonk5(self.b1, 1.0)
        self.fonk5(self.b2, 0.0)
    def fonk3(self, path, b12):
        with io.open(path, 'r', b8 = 'iso-8859-1') as f:
            b9 = f.readlines()
            for line in b9:
                b10 = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in b10:
                    b12[word] = b12.get(word, 0) + 1
    def fonk4(self):
        b11 = {}
        self.fonk5(self.b1, 1.0, b12 = b11)
        b13 = {}
        self.fonk5(self.b2, 0.0, b12 = b13)
        self.b6 = set(b11.keys()).union(b13.keys())
        for word in self.b6:
            self.b5[word] = 0.0
    def fonk5(self, folder, classification, b12 = None):
        b14 = os.listdir(folder)
        for file in b14:
            b15 = os.path.join(folder, file)
            if b12 is None:
                b12 = {}
            self.fonk3(b15, b12)
            self.b7.append({'fileName': b15, 'b16': b12, 'class': classification})
    def fonk6(self):
        for _ in range(500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        a3 = 0
        for eachFile in self.b7:
            b16 = eachFile["b16"]
            a4 = 1
            for everyToken in b16:
                a4 += b16[everyToken] * self.b5[everyToken]
            eachFile["a3"] = self.fonk8(a4)
            a3 += eachFile["a3"]
    def fonk8(self, x):
        b17 = 1 + np.exp(-x)
        return 1 / b17
    def fonk9(self):
        for b16 in self.b5.keys():
            a5 = 0
            a3 = 0
            for eachFile in self.b7:
                b18 = eachFile["b16"]
                b19 = eachFile["class"]
                if b16 in b18:
                    b20 = b19 - eachFile["a3"]
                    a3 += b20
                    a5 += b18[b16] * b20
            self.b5[b16] += ((a5 * self.a1) - (self.a1 * self.a2 * self.b5[b16]))
    def fonk10(self):
        b21 = os.listdir(self.b3)
        a6 = 0
        for file in b21:
            b22 = {}
            a4 = 0
            b15 = os.path.join(self.b3, file)
            self.fonk3(b15, b22)
            for b16 in b22:
                if b16 in self.b5:
                    a4 += self.b5[b16] * b22[b16]
            b23 = self.fonk8(a4)
            if b23 > 0.5:
                a6 += 1
        b24 = (a6 / len(b21)) * 100
        print("Ham accuracy is ", b24)
        b25 = os.listdir(self.b4)
        a7 = 0
        for file in b25:
            b26 = {}
            a4 = 0
            b15 = os.path.join(self.b4, file)
            self.fonk3(b15, b26)
            for b16 in b26:
                if b16 in self.b5:
                    a4 += self.b5[b16] * b26[b16]
            b23 = self.fonk8(a4)
            if b23 < 0.5:
                a7 += 1
        b27 = (a7 / len(b25)) * 100
        print("Spam accuracy is ", b27)
        b28 = ((a7 + a6) / (len(b21) + len(b25))) * 100
        print("Total accuracy is ", b28)
if b29 = = "__main__":
    b1 = "train_ham_folder_path"
    b2 = "train_spam_folder_path"
    b3 = "test_ham_folder_path"
    b4 = "test_spam_folder_path"
    b30 = class1(b1, b2, b3, b4)
    b30.fonk2()
    b30.fonk6()
    b30.fonk10()