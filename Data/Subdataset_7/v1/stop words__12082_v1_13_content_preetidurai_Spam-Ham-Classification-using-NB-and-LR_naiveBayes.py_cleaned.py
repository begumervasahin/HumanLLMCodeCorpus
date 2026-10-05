from collections import Counter
import math as m
import sys
from NBHelper import *
class class1:
    def fonk1(self, b1, classNames):
        self.b1 = b1
        self.b2 = {i: classNames[i] for i in range(b1)}
        self.b3 = {}
        self.b4 = {}
        self.b5 = {}
        self.b6 = []
        self.b7 = set()
    def fonk2(self, pathArray):
        b8 = {}
        a1 = 0
        for b14, value in self.b2.items():
            b9 = getMailDictionary(pathArray[b14])
            b8[value] = len(b9)
            a1 += len(b9)
            self.b3[value] = getVocabulary(b9)
        for b14, value in b8.items():
            self.b4[b14] = b8[b14] / a1
    def fonk3(self, pathArray, stopWordPath):
        b8 = {}
        a1 = 0
        b10 = readStopWords(stopWordPath)
        for b14, value in self.b2.items():
            b9 = getMailDictionaryWOStopWords(pathArray[b14], b10)
            b8[value] = len(b9)
            a1 += len(b9)
            self.b3[value] = getVocabulary(b9)
        for b14, value in b8.items():
            self.b4[b14] = b8[b14] / a1
    def fonk4(self):
        for value in self.b3.values():
            self.b6.extend(value)
        self.b7 = set(self.b6)
    def fonk5(self):
        for value in self.b2.values():
            b11 = Counter(self.b3[value])
            self.b5[value] = {}
            for term in self.b7:
                if term in b11.keys():
                    b12 = b11[term]
                    self.b5[value][term] = (1 + b12) / (len(self.b7) + len(self.b3[value]))
                else:
                    self.b5[value][term] = (1) / (len(self.b7) + len(self.b3[value]))
    def fonk6(self, listOfWords):
        b13 = {val: m.log(self.b4[val]) for val in self.b2.values()}
        for term in listOfWords:
            for val in self.b2.values():
                if term in self.b5[val]:
                    b13[val] += m.log(self.b5[val][term])
        return max(b13, b14 = b13.get)
    def fonk7(self, b25):
        b15 = getMailDictionary(b25[0])
        b16 = getMailDictionary(b25[1])
        b17 = sum(1 for value in b15.values() if self.fonk6(value) == "spam")
        b18 = sum(1 for value in b16.values() if self.fonk6(value) == "ham")
        b19 = (b17 / len(b15)) * 100
        b20 = (b18 / len(b16)) * 100
        b21 = ((b17 + b18) / (len(b15) + len(b16))) * 100
        print("Accuracy without removing stopwords:", b21)
    def fonk8(self, b25, b26):
        b10 = readStopWords(b26)
        b15 = getMailDictionaryWOStopWords(b25[0], b10)
        b16 = getMailDictionaryWOStopWords(b25[1], b10)
        b17 = sum(1 for value in b15.values() if self.fonk6(value) == "spam")
        b18 = sum(1 for value in b16.values() if self.fonk6(value) == "ham")
        b19 = (b17 / len(b15)) * 100
        b20 = (b18 / len(b16)) * 100
        b21 = ((b17 + b18) / (len(b15) + len(b16))) * 100
        print("Accuracy after removing stopwords:", b21)
def fonk9():
    b22 = class1(2, ["spam", "ham"])
    b23 = sys.argv
    b24 = [b23[1], b23[2]]
    b25 = [b23[3], b23[4]]
    b26 = b23[5]
    b22.fonk2(b24)
    b22.fonk4()
    b22.fonk5()
    b22.fonk7(b25)
    b27 = class1(2, ["spam", "ham"])
    b27.fonk3(b24, b26)
    b27.fonk4()
    b27.fonk5()
    b27.fonk8(b25, b26)
if b28 = = "__main__":
    fonk9()