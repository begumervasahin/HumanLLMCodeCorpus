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
    def fonk2(self, b16):
        b10 = self.b1 if b16 == self.a1 else self.b2
        b11 = os.listdir(b10)
        b12 = {}
        a5 = 0
        for filename in b11:
            with io.open(os.path.join(b10, filename), 'r', b13 = 'iso-8859-1') as f:
                b14 = f.readlines()
                for line in b14:
                    b15 = re.findall(r'\b\w+\b', line.lower())
                    for word in b15:
                        b12[word] = b12.get(word, 0) + 1
                        a5 += 1
        self.b5.extend(b12.keys())
        if b16 = = self.a1:
            self.b6 = b12
            self.a3 = a5
        else:
            self.b7 = b12
            self.a4 = a5
    def fonk3(self):
        for word in self.b5:
            b17 = self.b6.get(word, 0) + 1
            b18 = self.b7.get(word, 0) + 1
            self.b9[word] = [b17 / (self.a3 + len(self.b5)),
                                         b18 / (self.a4 + len(self.b5))]
    def fonk4(self):
        b19 = len(os.listdir(self.b1))
        b20 = len(os.listdir(self.b2))
        b21 = b19 + b20
        self.b8[self.a1] = b19 / b21
        self.b8[self.a2] = b20 / b21
        self.fonk2(self.a1)
        self.fonk2(self.a2)
        self.fonk3()
    def fonk5(self, path):
        a6 = 0
        a7 = 0
        b22 = self.a1 if path == self.b3 else self.a2
        b23 = os.listdir(path)
        for filename in b23:
            with io.open(os.path.join(path, filename), 'r', b13 = 'iso-8859-1') as f:
                b24 = f.read().lower()
                b15 = re.findall(r'\b\w+\b', b24)
                b25 = {self.a1: math.log(self.b8[self.a1], 2),
                         self.a2: math.log(self.b8[self.a2], 2)}
                for word in b15:
                    if word in self.b5:
                        b25[self.a1] += math.log(self.b9[word][self.a1], 2)
                        b25[self.a2] += math.log(self.b9[word][self.a2], 2)
                b26 = max(b25, key=b25.get)
                if b26 = = b22:
                    a6 += 1
                a7 += 1
        return a6, a7
    def fonk6(self):
        ham_correct, b27 = self.fonk5(self.b3)
        spam_correct, b28 = self.fonk5(self.b4)
        b29 = (ham_correct / b27) * 100 if b27 != 0 else 0
        b30 = (spam_correct / b28) * 100 if b28 != 0 else 0
        b31 = ((ham_correct + spam_correct) / (b27 + b28)) * 100 if (b27 + b28) != 0 else 0
        print("Ham test b32 = ", b29)
        print("Spam test b32 = ", b30)
        print("Total test b32 = ", b31)
if b33 = = "__main__":
    b1 = "path_to_training_ham_folder"
    b2 = "path_to_training_spam_folder"
    b3 = "path_to_test_ham_folder"
    b4 = "path_to_test_spam_folder"
    b34 = class1(b1, b2, b3, b4)
    b34.fonk4()
    b34.fonk6()