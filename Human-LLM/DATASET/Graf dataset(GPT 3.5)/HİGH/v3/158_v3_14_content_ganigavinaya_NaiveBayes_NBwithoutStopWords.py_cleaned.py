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
    def fonk2(self, directory, word_count_dict):
        b10 = os.listdir(directory)
        a5 = 0
        for filename in b10:
            with io.open(os.path.join(directory, filename), 'r', b11 = 'iso-8859-1') as file:
                b12 = file.readlines()
                for line in b12:
                    b13 = re.findall(r'\b\w+\b', line.lower())
                    for word in b13:
                        word_count_dict[word] = word_count_dict.get(word, 0) + 1
                        a5 += 1
        return a5
    def fonk3(self):
        for word in self.b5:
            b14 = self.b6.get(word, 0) + 1
            b15 = self.b7.get(word, 0) + 1
            self.b9[word] = [
                b14 / (self.a3 + len(self.b5)),
                b15 / (self.a4 + len(self.b5))
            ]
    def fonk4(self):
        b16 = len(os.listdir(self.b1))
        b17 = len(os.listdir(self.b2))
        b18 = b16 + b17
        self.b8[self.a1] = b16 / b18
        self.b8[self.a2] = b17 / b18
        self.a3 = self.fonk2(self.b1, self.b6)
        self.a4 = self.fonk2(self.b2, self.b7)
        self.b5 = list(set(self.b6.keys()) | set(self.b7.keys()))
        self.fonk3()
    def fonk5(self, directory):
        a6 = 0
        a7 = 0
        b19 = self.a1 if directory == self.b3 else self.a2
        b10 = os.listdir(directory)
        for filename in b10:
            with io.open(os.path.join(directory, filename), 'r', b11 = 'iso-8859-1') as file:
                b20 = file.read().lower()
                b13 = re.findall(r'\b\w+\b', b20)
                b21 = {self.a1: math.log(self.b8[self.a1], 2),
                         self.a2: math.log(self.b8[self.a2], 2)}
                for word in b13:
                    if word in self.b5:
                        b21[self.a1] += math.log(self.b9[word][self.a1], 2)
                        b21[self.a2] += math.log(self.b9[word][self.a2], 2)
                b22 = max(b21, key=b21.get)
                if b22 = = b19:
                    a6 += 1
                a7 += 1
        return a6, a7
    def fonk6(self):
        ham_correct, b23 = self.fonk5(self.b3)
        spam_correct, b24 = self.fonk5(self.b4)
        b25 = (ham_correct / b23) * 100 if b23 != 0 else 0
        b26 = (spam_correct / b24) * 100 if b24 != 0 else 0
        b27 = ((ham_correct + spam_correct) / (b23 + b24)) * 100 if (b23 + b24) != 0 else 0
        print("Ham test b28 = ", b25)
        print("Spam test b28 = ", b26)
        print("Total test b28 = ", b27)
if b29 = = "__main__":
    b1 = "path_to_training_ham_folder"
    b2 = "path_to_training_spam_folder"
    b3 = "path_to_test_ham_folder"
    b4 = "path_to_test_spam_folder"
    b30 = class1(b1, b2, b3, b4)
    b30.fonk4()
    b30.fonk6()