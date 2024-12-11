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
            b6.update(doc)
        return b6
    def fonk3(self, document):
        b7 = []
        for b8 in document:
            b8 = b8.lower().split()
            b8 = [self.b4.sub('', word) for word in b8]
            b8 = [self.b5.stem(word) for word in b8 if word]
            b7.extend(b8)
        return b7
    def fonk4(self, dirname):
        print("Stemming Documents...")
        b1 = []
        b2 = []
        os.makedirs(f'{dirname}/stemmed', b9 = True)
        b10 = re.compile('(.*) \d+\.txt')
        b11 = [filename for filename in os.listdir(f'{dirname}/raw') if filename.endswith(".txt") and not filename.startswith(".")]
        for i, filename in enumerate(b11):
            b12 = b10.search(filename).group(1)
            print(f"    Doc {i+1} of {len(b11)}: {b12}")
            b1.append(b12)
            b13 = []
            with open(f'{dirname}/raw/{filename}', 'r') as f:
                with open(f'{dirname}/stemmed/{b12}.txt', 'w') as of:
                    b13 = self.fonk3(f)
                    of.write('\n'.join(b13))
            b2.append(b13)
        return b1, b2
    def fonk5(self, dirname):
        print("Already stemmed!")
        b1 = []
        b2 = []
        b11 = [filename for filename in os.listdir(f'{dirname}/stemmed') if filename.endswith(".txt") and not filename.startswith(".")]
        if len(b11) != 60:
            b14 = "There are not 60 documents in ../data/RiderHaggard/stemmed/\n"
            b14 += "Remove ../data/RiderHaggard/stemmed/ directory and re-run."
            raise Exception(b14)
        for i, filename in enumerate(b11):
            b12 = filename.split('.')[0]
            b1.append(b12)
            with open(f'{dirname}/stemmed/{filename}', 'r') as f:
                b13 = f.read().splitlines()
            b2.append(b13)
        return b1, b2
    def fonk6(self, dirname):
        print("Reading in documents...")
        b11 = os.listdir(dirname)
        b15 = os.listdir(dirname)
        if 'stemmed' in b15:
            b1, b2 = self.fonk5(dirname)
        else:
            b1, b2 = self.fonk4(dirname)
        b16 = sorted(range(len(b1)), b28=lambda k: b1[k])
        self.b1 = [b1[i] for i in b16]
        self.b2 = [b2[i] for i in b16]
        self.b3 = list(self.fonk2())
    def fonk7(self):
        print("Indexing...")
        self.b17 = defaultdict(lambda: defaultdict(list))
        self.b18 = defaultdict(Counter)
        for idx, doc in enumerate(self.b2):
            for pos, word in enumerate(doc):
                self.b17[word][self.b1[idx]].append(pos)
                self.b18[idx][word] += 1
    def fonk8(self, word):
        return [idx for idx, b12 in enumerate(self.b1) if self.b17[word][b12]]
    def fonk9(self, b29):
        if not b29: return []
        b2 = set(self.fonk8(b29[0]))
        for word in b29[1:]:
            b2.intersection_update(self.fonk8(word))
        return sorted(b2)
    def fonk10(self, b29):
        b19 = self.fonk9(b29)
        b20 = []
        for doc in b19:
            b21 = [self.b17[word][self.b1[doc]] for word in b29]
            b22 = any(all(pos + i in b21[j] for j, pos in enumerate(b21[0])) for i in range(1, len(b29)))
            if b22:
                b20.append(doc)
        return b20
    def fonk11(self):
        print("Calculating b18-b24...")
        self.b23 = defaultdict(Counter)
        for word in self.b3:
            b24 = math.log10(len(self.b2) / len(self.fonk8(word)))
            for idx, doc in enumerate(self.b2):
                b18 = 1 + math.log10(self.b18[idx][word]) if self.b18[idx][word] else 0
                self.b23[idx][word] = b18 * b24
    def fonk12(self, b29):
        if not b29: return []
        b25 = defaultdict(float)
        b26 = Counter(b29)
        for word in b29:
            b27 = 1 + math.log10(b26[word])
            for idx, doc in enumerate(self.b2):
                if word in doc:
                    b25[idx] += self.b23[idx][word] * b27
        return sorted(b25.items(), b28 = lambda x: x[1], reverse=True)[:10]
    def fonk13(self, query_str):
        b29 = query_str.lower().split()
        b29 = [self.b4.sub('', word) for word in b29]
        b29 = [self.b5.stem(word) for word in b29 if word]
        return b29
def fonk14(b33):
    b30 = class1()
    b30.fonk6('../data/RiderHaggard')
    b30.fonk7()
    b30.fonk11()
    if not b33:
        run_tests(b30)
    else:
        b29 = " ".join(b33)
        print("Best matching documents to '%s':" % b29)
        b31 = b30.fonk12(b30.fonk13(b29))
        for docId, score in b31:
            print("%s: %e" % (b30.b1[docId], score))
if b32 = = '__main__':
    b33 = sys.argv[1:]
    fonk14(b33)