import os
import re
import operator
b1 = set([
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
    "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do",
    "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
    "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's",
    "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours",
    "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such",
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these",
    "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until",
    "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's",
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd",
    "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
])
class class1:
    def fonk1(self, b2 = None):
        self.b2 = b2 if b2 else b1
    @staticmethod
    def fonk2(s):
        try:
            float(s) if '.' in s else int(s)
            return True
        except ValueError:
            return False
    @staticmethod
    def fonk3(b5):
        return re.sub(r'[^a-zA-Z0-9\s]', '', b5)
    def fonk4(self, b28):
        b3 = []
        with open(b28, b4 = 'utf-8') as file:
            b5 = file.readlines()
        b5 = [x.strip() for x in b5]
        for line in b5:
            b3.append(self.fonk3(line))
        return b3
    def fonk5(self, text, min_word_return_size):
        b6 = re.compile('[^a-zA-Z0-9_\\+\\-/]')
        b7 = []
        for single_word in b6.split(text):
            b8 = single_word.strip().lower()
            if len(b8) > min_word_return_size and b8 != '' and not self.fonk2(b8):
                b7.append(b8)
        return b7
    def fonk6(self, text):
        b9 = re.compile(u'[.!?;:\t\\\\"\\(\\)\\\u2019\u2013]|\\s\\-\\s')
        b10 = b9.split(text)
        return b10
    def fonk7(self, b22):
        b11 = []
        for s in b22:
            b12 = re.sub(r'\b(' + '|'.join(self.b2) + r')\b', '|', s.strip().lower())
            b13 = b12.split("|")
            for b14 in b13:
                b14 = b14.strip().lower()
                if b14 != "":
                    b11.append(b14)
        return b11
    def fonk8(self, b11):
        b15 = {}
        b16 = {}
        for b14 in b11:
            b17 = self.fonk5(b14, 0)
            b18 = len(b17)
            b19 = b18 - 1
            for word in b17:
                b15.setdefault(word, 0)
                b15[word] += 1
                b16.setdefault(word, 0)
                b16[word] += b19
        for item in b15:
            b16[item] = b16[item] + b15[item]
        b20 = {}
        for item in b15:
            b20.setdefault(item, 0)
            b20[item] = b16[item] / (b15[item] * 1.0)
        return b20
    def fonk9(self, b11, b20):
        b21 = {}
        for b14 in b11:
            b21.setdefault(b14, 0)
            b17 = self.fonk5(b14, 0)
            a1 = 0
            for word in b17:
                a1 += b20[word]
            b21[b14] = a1
        return b21
    def fonk10(self, b28):
        if b28 and os.path.isfile(b28):
            b22 = self.fonk4(b28)
            b11 = self.fonk7(b22)
            b23 = self.fonk8(b11)
            b21 = self.fonk9(b11, b23)
            b24 = sorted(b21.items(), key=operator.itemgetter(1), reverse=True)
            b25 = [word for word in b24 if len(word[0].split()) <= 3]
            return b25
        else:
            return []
if b26 = = "__main__":
    b27 = class1()
    b28 = "your_content_file.txt"
    b29 = b27.fonk10(b28)
    print(b29)