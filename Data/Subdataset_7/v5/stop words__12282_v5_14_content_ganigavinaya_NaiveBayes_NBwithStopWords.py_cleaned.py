import os
import re
import io
import math
class class1:
    def fonk1(self, b1, b2, b8, b9):
        self.b1 = b1
        self.b2 = b2
        self.a1 = 0
        self.a2 = 1
        self.b3 = []
        self.b4 = {}
        self.a3 = 0
        self.b5 = {}
        self.a4 = 0
        self.b6 = {}
        self.b7 = {}
        self.b8 = b8
        self.b9 = b9
        self.b10 = ["a", "about", "above", "after", "again", "against", "all", "am",
                           "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before",
                           "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
                           "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few",
                           "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he",
                           "he'd", "he'll", "he", "her", "here", "here", "hers", "herself", "him", "himself", "his",
                           "how", "how's", "i", "i'd", "i'll", "i", "ie", "if", "in", "into", "is", "isn't", "it", "it",
                           "it's", "itself", "let", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not",
                           "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out",
                           "over", "own", "same", "shan't", "she", "she'd", "she'll", "she", "should", "shouldn't",
                           "so", "some", "such", "than", "that", "that", "the", "their", "theirs", "them", "themselves",
                           "then", "there", "there", "these", "they", "they'd", "they'll", "they're", "they've", "this",
                           "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd",
                           "we'll", "were", "we", "we're", "weren't", "what", "what", "when", "when", "where",
                           "where", "which", "while", "who", "who", "whom", "why", "why", "with", "won't", "would",
                           "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves",
                           "nt", "d", "ll", "re", "ve", "r", "t", "nd", "s"]
    def fonk2(self, b17):
        b11 = self.b1 if b17 == self.a1 else self.b2
        b12 = os.listdir(b11)
        b13 = {}
        a5 = 0
        for file_name in b12:
            with io.open(os.b27.join(b11, file_name), 'r', b14 = 'iso-8859-1') as file:
                b15 = file.readlines()
                for line in b15:
                    b16 = re.sub("[^a-zA-Z\s]", "", line).lower().split()
                    for word in b16:
                        if word not in self.b10:
                            b13[word] = b13.get(word, 0) + 1
                            a5 += 1
        self.b3 = list(set(self.b3 + list(b13.keys())))
        if b17 = = self.a1:
            self.b4 = b13
            self.a3 += a5
        else:
            self.b5 = b13
            self.a4 += a5
    def fonk3(self):
        for word in self.b3:
            b18 = self.b4.get(word, 0) + 1
            b19 = self.b5.get(word, 0) + 1
            self.b7[word] = [(b18 / self.a3), (b19 / self.a4)]
    def fonk4(self):
        self.fonk2(self.a1)
        self.fonk2(self.a2)
    def fonk5(self):
        b20 = len(os.listdir(self.b1))
        b21 = len(os.listdir(self.b2))
        b22 = b20 + b21
        self.b6[self.a1] = b20 / b22
        self.b6[self.a2] = b21 / b22
        self.fonk3()
    def fonk6(self, b27):
        a6 = 0
        b23 = os.listdir(b27)
        for file_name in b23:
            with io.open(os.b27.join(b27, file_name), 'r', b14 = 'iso-8859-1') as file:
                b24 = file.read().lower()
                b16 = re.sub("[^a-zA-Z\s]", "", b24)
                b25 = set(b16.split())
                b26 = {self.a1: math.log2(self.b6[self.a1]), self.a2: math.log2(self.b6[self.a2])}
                for word in b25:
                    if word in self.b3:
                        b26[self.a1] += math.log2(self.b7[word][self.a1])
                        b26[self.a2] += math.log2(self.b7[word][self.a2])
                if b26[self.a1] > b26[self.a2]:
                    if b27 = = self.b8:
                        a6 += 1
                else:
                    if b27 = = self.b9:
                        a6 += 1
        return a6
    def fonk7(self):
        b28 = self.fonk6(self.b8)
        b29 = len(os.listdir(self.b8))
        b30 = (b28 / b29) * 100
        print("Ham test b31 = {:.2f}%".format(b30))
        b32 = self.fonk6(self.b9)
        b33 = len(os.listdir(self.b9))
        b34 = (b32 / b33) * 100
        print("Spam test b31 = {:.2f}%".format(b34))
        b35 = b29 + b33
        b36 = b28 + b32
        b37 = (b36 / b35) * 100
        print("Total test b31 = {:.2f}%".format(b37))
if b38 = = "__main__":
    b39 = class1("path_to_training_ham", "path_to_training_spam", "path_to_test_ham", "path_to_test_spam")
    b39.fonk4()
    b39.fonk5()
    b39.fonk7()