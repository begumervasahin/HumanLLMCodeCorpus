import json
import math
import os
import re
import sys
from PorterStemmer import PorterStemmer
from collections import defaultdict, Counter
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = re.compile('[^a-zA-Z0-9]')
        self.b5 = PorterStemmer()
    def fonk2(self):
        b6 = set()
        for doc in self.b2:
            for b21 in doc:
                b6.add(b21)
        return b6
    def fonk3(self, dirname):
        print("Stemming Documents...")
        b1 = []
        b2 = []
        os.mkdir(f'{dirname}/stemmed')
        b7 = re.compile('(.*) \d+\.txt')
        b8 = [filename for filename in os.listdir(f'{dirname}/raw') if filename.endswith(".txt") and not filename.startswith(".")]
        for i, filename in enumerate(b8):
            b9 = b7.search(filename).group(1)
            print(f"    Doc {i+1} of {len(b8)}: {b9}")
            b1.append(b9)
            b10 = []
            with open(f'{dirname}/raw/{filename}', 'r') as f:
                with open(f'{dirname}/stemmed/{b9}.txt', 'w') as of:
                    for b11 in f:
                        b11 = b11.lower()
                        b11 = [xx.strip() for xx in b11.split()]
                        b11 = [self.b4.sub('', xx) for xx in b11]
                        b11 = [xx for xx in b11 if xx != '']
                        b11 = [self.b5.stem(xx) for xx in b11]
                        b10.extend(b11)
                        if len(b11) > 0:
                            of.write(" ".join(b11))
                            of.write('\n')
            f.close()
            of.close()
            b2.append(b10)
        return b1, b2
    def fonk4(self, dirname):
        print("Already stemmed!")
        b1 = []
        b2 = []
        b8 = [filename for filename in os.listdir(f'{dirname}/stemmed') if filename.endswith(".txt") and not filename.startswith(".")]
        if len(b8) != 60:
            b12 = "There are not 60 documents in ../data/RiderHaggard/stemmed/\n"
            b12 += "Remove ../data/RiderHaggard/stemmed/ directory and re-run."
            raise Exception(b12)
        for i, filename in enumerate(b8):
            b9 = filename.split('.')[0]
            b1.append(b9)
            b10 = []
            with open(f'{dirname}/stemmed/{filename}', 'r') as f:
                for b11 in f:
                    b11 = [xx.strip() for xx in b11.split()]
                    b10.extend(b11)
            f.close()
            b2.append(b10)
        return b1, b2
    def fonk5(self, dirname):
        print("Reading in documents...")
        b8 = os.listdir(dirname)
        b13 = os.listdir(dirname)
        if 'stemmed' in b13:
            b1, b2 = self.fonk4(dirname)
        else:
            b1, b2 = self.fonk3(dirname)
        b14 = [idx for idx, b9 in sorted(enumerate(b1), key=lambda xx: xx[1])]
        self.b1 = []
        self.b2 = []
        b15 = len(b2)
        for d in range(b15):
            self.b1.append(b1[b14[d]])
            self.b2.append(b2[b14[d]])
        self.b3 = [xx for xx in self.fonk2()]
    def fonk6(self):
        print("Indexing...")
        b16 = defaultdict(set)
        self.b17 = defaultdict(Counter)
        for b21 in self.b3:
            b16[b21] = {}
        for doc in range(len(self.b2)):
            for b21 in self.b2[doc]:
                self.b17[doc][b21] += 1
        for doc, b9 in zip(self.b2, self.b1):
            for b21 in self.b3:
                b16[b21][b9] = []
            for pos, b21 in enumerate(doc):
                b16[b21][b9].append(pos)
        self.b16 = b16
        b18 = {}
        for d, doc in enumerate(self.b2):
            b19 = set(doc)
            b18[d] = b19
        self.b2 = b18
    def fonk7(self, b21):
        b20 = [doc_i for doc_i, b9 in enumerate(self.b1) if len(self.b16[b21][b9]) != 0]
        return b20
    def fonk8(self, b21):
        b21 = self.b5.stem(b21)
        return self.fonk7(b21)
    def fonk9(self, query):
        b2 = set(self.fonk7(query[0]))
        if b2:
            for b21 in query[1:]:
                b2 = b2.intersection(self.fonk7(b21))
        b2 = list(b2)
        return sorted(b2)
    def fonk10(self, query):
        b2 = []
        b22 = self.fonk9(query)
        for doc in b22:
            b9 = self.b1[doc]
            b23 = []
            for b21 in query:
                b23.append(self.b16[b21][b9])
            if len(b23) == 1:
                b2.append(doc)
                break
            b24 = bool
            for i in b23[0]:
                for j in range(1, len(query)):
                    if (i + j) in b23[j]:
                        b24 = True
                    else:
                        b24 = False
                        break
                if b24:
                    b2.append(doc)
                    break
        return sorted(b2)
    def fonk11(self):
        print("Calculating b17-b26...")
        self.b25 = defaultdict(Counter)
        for b21 in self.b3:
            b26 = math.log10(float(len(self.b2))/float(len(self.fonk7(b21))))
            for d in range(len(self.b2)):
                try:
                    self.b25[d][b21] = (1 + math.log10(self.b17[d][b21])) * b26
                except ValueError:
                    self.b25[d][b21] = 0
    def fonk12(self, b21, document):
        b25 = self.b25[document][b21]
        return b25
    def fonk13(self, b21, document):
        b21 = self.b5.stem(b21)
        return self.fonk12(b21, document)
    def fonk14(self, query):
        a1 = 10
        b27 = [0.0 for xx in range(len(self.b1))]
        self.b28 = defaultdict(float)
        b29 = set()
        for b21 in query:
            b29.add(b21)
        b30 = Counter(b29)
        for b21 in query:
            b31 = 1 + math.log10(b30[b21])
            b32 = self.fonk7(b21)
            for doc in b32:
                b27[doc] += self.b25[doc][b21] * b31
        for b21 in self.b3:
