from collections import Counter
from NBHelper import *
import math as m
import sys
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
        for key, value in self.b2.items():
            b9 = get_mail_dictionary(path_array[key])
            b8[value] = len(b9)
            a1 += len(b9)
            self.b3[value] = get_vocabulary(b9)
        for key, value in b8.items():
            self.b4[key] = value / a1
    def fonk3(self, path_array, stop_word_path):
        b8 = {}
        a1 = 0
        b10 = read_stop_words(stop_word_path)
        for key, value in self.b2.items():
            b9 = get_mail_dictionary_without_stopwords(path_array[key], b10)
            b8[value] = len(b9)
            a1 += len(b9)
            self.b3[value] = get_vocabulary(b9)
        for key, value in b8.items():
            self.b4[key] = value / a1
    def fonk4(self):
        for value in self.b3.values():
            self.b6.extend(value)
        self.b7 = set(self.b6)
    def fonk5(self):
        for value in self.b2.values():
            b11 = Counter(self.b3[value])
            for term in self.b7:
                b12 = b11[term] if term in b11 else 0
                self.b5[value][term] = (1 + b12) / (len(self.b7) + len(self.b3[value]))
    def fonk6(self, word_list):
        b13 = {val: m.log(self.b4[val]) for val in self.b2.values()}
        for term in word_list:
            for val in self.b2.values():
                if term in self.b5[val]:
                    b13[val] += m.log(self.b5[val][term])
        b14 = max(b13, key=b13.get)
        return b14
    def fonk7(self, b25):
        b15 = get_mail_dictionary(b25[0])
        b16 = get_mail_dictionary(b25[1])
        b17 = sum(1 for value in b15.values() if self.fonk6(value) == "spam")
        b18 = sum(1 for value in b16.values() if self.fonk6(value) == "ham")
        b19 = (b17 / len(b15)) * 100
        b20 = (b18 / len(b16)) * 100
        b21 = ((b17 + b18) / (len(b15) + len(b16))) * 100
        print("Accuracy without removing stopwords:", b21)
    def fonk8(self, b25, stop_path):
        b10 = read_stop_words(stop_path)
        b15 = get_mail_dictionary_without_stopwords(b25[0], b10)
        b16 = get_mail_dictionary_without_stopwords(b25[1], b10)
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
    b22.fonk2(b24)
    b22.fonk4()
    b22.fonk5()
    b22.fonk7(b25)
    b26 = class1(2, ["spam", "ham"])
    b26.fonk3(b24, b23[5])
    b26.fonk4()
    b26.fonk5()
    b26.fonk8(b25, b23[5])
if b27 = = "__main__":
    fonk9()