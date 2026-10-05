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
            for b24 in doc:
                b6.add(b24)
        return b6
    def fonk3(self, dirname):
        print("Stemming Documents...")
        b1 = []
        b2 = []
        os.mkdir('%s/stemmed' % dirname)
        b7 = re.compile('(.*) \d+\.txt')
        b8 = []
        for filename in os.listdir('%s/raw' % dirname):
            if filename.endswith(".txt") and not filename.startswith("."):
                b8.append(filename)
        for i, filename in enumerate(b8):
            b9 = b7.search(filename).group(1)
            print("    Doc %d b12 %d: %s" % (i+1, len(b8), b9))
            b1.append(b9)
            b10 = []
            b11 = open('%s/raw/%s' % (dirname, filename), 'r')
            b12 = open('%s/stemmed/%s.txt' % (dirname, b9), 'w')
            for b13 in b11:
                b13 = b13.lower()
                b13 = [xx.strip() for xx in b13.split()]
                b13 = [self.b4.sub('', xx) for xx in b13]
                b13 = [xx for xx in b13 if xx != '']
                b13 = [self.b5.stem(xx) for xx in b13]
                b10.extend(b13)
                if len(b13) > 0:
                    b12.write(" ".join(b13))
                    b12.write('\n')
            b11.close()
            b12.close()
            b2.append(b10)
        return b1, b2
    def fonk4(self, dirname):
        print("Already stemmed!")
        b1 = []
        b2 = []
        b8 = []
        for filename in os.listdir('%s/stemmed' % dirname):
            if filename.endswith(".txt") and not filename.startswith("."):
                b8.append(filename)
        if len(b8) != 60:
            b14 = "There are not 60 documents in ../data/RiderHaggard/stemmed/\n"
            b14 += "Remove ../data/RiderHaggard/stemmed/ directory and re-run."
            raise Exception(b14)
        for i, filename in enumerate(b8):
            b9 = filename.split('.')[0]
            b1.append(b9)
            b10 = []
            b11 = open('%s/stemmed/%s' % (dirname, filename), 'r')
            for b13 in b11:
                b13 = [xx.strip() for xx in b13.split()]
                b10.extend(b13)
            b11.close()
            b2.append(b10)
        return b1, b2
    def fonk5(self, dirname):
        print("Reading in documents...")
        b8 = os.listdir(dirname)
        b15 = os.listdir(dirname)
        if 'stemmed' in b15:
            b1, b2 = self.fonk4(dirname)
        else:
            b1, b2 = self.fonk3(dirname)
        b16 = [idx for idx, b9 in sorted(enumerate(b1),
            b17 = lambda xx : xx[1])]
        self.b1 = []
        self.b2 = []
        b18 = len(b2)
        for d in range(b18):
            self.b1.append(b1[b16[d]])
            self.b2.append(b2[b16[d]])
        self.b3 = [xx for xx in self.fonk2()]
    def fonk6(self):
        print("Indexing...")
        b19 = defaultdict(set)
        self.b20 = defaultdict(Counter)
        for b24 in self.b3:
            b19[b24] = {}
        for doc in range(len(self.b2)):
            for b24 in self.b2[doc]:
                self.b20[doc][b24] += 1
        for doc, b9 in zip(self.b2, self.b1):
            for b24 in self.b3:
                b19[b24][b9] = []
            for pos, b24 in enumerate(doc):
                b19[b24][b9].append(pos)
        self.b19 = b19
        b21 = {}
        for d, doc in enumerate(self.b2):
            b22 = set(doc)
            b21[d] = b22
        self.b2 = b21
    def fonk7(self, b24):
        b23 = [doc_i for doc_i, b9 in enumerate(self.b1) if len(self.b19[b24][b9]) != 0]
        return b23
    def fonk8(self, b24):
        b24 = self.b5.stem(b24)
        return self.fonk7(b24)
    def fonk9(self, b38):
        b2 = set(self.fonk7(b38[0]))
        if b2:
            for b24 in b38[1:]:
                b2 = b2.intersection(self.fonk7(b24))
        b2 = list(b2)
        return sorted(b2)
    def fonk10(self, b38):
        b2 = []
        b25 = self.fonk9(b38)
        for doc in b25:
            b9 = self.b1[doc]
            b26 = []
            for b24 in b38:
                b26.append(self.b19[b24][b9])
            if len(b26) == 1:
                b2.append(doc)
                break
            b27 = bool
            for i in b26[0]:
                for j in range(1, len(b38)):
                    if (i + j) in b26[j]:
                        b27 = True
                    else:
                        b27 = False
                        break
                if b27:
                    b2.append(doc)
                    break
        return sorted(b2)
    def fonk11(self):
        print("Calculating b20-b29...")
        self.b28 = defaultdict(Counter)
        for b24 in self.b3:
            b29 = math.log10(float(len(self.b2))/float(len(self.fonk7(b24))))
            for d in range(len(self.b2)):
                try:
                    self.b28[d][b24] = (1 + math.log10(self.b20[d][b24])) * b29
                except ValueError:
                    self.b28[d][b24] = 0
    def fonk12(self, b24, document):
        b28 = self.b28[document][b24]
        return b28
    def fonk13(self, b24, document):
        b24 = self.b5.stem(b24)
        return self.fonk12(b24, document)
    def fonk14(self, b38):
        a1 = 10
        b30 = [0.0 for xx in range(len(self.b1))]
        self.b31 = defaultdict(float)
        b32 = set()
        for b24 in b38:
            b32.add(b24)
        b33 = Counter(b32)
        for b24 in b38:
            b34 = 1 + math.log10(b33[b24])
            b35 = self.fonk7(b24)
            for doc in b35:
                b30[doc] += self.b28[doc][b24] * b34
        for b24 in self.b3:
            for doc in range(len(self.b2)):
                self.b31[doc] += self.b28[doc][b24] ** 2
        for doc in range(len(self.b2)):
            b30[doc] /= math.sqrt(self.b31[doc])
        b36 = [idx for idx, sim in sorted(enumerate(b30),
            b17 = lambda xx : xx[1], reverse = True)]
        b37 = []
        for i in range(a1):
            b37.append((b36[i], b30[b36[i]]))
        return b37
    def fonk15(self, query_str):
        b38 = query_str.lower()
        b38 = b38.split()
        b38 = [self.b4.sub('', xx) for xx in b38]
        b38 = [self.b5.stem(xx) for xx in b38]
        return b38
    def fonk16(self, query_str):
        b38 = self.fonk15(query_str)
        return self.fonk9(b38)
    def fonk17(self, query_str):
        b38 = self.fonk15(query_str)
        return self.fonk10(b38)
    def fonk18(self, query_str):
        b38 = self.fonk15(query_str)
        return self.fonk14(b38)
def fonk19(b52):
    print("===== Running b39 = ====")
    b40 = open('../data/b47.txt')
    b41 = [xx.strip() for xx in b40.readlines()]
    b40.close()
    b40 = open('../data/b42.txt')
    b42 = [xx.strip() for xx in b40.readlines()]
    b40.close()
    a2 = 1e-4
    for b45 in range(5):
        a3 = 0
        a4 = 0
        a5 = 0
        b43 = b41[b45]
        b44 = json.loads(b42[b45])
        if b45 = = 0:
            print("Inverted Index Test (requires both fonk6() and fonk7() to pass)")
            b46 = b43.split(", ")
            for i, b24 in enumerate(b46):
                a5 += 1
                b23 = b52.fonk8(b24)
                if set(b23) == set(b44[i]):
                    a4 += 1
        elif b45 = = 1:
            print("Boolean Retrieval Test")
            b47 = b43.split(", ")
            for i, b38 in enumerate(b47):
                a5 += 1
                b48 = b52.fonk16(b38)
                if set(b48) == set(b44[i]):
                    a4 += 1
        elif b45 = = 2:
            print("Phrase Query Retrieval")
            b47 = b43.split(", ")
            for i, b38 in enumerate(b47):
                a5 += 1
                b48 = b52.fonk17(b38)
                if set(b48) == set(b44[i]):
                    a4 += 1
        elif b45 = = 3:
            print("TF-IDF Test")
            b47 = b43.split("; ")
            b47 = [xx.split(", ") for xx in b47]
            b47 = [(xx[0], int(xx[1])) for xx in b47]
            for i, (b24, doc) in enumerate(b47):
                a5 += 1
                b48 = b52.fonk13(b24, doc)
                if b48 >= float(b44[i]) - a2 and \
                        b48 <= float(b44[i]) + a2:
                    a4 += 1
        elif b45 = = 4:
            print("Cosine Similarity Test")
            b47 = b43.split(", ")
            for i, b38 in enumerate(b47):
                a5 += 1
                b49 = b52.fonk18(b38)
                b50 = b49[0]
                if b50[0] == b44[i][0]:
                    if b50[1] >= float(b44[i][1]) - a2 and \
                            b50[1] <= float(b44[i][1]) + a2:
                        a4 += 1
        b51 = "%d/%d Correct. Accuracy: %b11" % \
                (a4, a5, float(a4)/a5)
        if a4 = = a5:
            a3 = 3
        elif a4 > 0.75 * a5:
            a3 = 2
        elif a4 > 0:
            a3 = 1
        else:
            a3 = 0
        print("    Score: %d Feedback: %s" % (a3, b51))
def fonk20(b54):
    b52 = class1()
    b52.fonk5('../data/RiderHaggard')
    b52.fonk6()
    b52.fonk11()
    if len(b54) == 0:
        fonk19(b52)
    else:
        b38 = " ".join(b54)
        print("Best matching documents to '%s':" % b38)
        b37 = b52.fonk18(b38)
        for docId, score in b37:
            print("%s: %e" % (b52.b1[docId], score))
if b53 = = '__main__':
    b54 = sys.argv[1:]
    fonk20(b54)