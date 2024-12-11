from collections import Counter
from NBHelper import *
import math as m
import sys
class class1:
    def fonk1(self, b1, class_names):
        self.b1 = b1
        self.b2 = {}
        self.b3 = {}
        self.b4 = {}
        self.b5 = {}
        self.b6 = []
        self.b7 = set()
        for i in range(b1):
            self.b2[i] = class_names[i]
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
                if term in b11:
                    b12 = b11[term]
                    self.b5[value][term] = (1 + b12) / (len(self.b7) + len(self.b3[value]))
                else:
                    self.b5[value][term] = 1 / (len(self.b7) + len(self.b3[value]))
    def fonk6(self, word_list):
        b13 = {}
        for val in self.b2.values():
            b13[val] = m.log(self.b4[val])
        for term in word_list:
            for val in self.b2.values():
                if term in self.b5[val]:
                    b13[val] += m.log(self.b5[val][term])
        b14 = max(b13, key=b13.get)
        return b14
    def fonk7(self, b23):
        b15 = get_mail_dictionary(b23[0])
        b16 = get_mail_dictionary(b23[1])
        a2 = 0
        a3 = 0
        for key, value in b15.items():
            if self.fonk6(value) == "spam":
                a2 += 1
        for key, value in b16.items():
            if self.fonk6(value) == "ham":
                a3 += 1
        b17 = (a2 / len(b15)) * 100
        b18 = (a3 / len(b16)) * 100
        b19 = ((a2 + a3) / (len(b15) + len(b16))) * 100
        print("Accuracy without removing stopwords:", b19)
    def fonk8(self, b23, stop_path):
        b10 = read_stop_words(stop_path)
        b15 = get_mail_dictionary_without_stopwords(b23[0], b10)
        b16 = get_mail_dictionary_without_stopwords(b23[1], b10)
        a2 = 0
        a3 = 0
        for key, value in b15.items():
            if self.fonk6(value) == "spam":
                a2 += 1
        for key, value in b16.items():
            if self.fonk6(value) == "ham":
                a3 += 1
        b17 = (a2 / len(b15)) * 100
        b18 = (a3 / len(b16)) * 100
        b19 = ((a2 + a3) / (len(b15) + len(b16))) * 100
        print("Accuracy after removing stopwords:", b19)
def fonk9():
    b20 = class1(2, ["spam", "ham"])
    b21 = sys.argv
    b22 = [b21[1], b21[2]]
    b23 = [b21[3], b21[4]]
    b20.fonk2(b22)
    b20.fonk4()
    b20.fonk5()
    b20.fonk7(b23)
    b24 = class1(2, ["spam", "ham"])
    b24.fonk3(b22, b21[5])
    b24.fonk4()
    b24.fonk5()
    b24.fonk8(b23, b21[5])
if b25 = = "__main__":
    fonk9()