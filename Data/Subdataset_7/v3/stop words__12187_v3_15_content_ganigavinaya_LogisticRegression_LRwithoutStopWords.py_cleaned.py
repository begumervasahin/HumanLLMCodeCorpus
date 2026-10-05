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
        self.b6 = set()
        self.a1 = 0.0001
        self.a2 = 5
        self.b7 = []
    def fonk2(self):
        self.fonk4()
        self.fonk5()
    def fonk3(self, path):
        b8 = {}
        with io.open(path, 'r', b9 = 'iso-8859-1') as f:
            for line in f:
                b10 = re.sub("[^a-zA-Z0-9\s]", "", line.lower()).split()
                for word in b10:
                    b8[word] = b8.get(word, 0) + 1
        return b8
    def fonk4(self):
        for folder in [self.b1, self.b2]:
            for file in os.listdir(folder):
                b11 = os.path.join(folder, file)
                b8 = self.fonk3(b11)
                self.b6.update(b8.keys())
        self.b5 = {word: 0.0 for word in self.b6}
    def fonk5(self):
        for folder, classification in [(self.b1, 1.0), (self.b2, 0.0)]:
            for file in os.listdir(folder):
                b11 = os.path.join(folder, file)
                b8 = self.fonk3(b11)
                self.b7.append({'file_name': b11, 'b12': b8, 'class': classification})
    def fonk6(self):
        for _ in range(500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        for data in self.b7:
            b12 = data["b12"]
            a3 = 1
            for word, count in b12.items():
                a3 += count * self.b5[word]
            data["error"] = self.fonk8(a3)
    def fonk8(self, x):
        return 1 / (1 + np.exp(-x))
    def fonk9(self):
        for word in self.b5:
            b13 = sum((data["class"] - data["error"]) * b12.get(word, 0) for data in self.b7)
            self.b5[word] += (b13 * self.a1) - (self.a1 * self.a2 * self.b5[word])
    def fonk10(self):
        b14 = sum(self.fonk11(os.path.join(self.b3, file)) > 0.5 for file in os.listdir(self.b3))
        b15 = sum(self.fonk11(os.path.join(self.b4, file)) < 0.5 for file in os.listdir(self.b4))
        b16 = (b14 / len(os.listdir(self.b3))) * 100
        b17 = (b15 / len(os.listdir(self.b4))) * 100
        b18 = ((b14 + b15) / (len(os.listdir(self.b3)) + len(os.listdir(self.b4)))) * 100
        print("Ham accuracy is ", b16)
        print("Spam accuracy is ", b17)
        print("Total accuracy is ", b18)
    def fonk11(self, b11):
        b8 = self.fonk3(b11)
        a3 = sum(self.b5[word] * count for word, count in b8.items() if word in self.b5)
        return self.fonk8(a3)
if b19 = = "__main__":
    b20 = "train_ham_folder_path"
    b21 = "train_spam_folder_path"
    b22 = "test_ham_folder_path"
    b23 = "test_spam_folder_path"
    b24 = class1(b20, b21, b22, b23)
    b24.fonk2()
    b24.fonk6()
    b24.fonk10()