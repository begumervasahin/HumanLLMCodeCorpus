import nltk
nltk.download('punkt')
from textblob import TextBlob as tb
import json
import math
import sys
class class1:
    def fonk1(self, b9):
        self.b1 = b9
        self.b2 = ""
        self.b3 = {}
        self.b4 = []
        self.a1 = 0
    def fonk2(self):
        for cp in self.b1:
            self.b2 = json.load(open(cp, 'r'))
            self.fonk3()
        self.fonk4()
    def fonk3(self):
        for i in range(0,len(self.b2)):
            b5 = '. '.join(self.b2[i]['b5'])
            b5.replace('..','.')
            self.b4.append(tb(b5))
        self.a1 = len(self.b4)
    def fonk4(self):
        for i, blob in enumerate(self.b4):
            for word in set(blob.words):
                if word not in self.b3:
                    self.b3[word] = 0
                self.b3[word] += 1
    def fonk5(self):
        b6 = "stop-words.txt"
        b7 = open(b6, 'w')
        for b8, val in sorted(self.b3.items(), b8 = lambda x: x[1], reverse=True)[:102]:
            b7.write(b8)
            b7.write('\n')
        b7.close()
b9 = ["udayavani.json"]
b10 = class1(b9)
b10.fonk2()
b10.fonk5()