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
        with io.open(path, 'r', b9 = 'iso-8859-1') as file:
            b10 = file.readlines()
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
        for filename in os.listdir(self.b1):
            self.fonk3(os.path.join(self.b1, filename), b12)
        b13 = {}
        for filename in os.listdir(self.b2):
            self.fonk3(os.path.join(self.b2, filename), b13)
        self.b6 = set(b12.keys()) | set(b13.keys())
        self.b5 = {word: 0.0 for word in self.b6}
    def fonk5(self, file, classification):
        b14 = {}
        self.fonk3(file, b14)
        self.b7.append({'filename': file, 'b16': b14, 'class': classification})
    def fonk6(self):
        for _ in range(500):
            self.fonk8()
            self.fonk9()
    def fonk7(self, x):
        b15 = 1 + np.exp(-x)
        return 1 / b15
    def fonk8(self):
        for data in self.b7:
            b16 = data["b16"]
            a3 = 1
            for token, count in b16.items():
                a3 += count * self.b5[token]
            data["error"] = self.fonk7(a3)
    def fonk9(self):
        for token in self.b5.keys():
            a4 = 0
            for data in self.b7:
                b16 = data["b16"]
                b17 = data["class"]
                if token in b16:
                    b18 = b17 - data["error"]
                    a4 += b16[token] * b18
            self.b5[token] += ((a4 * self.a1) - (self.a1 * self.a2 * self.b5[token]))
    def fonk10(self):
        b19 = os.listdir(self.b3)
        a5 = 0
        for filename in b19:
            b12 = {}
            self.fonk3(os.path.join(self.b3, filename), b12)
            a3 = sum(self.b5.get(token, 0) * count for token, count in b12.items())
            b20 = self.fonk7(a3)
            if b20 > 0.5:
                a5 += 1
        b21 = (a5 / len(b19)) * 100
        print("Ham accuracy is ", b21)
        b22 = os.listdir(self.b4)
        a6 = 0
        for filename in b22:
            b13 = {}
            self.fonk3(os.path.join(self.b4, filename), b13)
            a3 = sum(self.b5.get(token, 0) * count for token, count in b13.items())
            b20 = self.fonk7(a3)
            if b20 < 0.5:
                a6 += 1
        b23 = (a6 / len(b22)) * 100
        print("Spam accuracy is ", b23)
        b24 = ((a6 + a5) / (len(b19) + len(b22))) * 100
        print("Total accuracy is ", b24)
if b25 = = "__main__":
    b1 = "train/ham"
    b2 = "train/spam"
    b3 = "test/ham"
    b4 = "test/spam"
    b26 = class1(b1, b2, b3, b4)
    b26.fonk2()
    b26.fonk10()