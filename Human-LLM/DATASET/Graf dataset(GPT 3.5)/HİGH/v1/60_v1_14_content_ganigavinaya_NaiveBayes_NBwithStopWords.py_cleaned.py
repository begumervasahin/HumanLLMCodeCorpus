import os
import re
import io
import math
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = ['HAM', 'SPAM']
        self.b6 = {'HAM': {}, 'SPAM': {}}
        self.b7 = {'HAM': 0, 'SPAM': 0}
        self.b8 = set()
        self.b9 = {}
        self.b10 = {}
        self.b11 = set([
            "a", "about", "above", "after", "again", "against", "all", "am",
            "an", "and", "any", "are", "as", "at", "be", "because", "been",
            "before", "being", "below", "between", "both", "but", "by",
            "could", "did", "do", "does", "doing", "down", "during", "each",
            "few", "for", "from", "further", "had", "has", "have", "having",
            "he", "her", "here", "hers", "him", "himself", "his", "how",
            "i", "if", "in", "into", "is", "it", "its", "itself", "me",
            "more", "most", "my", "myself", "no", "nor", "not", "of", "off",
            "on", "once", "only", "or", "other", "our", "ours", "ourselves",
            "out", "over", "own", "same", "she", "should", "so", "some", "such",
            "than", "that", "the", "their", "theirs", "them", "themselves",
            "then", "there", "these", "they", "this", "those", "through", "to",
            "too", "under", "until", "up", "very", "was", "we", "were", "what",
            "when", "where", "which", "while", "who", "whom", "why", "with",
            "you", "your", "yours", "yourself", "yourselves"
        ])
    def fonk2(self, text):
        b12 = re.sub("[^a-zA-Z\s]", "", text).lower()
        b13 = b12.split()
        b13 = [word for word in b13 if word not in self.b11]
        return b13
    def fonk3(self):
        for category in self.b5:
            b14 = self.b1 if category == 'HAM' else self.b2
            b15 = os.listdir(b14)
            for file_name in b15:
                with io.open(os.b14.join(b14, file_name), 'r', b16 = 'iso-8859-1') as file:
                    b13 = self.fonk2(file.read())
                    for word in b13:
                        if word not in self.b8:
                            self.b8.add(word)
                        if word in self.b6[category]:
                            self.b6[category][word] += 1
                        else:
                            self.b6[category][word] = 1
                        self.b7[category] += 1
        b17 = sum(len(os.listdir(b14)) for b14 in [self.b1, self.b2])
        for category in self.b5:
            b14 = self.b1 if category == 'HAM' else self.b2
            self.b9[category] = len(os.listdir(b14)) / b17
        b18 = len(self.b8)
        for word in self.b8:
            self.b10[word] = {}
            for category in self.b5:
                b19 = self.b6[category].get(word, 0)
                self.b10[word][category] = (b19 + 1) / (self.b7[category] + b18)
    def fonk4(self, text):
        b13 = set(self.fonk2(text))
        b20 = {}
        for category in self.b5:
            b20[category] = math.log(self.b9[category], 2)
            for word in b13:
                if word in self.b8:
                    b20[category] += math.log(self.b10[word][category], 2)
        return 'HAM' if b20['HAM'] > b20['SPAM'] else 'SPAM'
    def fonk5(self):
        b21 = {}
        for category in ['HAM', 'SPAM']:
            b14 = self.b3 if category == 'HAM' else self.b4
            a1 = 0
            b15 = os.listdir(b14)
            for file_name in b15:
                with io.open(os.b14.join(b14, file_name), 'r', b16 = 'iso-8859-1') as file:
                    b22 = self.fonk4(file.read())
                    if b22 = = category:
                        a1 += 1
            b23 = a1 / len(b15) * 100
            b21[category] = b23
            print(f"{category} test b23: {b23:.2f}%")
        b24 = sum(b21.values()) / 2
        print(f"Total test b23: {b24:.2f}%")
if b25 = = "__main__":
    b26 = class1("b14/to/training/ham", "b14/to/training/spam", "b14/to/test/ham", "b14/to/test/spam")
    b26.fonk3()
    b26.fonk5()