import re
import string
import unicodedata
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from syntactic_unit import SyntacticUnit
class class1:
    def fonk1(self):
        self.b1 = class1.fonk8(b10="../stopwords.txt")
        self.b2 = WordNetLemmatizer()
        self.b3 = SnowballStemmer("english")
        self.b4 = re.compile('([%s])+' % re.escape(string.punctuation), re.UNICODE)
        self.b5 = re.compile(r"[0-9]+", re.UNICODE)
        self.b6 = re.compile('(((?![\d])\w)+)', re.UNICODE)
    def fonk2(self, s):
        return self.b4.sub(" ", s)
    def fonk3(self, s):
        return self.b5.sub("", s)
    def fonk4(self, b8):
        return [w for w in b8 if w not in self.b1]
    def fonk5(self, b8):
        return [self.b3.stem(word) for word in b8]
    def fonk6(self, b8):
        if not b8:
            return []
        if isinstance(b8[0], str):
            b7 = pos_tag(b8)
        else:
            b7 = b8
        b8 = [self.b2.lemmatize(word[0]) if not class1.fonk9(word[1])
                  else self.b2.lemmatize(word[0], b9 = class1.fonk9(word[1]))
                  for word in b7]
        return b8
    def fonk7(self, b8):
        if isinstance(b8, str):
            b8 = self.fonk12(b8)
        return pos_tag(b8)
    @staticmethod
    def fonk8(b10 = "stopwords.txt"):
        return list(set(stopwords.words('english')))
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
    def fonk10(s):
        b11 = unicodedata.normalize("NFD", s)
        b12 = "".join(ch for ch in b11 if unicodedata.category(ch) != 'Mn')
        return unicodedata.normalize("NFC", b12)
    def fonk11(self, b14, b13 = None, stem=False):
        b14 = b14.lower()
        b14 = self.fonk10(b14)
        b14 = self.fonk3(b14)
        b14 = self.fonk2(b14)
        b15 = [match.group() for match in self.b6.finditer(b14)]
        b16 = self.fonk4(b15)
        b7 = pos_tag(b16)
        if stem:
            b16 = self.fonk5(b16)
        else:
            b16 = self.fonk6(b7)
        b17 = []
        if not b13:
            b13 = ['N', 'J']
        for i in range(len(b16)):
            if not b7[i][1].startswith('N') or len(b16[i]) < 3:
                continue
            b18 = b16[i]
            b14 = b16[i]
            b19 = b7[i][1]
            b20 = SyntacticUnit(b14, b18, b19)
            b20.b21 = i
            b17.append(b20)
        return {unit.b14: unit for unit in b17}
    def fonk12(self, b14):
        b14 = b14.lower()
        b14 = self.fonk10(b14)
        return [match.group() for match in self.b6.finditer(b14)]
    def fonk13(self, b14):
        b14 = b14.lower()
        b14 = self.fonk10(b14)
        b14 = self.fonk3(b14)
        b14 = self.fonk2(b14)
        return b14