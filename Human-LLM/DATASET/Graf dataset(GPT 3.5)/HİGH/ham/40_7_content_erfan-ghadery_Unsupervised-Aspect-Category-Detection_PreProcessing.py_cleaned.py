from __future__ import unicode_literals
import string
import pandas as pd
import codecs
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
pd.set_option('display.width', 2000)
class class1:
    b1 = None
    b2 = None
    def fonk1(self,b1,language):
        self.b1 = b1
        self.b2 = language
    def fonk2(self):
        if self.b2 = = 'persian':
            a1 = 1
            for i in range(len(self.b1)):
                a1 += 1
                try:
                    b3 = self.b1.loc[i, 'Text']
                    b4 = [char for char in b3 if char not in string.punctuation]
                    b4 = ''.join(b4)
                    self.b1.loc[i, 'Text'] = b4
                except:
                    pass
            return self.b1
        else:
            for i in range(len(self.b1)):
                try:
                    b3 = self.b1[i]
                    b5 = str.maketrans(string.punctuation, ' '*len(string.punctuation))
                    self.b1[i] = b3.translate(b5)
                except:
                    pass
            return self.b1
    def fonk3(self):
        b6 = '../stopwords-persian'
        b7 = set(stopwords.b11(self.b2))
        if self.b2 = = 'persian':
            b8 = codecs.open(b6, encoding='utf-8')
            b6 = b8.read()
            a1 = 1
            for i in range(len(self.b1)):
                a1 += 1
                try:
                    b9 = (self.b1.loc[i, 'Text']).split()
                    b10 = [word for word in b9 if word not in b6.split()]
                    b10 = ' '.join(b10)
                    self.b1.loc[i, 'Text'] = b10
                except:
                    pass
        for i in range(len(self.b1)):
            try:
                b11 = word_tokenize(self.b1[i])
                b12 = [word for word in b11 if word not in b7]
                b12 = ' '.join(b12)
                self.b1[i] = b12
            except:
                pass
        return self.b1