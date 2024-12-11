import re
import math
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
class class1:
    def fonk1(self, b17):
        self.b1 = {}
        self.b2 = {}
        self.b3 = {}
        self.b4 = b17
        self.b5 = self.fonk2(self.b4)
        self.b6 = self.fonk4(self.b4)
        self.b7 = self.fonk6()
        self.b8 = self.fonk7()
        self.b9 = self.fonk8(self.b4)
        self.fonk10()
    def fonk2(self, b4):
        b5 = {}
        for file in b4:
            b10 = open(file, 'r').read().lower()
            b10 = re.sub(r'[\W_]+', ' ', b10)
            b5[file] = b10.split()
        return b5
    def fonk3(self, termlist):
        b11 = {}
        b12 = PorterStemmer()
        for b18, words in enumerate(termlist):
            for b13 in word_tokenize(words):
                b13 = b13.lower().strip('.').strip(',')
                b13 = b12.stem(b13)
                if b13 in b11:
                    b11[b13].append(b18)
                else:
                    b11[b13] = [b18]
        return b11
    def fonk4(self, b4):
        b5 = {}
        for file in b4:
            b5[file] = self.b5[file]
        return self.fonk5(b5)
    def fonk5(self, termlists):
        b14 = {}
        for filename in termlists.keys():
            b14[filename] = self.fonk3(termlists[filename])
        return b14
    def fonk6(self):
        b7 = {}
        b15 = self.b6
        for filename in b15.keys():
            self.b1[filename] = {}
            for b13 in b15[filename].keys():
                self.b1[filename][b13] = len(b15[filename][b13])
                if b13 in self.b2.keys():
                    self.b2[b13] += 1
                else:
                    self.b2[b13] = 1
                if b13 in b7.keys():
                    if filename in b7[b13].keys():
                        b7[b13][filename].append(b15[filename][b13][:])
                    else:
                        b7[b13][filename] = b15[filename][b13]
                else:
                    b7[b13] = {filename: b15[filename][b13]}
        return b7
    def fonk7(self):
        b8 = {}
        for filename in self.b4:
            b8[filename] = [len(self.b6[filename][b13]) for b13 in self.b6[filename].keys()]
        return b8
    def fonk8(self, documents):
        b9 = {}
        for document in documents:
            b9[document] = pow(sum(map(lambda x: x**2, self.b8[document])), 0.5)
        return b9
    def fonk9(self, term, document):
        return self.b1[document][term] / self.b9[document] if term in self.b1[document].keys() else 0
    def fonk10(self):
        for filename in self.b4:
            for term in self.fonk13():
                self.b1[filename][term] = self.fonk9(term, filename)
                if term in self.b2.keys():
                    self.b3[term] = self.fonk11(len(self.b4), self.b2[term])
                else:
                    self.b3[term] = 0
    def fonk11(self, N, N_t):
        return math.log(1 + N / N_t) if N_t != 0 else 1
    def fonk12(self, term, document):
        return self.b1[document][term] * self.b3[term]
    def fonk13(self):
        return self.b7.keys()
if b16 = = "__main__":
    b17 = ["file1.txt", "file2.txt"]
    b18 = class1(b17)
    print("TF:", b18.b1)
    print("DF:", b18.b2)
    print("IDF:", b18.b3)