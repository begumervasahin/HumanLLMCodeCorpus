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
        self.b6 = set()
        self.a1 = 0.0001
        self.a2 = 5
        self.b7 = []
        self.b8 = [
            "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "arent",
            "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "cant",
            "cannot", "could", "couldnt", "did", "didnt", "do", "does", "doesnt", "doing", "dont", "down", "during",
            "each", "few", "for", "from", "further", "had", "hadnt", "has", "hasnt", "have", "havent", "having",
            "he", "hed", "hell", "he", "her", "here", "here", "hers", "herself", "him", "himself", "his", "how",
            "hows", "i", "id", "ill", "i", "ie", "if", "in", "into", "is", "isnt", "it", "it", "its", "itself",
            "let", "me", "more", "most", "mustnt", "my", "myself", "no", "nor", "not", "of", "off", "on", "once",
            "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shant", "she",
            "shed", "shell", "she", "should", "shouldnt", "so", "some", "such", "than", "that", "that", "the", "their",
            "theirs", "them", "themselves", "then", "there", "there", "these", "they", "theyd", "theyll", "theyre",
            "theyve", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasnt", "we",
            "wed", "well", "were", "wee", "werent", "what", "when", "where", "which", "while", "who", "whom", "why",
            "with", "wont", "would", "wouldnt", "you", "youd", "youll", "youre", "youve", "your", "yours", "yourself",
            "yourselves"
        ]
    def fonk2(self):
        self.fonk4()
        self.fonk5(self.b1, 1.0)
        self.fonk5(self.b2, 0.0)
    def fonk3(self, path):
        b9 = {}
        with io.open(path, 'r', b10 = 'iso-8859-1') as f:
            b11 = f.readlines()
            for line in b11:
                b12 = re.findall(r'\b\w+\b', line.lower())
                for word in b12:
                    if word not in self.b8:
                        b9[word] = b9.get(word, 0) + 1
        return b9
    def fonk4(self):
        b13 = {}
        b14 = {}
        for b15 in [self.b1, self.b2]:
            for filename in os.listdir(b15):
                b9 = self.fonk3(os.path.join(b15, filename))
                if b15 = = self.b1:
                    b13.update(b9)
                else:
                    b14.update(b9)
        self.b6.update(b13.keys(), b14.keys())
        self.b5 = {word: 0.0 for word in self.b6}
    def fonk5(self, b15, classification):
        for filename in os.listdir(b15):
            b9 = self.fonk3(os.path.join(b15, filename))
            self.b7.append({'fileName': os.path.join(b15, filename), 'token': b9, 'class': classification})
    def fonk6(self):
        for _ in range(500):
            self.fonk7()
            self.fonk9()
    def fonk7(self):
        for b7 in self.b7:
            b16 = b7["token"]
            a3 = 1
            for token, count in b16.items():
                a3 += count * self.b5[token]
            b7["error"] = self.fonk8(a3)
    def fonk8(self, x):
        return 1 / (1 + np.exp(-x))
    def fonk9(self):
        for token in self.b5.keys():
            b17 = sum(b7["token"].get(token, 0) * (b7["class"] - b7["error"]) for b7 in self.b7)
            self.b5[token] += (b17 * self.a1) - (self.a1 * self.a2 * self.b5[token])
    def fonk10(self):
        b18 = sum(1 for filename in os.listdir(self.b3) if self.fonk11(os.path.join(self.b3, filename)) > 0.5)
        b19 = (b18 / len(os.listdir(self.b3))) * 100
        print("Ham accuracy is ", b19)
        b20 = sum(1 for filename in os.listdir(self.b4) if self.fonk11(os.path.join(self.b4, filename)) < 0.5)
        b21 = (b20 / len(os.listdir(self.b4))) * 100
        print("Spam accuracy is ", b21)
        b22 = ((b18 + b20) / (len(os.listdir(self.b3)) + len(os.listdir(self.b4)))) * 100
        print("Total accuracy is ", b22)
    def fonk11(self, file_path):
        b9 = self.fonk3(file_path)
        a3 = 1
        for token, count in b9.items():
            if token in self.b5:
                a3 += count * self.b5[token]
        return self.fonk8(a3)
