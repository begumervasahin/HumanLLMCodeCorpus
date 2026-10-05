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
    def fonk3(content):
        return re.sub(r'[^a-zA-Z0-9\s]', '', content)
    def fonk4(self, b26):
        b3 = []
        with open(b26, b4 = 'utf-8') as file:
            b5 = file.readlines()
        for line in b5:
            b3.append(self.fonk3(line.strip()))
        return b3
    def fonk5(self, text, min_word_return_size):
        b6 = []
        b7 = re.compile('[^a-zA-Z0-9_\\+\\-/]')
        for word in b7.split(text):
            b8 = word.strip().lower()
            if len(b8) > min_word_return_size and b8 != '' and not self.fonk2(b8):
                b6.append(b8)
        return b6
    def fonk6(self, b20):
        b9 = []
        for sentence in b20:
            b10 = re.sub(r'\b(' + '|'.join(self.b2) + r')\b', '|', sentence.strip().lower())
            b11 = b10.split("|")
            for phrase in b11:
                b12 = phrase.strip().lower()
                if b12 != "":
                    b9.append(b12)
        return b9
    def fonk7(self, b9):
        b13 = {}
        b14 = {}
        for phrase in b9:
            b6 = self.fonk5(phrase, 0)
            b15 = len(b6)
            b16 = b15 - 1
            for word in b6:
                b13.setdefault(word, 0)
                b13[word] += 1
                b14.setdefault(word, 0)
                b14[word] += b16
        for word in b13:
            b14[word] += b13[word]
        b17 = {}
        for word in b13:
            b17[word] = b14[word] / (b13[word] * 1.0)
        return b17
    def fonk8(self, b9, b17):
        b18 = {}
        for phrase in b9:
            b6 = self.fonk5(phrase, 0)
            b19 = sum(b17[word] for word in b6)
            b18[phrase] = b19
        return b18
    def fonk9(self, b26):
        if b26 and os.path.isfile(b26):
            b20 = self.fonk4(b26)
            b9 = self.fonk6(b20)
            b21 = self.fonk7(b9)
            b18 = self.fonk8(b9, b21)
            b22 = sorted(b18.items(), key=operator.itemgetter(1), reverse=True)
            b23 = [keyword for keyword in b22 if len(keyword[0].split()) <= 3]
            return b23
        else:
            return []
if b24 = = "__main__":
    b25 = class1()
    b26 = "your_content_file.txt"
    b27 = b25.fonk9(b26)
    print(b27)