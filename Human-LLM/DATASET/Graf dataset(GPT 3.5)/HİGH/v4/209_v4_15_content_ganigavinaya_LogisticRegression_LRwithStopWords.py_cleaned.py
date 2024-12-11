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
                           "theyll", "theyre", "theyve", "this", "those", "through", "to", "too",
                           "under", "until", "up", "very", "was", "wasnt", "we", "wed", "well",
                           "were", "wee", "werent", "what", "when", "where", "which", "while",
                           "who", "whom", "why", "with", "wont", "would", "wouldnt", "you",
                           "youd", "youll", "youre", "youve", "your", "yours", "yourself",
                           "yourselves"]
    def fonk2(self):
        self.fonk4()
        self.fonk5(self.b1, 1.0)
        self.fonk5(self.b2, 0.0)
    def fonk3(self, path, b15):
        with io.open(path, 'r', b9 = 'iso-8859-1') as f:
            b10 = f.readlines()
            for line in b10:
                b11 = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in b11:
                    if word not in self.b8:
                        if word in b15:
                            b15[word] += 1
                        else:
                            b15[word] = 1
    def fonk4(self):
        b12 = {}
        b13 = {}
        for b14 in [self.b1, self.b2]:
            for filename in os.listdir(b14):
                self.fonk3(os.path.join(b14, filename), b12 if b14 = = self.b1 else b13)
        self.b6 = set(list(b12.keys()) + list(b13.keys()))
        for word in self.b6:
            self.b5[word] = 0.0
    def fonk5(self, b14, classification):
        for filename in os.listdir(b14):
            b15 = {}
            self.fonk3(os.path.join(b14, filename), b15)
            self.b7.append({'fileName': os.path.join(b14, filename), 'token': b15, 'class': classification})
    def fonk6(self):
        for _ in range(500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        a3 = 0
        for b7 in self.b7:
            b16 = b7["token"]
            a4 = 1
            for token in b16:
                a4 += b16[token] * self.b5[token]
            b7["error"] = self.fonk8(a4)
            a3 += b7["error"]
    def fonk8(self, x):
        b17 = 1 + np.exp(-x)
        return 1 / b17
    def fonk9(self):
        for token in self.b5.keys():
            a5 = 0
            for b7 in self.b7:
                b16 = b7["token"]
                b18 = b7["class"]
                if token in b16:
                    b19 = b18 - b7["error"]
                    a5 += b16[token] * b19
            self.b5[token] += ((a5 * self.a1) - (self.a1 * self.a2 * self.b5[token]))
    def fonk10(self):
        b20 = os.listdir(self.b3)
        a6 = 0
        for filename in b20:
            b21 = {}
            a4 = 0
            self.fonk3(os.path.join(self.b3, filename), b21)
            for token in b21:
                if token in self.b5:
                    a4 += self.b5[token] * b21[token]
            b22 = self.fonk8(a4)
            if b22 > 0.5:
                a6 += 1
        b23 = (a6 / len(b20)) * 100
        print("Ham accuracy is ", b23)
        b24 = os.listdir(self.b4)
        a7 = 0
        for filename in b24:
            b25 = {}
            a4 = 0
            self.fonk3(os.path.join(self.b4, filename), b25)
            for token in b25:
                if token in self.b5:
                    a4 += self.b5[token] * b25[token]
            b22 = self.fonk8(a4)
            if b22 < 0.5:
                a7 += 1
        b26 = (a7 / len(b24)) * 100
        print("Spam accuracy is ", b26)
        b27 = ((a7 + a6) / (len(b20) + len(b24))) * 100
        print("Total accuracy is ", b27)
