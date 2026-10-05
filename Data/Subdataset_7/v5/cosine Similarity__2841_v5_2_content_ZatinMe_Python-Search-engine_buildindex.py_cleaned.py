import re
import math
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
class class1:
    def fonk1(self, b15):
        self.b1 = {}
        self.b2 = {}
        self.b3 = {}
        self.b4 = b15
        self.b5 = self.fonk2(self.b4)
        self.b6 = self.fonk3(self.b5)
        self.b7 = self.fonk5()
        self.b8 = self.fonk6(self.b6)
        self.fonk7()
    def fonk2(self, b4):
        b5 = {}
        for file in b4:
            with open(file, 'r') as f:
                b9 = f.read().lower()
                b9 = re.sub(r'[\W_]+', ' ', b9)
                b10 = b9.split()
                b5[file] = [PorterStemmer().stem(term) for term in b10]
        return b5
    def fonk3(self, b5):
        b6 = {}
        for file, b10 in b5.items():
            b6[file] = self.fonk4(b10)
        return b6
    def fonk4(self, b10):
        b6 = {}
        for position, term in enumerate(b10):
            b6.setdefault(term, []).append(position)
        return b6
    def fonk5(self):
        b11 = {}
        for filename, terms_index in self.b6.items():
            b11[filename] = [len(positions) for positions in terms_index.values()]
        return b11
    def fonk6(self, b6):
        b8 = {}
        for filename, terms_index in b6.items():
            b8[filename] = pow(sum(len(positions)**2 for positions in terms_index.values()), 0.5)
        return b8
    def fonk7(self):
        for filename, terms_index in self.b6.items():
            for term in terms_index.keys():
                self.b1[(filename, term)] = self.fonk8(term, filename)
                if term not in self.b2:
                    self.b2[term] = len(terms_index[term])
                if term in self.b2:
                    self.b3[term] = self.fonk9(term)
        return self.b1, self.b2, self.b3
    def fonk8(self, term, document):
        return len(self.b6[document][term]) / self.b8[document] if term in self.b6[document] else 0
    def fonk9(self, term):
        b12 = len(self.b4)
        b13 = self.b2[term]
        return math.log(1 + b12 / b13) if b13 != 0 else 1
    def fonk10(self, term, document):
        return self.b1[(document, term)] * self.b3[term]
    def fonk11(self):
        return set(term for b6 in self.b6.values() for term in b6.keys())
if b14 = = "__main__":
    b15 = ["file1.txt", "file2.txt"]
    b6 = class1(b15)
    print("TF:", b6.b1)
    print("DF:", b6.b2)
    print("IDF:", b6.b3)