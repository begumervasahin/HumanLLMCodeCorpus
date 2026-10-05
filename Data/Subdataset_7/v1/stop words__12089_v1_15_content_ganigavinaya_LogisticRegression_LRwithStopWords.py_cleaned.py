import os
import io
import re
import numpy as np
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = {}
        self.b6 = []
        self.a1 = 0.0001
        self.a2 = 5
        self.b7 = []
        self.b8 = ["a", "about", "above", "after", "again", "against", "all", "am",
                           "an", "and", "any", "are", "arent", "as", "at", "be", "because",
                           "been", "before", "being", "below", "between", "both", "but",
                           "by", "cant", "cannot", "could", "couldnt", "did", "didnt", "do",
                           "does", "doesnt", "doing", "dont", "down", "during", "each", "few",
                           "for", "from", "further", "had", "hadnt", "has", "hasnt", "have",
                           "havent", "having", "he", "hed", "hell", "he", "her", "here", "here",
                           "hers", "herself", "him", "himself", "his", "how", "hows", "i", "id",
                           "ill", "i", "ie", "if", "in", "into", "is", "isnt", "it", "it", "its",
                           "itself", "let", "me", "more", "most", "mustnt", "my", "myself", "no",
                           "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
                           "our", "ours", "ourselves", "out", "over", "own", "same", "shant",
                           "she", "shed", "shell", "she", "should", "shouldnt", "so", "some",
                           "such", "than", "that", "that", "the", "their", "theirs", "them",
                           "themselves", "then", "there", "there", "these", "they", "theyd",
                           "theyll", "theyre", "theye", "this", "those", "through", "to", "too",
                           "under", "until", "up", "very", "was", "wasnt", "we", "wed", "well",
                           "were", "wee", "werent", "what", "when", "where", "which", "while",
                           "who", "whom", "why", "with", "wont", "would", "wouldnt", "you",
                           "youd", "youll", "youre", "youve", "your", "yours", "yourself",
                           "yourselves"]
    def fonk2(self):
        self.fonk4()
        self.fonk6()
    def fonk3(self, path, b14):
        with io.open(path, 'r', b9 = 'iso-8859-1') as f:
            b10 = f.readlines()
            for line in b10:
                b11 = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in b11:
                    if word not in self.b8:
                        if word in b14:
                            b14[word] += 1
                        else:
                            b14[word] = 1
    def fonk4(self):
        b12 = {}
        for each in os.listdir(self.b1):
            self.fonk3(os.path.join(self.b1, each), b12)
        b13 = {}
        for each in os.listdir(self.b2):
            self.fonk3(os.path.join(self.b2, each), b13)
        self.b6 = set(b12.keys()) | set(b13.keys())
        self.b5 = {word: 0.0 for word in self.b6}
    def fonk5(self, file, classification):
        b14 = {}
        self.fonk3(file, b14)
        self.b7.append({'fileName': file, 'b15': b14, 'class': classification})
    def fonk6(self):
        for _ in range(500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        for eachFile in self.b7:
            b15 = eachFile["b15"]
            a3 = 1
            for everyToken in b15:
                a3 += b15[everyToken] * self.b5[everyToken]
            eachFile["error"] = self.fonk8(a3)
    def fonk8(self, x):
        b16 = 1 + np.exp(-x)
        return 1 / b16
    def fonk9(self):
        for b15 in self.b5.keys():
            a4 = 0
            for eachFile in self.b7:
                b17 = eachFile["b15"]
                b18 = eachFile["class"]
                if b15 in b17:
                    b19 = b18 - eachFile["error"]
                    a4 += b17[b15] * b19
            self.b5[b15] += ((a4 * self.a1) - (self.a1 * self.a2 * self.b5[b15]))
    def fonk10(self):
        b20 = os.listdir(self.b3)
        a5 = 0
        for each in b20:
            b21 = {}
            self.fonk3(os.path.join(self.b3, each), b21)
            a3 = sum(self.b5.get(b15, 0) * count for b15, count in b21.items())
            b22 = self.fonk8(a3)
            if b22 > 0.5:
                a5 += 1
        b23 = (a5 / len(b20)) * 100
        print("Ham accuracy is ", b23)
        b24 = os.listdir(self.b4)
        a6 = 0
        for each in b24:
            b25 = {}
            self.fonk3(os.path.join(self.b4, each), b25)
            a3 = sum(self.b5.get(b15, 0) * count for b15, count in b25.items())
            b22 = self.fonk8(a3)
            if b22 < 0.5:
                a6 += 1
        b26 = (a6 / len(b24)) * 100
        print("Spam accuracy is ", b26)
        b27 = ((a6 + a5) / (len(b20) + len(b24))) * 100
        print("Total accuracy is ", b27)
if b28 = = "__main__":
    b29 = "train/ham"
    b30 = "train/spam"
    b31 = "test/ham"
    b32 = "test/spam"
    b33 = class1(b29, b30, b31, b32)
    b33.fonk2()
    b33.fonk10()