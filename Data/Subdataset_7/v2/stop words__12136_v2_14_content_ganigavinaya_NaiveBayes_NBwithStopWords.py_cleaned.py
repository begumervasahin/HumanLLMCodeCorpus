import os
import re
import io
import math
class class1:
    def fonk1(self, training_ham_path, training_spam_path, test_ham_path, test_spam_path):
        self.b1 = {
            'HAM': training_ham_path,
            'SPAM': training_spam_path
        }
        self.b2 = {
            'HAM': test_ham_path,
            'SPAM': test_spam_path
        }
        self.b3 = {'HAM': {}, 'SPAM': {}}
        self.b4 = {'HAM': 0, 'SPAM': 0}
        self.b5 = set()
        self.b6 = {}
        self.b7 = {}
        self.fonk2()
    def fonk2(self):
        self.b8 = set([
        ])
    def fonk3(self, text):
        b9 = re.sub("[^a-zA-Z\s]", "", text).lower()
        b10 = b9.split()
        return [word for word in b10 if word not in self.b8]
    def fonk4(self):
        for category, path in self.b1.items():
            for filename in os.listdir(path):
                with io.open(os.path.join(path, filename), 'r', b11 = 'iso-8859-1') as file:
                    b10 = self.fonk3(file.read())
                    for word in b10:
                        self.b5.add(word)
                        self.b3[category][word] = self.b3[category].get(word, 0) + 1
                        self.b4[category] += 1
        self.fonk5()
        self.fonk6()
    def fonk5(self):
        b12 = sum(len(os.listdir(path)) for path in self.b1.values())
        for category in self.b1.keys():
            self.b6[category] = len(os.listdir(self.b1[category])) / b12
    def fonk6(self):
        b13 = len(self.b5)
        for word in self.b5:
            self.b7[word] = {}
            for category in self.b1.keys():
                b14 = self.b3[category].get(word, 0)
                self.b7[word][category] = (b14 + 1) / (self.b4[category] + b13)
    def fonk7(self, text):
        b10 = set(self.fonk3(text))
        b15 = {category: math.log(self.b6[category], 2) for category in self.b1.keys()}
        for word in b10:
            if word in self.b5:
                for category in b15:
                    b15[category] += math.log(self.b7[word][category], 2)
        return 'HAM' if b15['HAM'] > b15['SPAM'] else 'SPAM'
    def fonk8(self):
        for category, path in self.b2.items():
            a1 = 0
            b16 = os.listdir(path)
            for filename in b16:
                with io.open(os.path.join(path, filename), 'r', b11 = 'iso-8859-1') as file:
                    if self.fonk7(file.read()) == category:
                        a1 += 1
            b17 = a1 / len(b16) * 100
            print(f"{category} test b17: {b17:.2f}%")
