import os
import re
import operator
b1 = {
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
}
class class1:
    def fonk1(self, b2 = None):
        self.b2 = b2 or b1
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
    def fonk4(self, b25):
        b3 = []
        with open(b25, b4 = 'utf-8') as file:
            for line in file:
                b3.append(self.fonk3(line.strip()))
        return b3
    def fonk5(self, text, min_word_return_size):
        b5 = []
        b6 = re.compile('[^a-zA-Z0-9_\\+\\-/]')
        for word in b6.split(text):
            b7 = word.strip().lower()
            if len(b7) > min_word_return_size and b7 and not self.fonk2(b7):
                b5.append(b7)
        return b5
    def fonk6(self, b19):
        b8 = []
        for sentence in b19:
            b9 = re.sub(r'\b(' + '|'.join(self.b2) + r')\b', '|', sentence.strip().lower())
            b10 = b9.split("|")
            for phrase in b10:
                b11 = phrase.strip().lower()
                if b11:
                    b8.append(b11)
        return b8
    def fonk7(self, b8):
        b12 = {}
        b13 = {}
        for phrase in b8:
            b5 = self.fonk5(phrase, 0)
            b14 = len(b5)
            b15 = b14 - 1
            for word in b5:
                b12[word] = b12.get(word, 0) + 1
                b13[word] = b13.get(word, 0) + b15
                b13[word] += b12[word]
        b16 = {word: b13[word] / (b12[word] * 1.0) for word in b12}
        return b16
    def fonk8(self, b8, b16):
        b17 = {}
        for phrase in b8:
            b5 = self.fonk5(phrase, 0)
            b18 = sum(b16[word] for word in b5)
            b17[phrase] = b18
        return b17
    def fonk9(self, b25):
        if b25 and os.path.isfile(b25):
            b19 = self.fonk4(b25)
            b8 = self.fonk6(b19)
            b20 = self.fonk7(b8)
            b17 = self.fonk8(b8, b20)
            b21 = sorted(b17.items(), key=operator.itemgetter(1), reverse=True)
            b22 = [keyword for keyword in b21 if len(keyword[0].split()) <= 3]
            return b22
        else:
            return []
if b23 = = "__main__":
    b24 = class1()
    b25 = "your_content_file.txt"
    b26 = b24.fonk9(b25)
    print(b26)