import re
import string
import unicodedata
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import b1
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from syntactic_unit import SyntacticUnit
class class1:
    def fonk1(self):
        self.b1 = self.fonk8(b11="../b1.txt")
        self.b2 = WordNetLemmatizer()
        self.b3 = SnowballStemmer("english")
        self.b4 = re.compile('([%s])+' % re.escape(string.punctuation), re.UNICODE)
        self.b5 = re.compile(r"[0-9]+", re.UNICODE)
        self.b6 = re.compile('(((?![\d])\w)+)', re.UNICODE)
    def fonk2(self, b15):
        return self.b4.sub(" ", b15)
    def fonk3(self, b15):
        return self.b5.sub("", b15)
    def fonk4(self, b10):
        return [word for word in b10 if word not in self.b1]
    def fonk5(self, b10):
        return [self.b3.stem(word) for word in b10]
    def fonk6(self, b10):
        if not b10:
            return []
        if isinstance(b10[0], str):
            b7 = pos_tag(b10)
        else:
            b7 = b10
        b8 = [
            self.b2.lemmatize(word[0]) if not self.fonk9(word[1])
            else self.b2.lemmatize(word[0], b9 = self.fonk9(word[1]))
            for word in b7
        ]
        return b8
    def fonk7(self, b10):
        if isinstance(b10, str):
            b10 = self.fonk12(b10)
        return pos_tag(b10)
    @staticmethod
    def fonk8(b11 = "b1.txt"):
        return list(set(b1.words('english')))
    @staticmethod
    def fonk9(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None
    @staticmethod
    def fonk10(b15):
        b12 = unicodedata.normalize("NFD", b15)
        b13 = "".join(ch for ch in b12 if unicodedata.category(ch) != 'Mn')
        return unicodedata.normalize("NFC", b13)
    def fonk11(self, b15, b14 = None, stem=False):
        b15 = b15.lower()
        b15 = self.fonk10(b15)
        b15 = self.fonk3(b15)
        b15 = self.fonk2(b15)
        b16 = [match.group() for match in self.b6.finditer(b15)]
        b17 = self.fonk4(b16)
        b7 = pos_tag(b17)
        if stem:
            b17 = self.fonk5(b17)
        else:
            b17 = self.fonk6(b7)
        b18 = [
            SyntacticUnit(word, word, tag)
            for i, (word, tag) in enumerate(b7)
            if tag.startswith('N') and len(b17[i]) >= 3
        ]
        return {unit.b15: unit for unit in b18}
    def fonk12(self, b15):
        b15 = b15.lower()
        b15 = self.fonk10(b15)
        return [match.group() for match in self.b6.finditer(b15)]
    def fonk13(self, b15):
        b15 = b15.lower()
        b15 = self.fonk10(b15)
        b15 = self.fonk3(b15)
        b15 = self.fonk2(b15)
        return b15