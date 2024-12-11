from collections import Counter
import math as m
import sys
from NBHelper import *
class class1:
    def fonk1(self, b1, class_names):
        self.b1 = b1
        self.b2 = {i: class_names[i] for i in range(b1)}
        self.b3 = {}
        self.b4 = {}
        self.b5 = {}
        self.b6 = []
        self.b7 = set()
    def fonk2(self, path_array):
        b8 = {}
        a1 = 0
        for b14, value in self.b2.items():
            b9 = getMailDictionary(path_array[b14])
            b8[value] = len(b9)
            a1 += len(b9)
            self.b3[value] = getVocabulary(b9)
        for b14, value in b8.items():
            self.b4[b14] = b8[b14] / a1
    def fonk3(self, path_array, stop_word_path):
        b8 = {}
        a1 = 0
        b10 = readStopWords(stop_word_path)
        for b14, value in self.b2.items():
            b9 = getMailDictionaryWOStopWords(path_array[b14], b10)
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
                if term in b11:
                    b12 = b11[term]
                    self.b5[value][term] = (1 + b12) / (len(self.b7) + len(self.b3[value]))
                else:
                    self.b5[value][term] = 1 / (len(self.b7) + len(self.b3[value]))
    def fonk6(self, words):
        b13 = {val: m.log(self.b4[val]) for val in self.b2.values()}
        for term in words:
            for val in self.b2.values():
                if term in self.b5[val]:
                    b13[val] += m.log(self.b5[val][term])
        return max(b13, b14 = b13.get)
    def fonk7(self, b26):
        b15 = getMailDictionary(b26[0])
        b16 = getMailDictionary(b26[1])
        b17 = sum(1 for value in b15.values() if self.fonk6(value) == "spam")
        b18 = sum(1 for value in b16.values() if self.fonk6(value) == "ham")
        b19 = len(b15)
        b20 = len(b16)
        b21 = b17 + b18
        a1 = b19 + b20
        b22 = (b21 / a1) * 100
        print("Accuracy without removing stopwords:", b22)
    def fonk8(self, b26, b27):
        b10 = readStopWords(b27)
        b15 = getMailDictionaryWOStopWords(b26[0], b10)
        b16 = getMailDictionaryWOStopWords(b26[1], b10)
        b17 = sum(1 for value in b15.values() if self.fonk6(value) == "spam")
        b18 = sum(1 for value in b16.values() if self.fonk6(value) == "ham")
        b19 = len(b15)
        b20 = len(b16)
        b21 = b17 + b18
        a1 = b19 + b20
        b22 = (b21 / a1) * 100
        print("Accuracy after removing stopwords:", b22)
def fonk9():
    b23 = class1(2, ["spam", "ham"])
    b24 = sys.argv
    b25 = [b24[1], b24[2]]
    b26 = [b24[3], b24[4]]
    b27 = b24[5]
    b23.fonk2(b25)
    b23.fonk4()
    b23.fonk5()
    b23.fonk7(b26)
    b28 = class1(2, ["spam", "ham"])
    b28.fonk3(b25, b27)
    b28.fonk4()
    b28.fonk5()
    b28.fonk8(b26, b27)
if b29 = = "__main__":
    fonk9()