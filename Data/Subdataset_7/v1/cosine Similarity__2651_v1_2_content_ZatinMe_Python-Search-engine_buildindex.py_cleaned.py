import re
import math
from nltk.stem import *
from nltk.tokenize import sent_tokenize, word_tokenize
class class1:
    def fonk1(self, b19):
        self.b1 = {}
        self.b2 = {}
        self.b3 = {}
        self.b4 = b19
        self.b5 = self.fonk2(self.b4)
        self.b6 = self.fonk15(self.b4)
        self.b7 = self.fonk14()
        self.b8 = self.fonk6()
        self.b9 = self.fonk9(self.b4)
        self.fonk11()
    def fonk2(self, b4):
        b5 = {}
        for file in b4:
            b10 = re.compile('[\W_]+')
            b11 = open(file, 'r').read().lower()
            b11 = b10.sub(' ', b11)
            b11 = re.sub(r'[\W_]+', '', b11)
            b5[file] = b11.split()
        return b5
    def fonk3(self, termlist):
        b12 = {}
        b13 = PorterStemmer()
        for b20, words in enumerate(termlist):
            for b14 in word_tokenize(words):
                b14 = b14.lower().strip('.').strip(',')
                b14 = b13.stem(b14)
                if b14 in b12:
                    b12[b14].append(b20)
                else:
                    b12[b14] = [b20]
        return b12
    def fonk4(self, termlists):
        b15 = {}
        for filename in termlists.keys():
            b15[filename] = self.fonk3(termlists[filename])
        return b15
    def fonk5(self):
        b16 = {}
        b17 = self.b6
        for filename in b17.keys():
            self.b1[filename] = {}
            for b14 in b17[filename].keys():
                self.b1[filename][b14] = len(b17[filename][b14])
                if b14 in self.b2.keys():
                    self.b2[b14] += 1
                else:
                    self.b2[b14] = 1
                if b14 in b16.keys():
                    if filename in b16[b14].keys():
                        b16[b14][filename].append(b17[filename][b14][:])
                    else:
                        b16[b14][filename] = b17[filename][b14]
                else:
                    b16[b14] = {filename: b17[filename][b14]}
        return b16
    def fonk6(self):
        b8 = {}
        for filename in self.b4:
            b8[filename] = [len(self.b6[filename][b14]) for b14 in self.b6[filename].keys()]
        return b8
    def fonk7(self, term):
        return len(self.b7[term].keys()) if term in self.b7.keys() else 0
    def fonk8(self):
        return len(self.b4)
    def fonk9(self, documents):
        b9 = {}
        for document in documents:
            b9[document] = pow(sum(map(lambda x: x**2, self.b8[document])), 0.5)
        return b9
    def fonk10(self, term, document):
        return self.b1[document][term] / self.b9[document] if term in self.b1[document].keys() else 0
    def fonk11(self):
        for filename in self.b4:
            for term in self.fonk16():
                self.b1[filename][term] = self.fonk10(term, filename)
                if term in self.b2.keys():
                    self.b3[term] = self.fonk12(self.fonk8(), self.b2[term])
                else:
                    self.b3[term] = 0
        return self.b2, self.b1, self.b3
    def fonk12(self, N, N_t):
        return math.log(1 + N / N_t) if N_t != 0 else 1
    def fonk13(self, term, document):
        return self.b1[document][term] * self.b3[term]
    def fonk14(self):
        return self.fonk5()
    def fonk15(self, b4):
        b5 = {}
        for file in b4:
            b5[file] = self.b5[file]
        return self.fonk4(b5)
    def fonk16(self):
        return self.b7.keys()
if b18 = = "__main__":
    b19 = ["file1.txt", "file2.txt"]
    b20 = class1(b19)
    print("TF:", b20.b1)
    print("DF:", b20.b2)
    print("IDF:", b20.b3)