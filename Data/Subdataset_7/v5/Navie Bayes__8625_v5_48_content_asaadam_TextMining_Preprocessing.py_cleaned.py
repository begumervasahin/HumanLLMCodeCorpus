import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class class1:
    b1 = open("b1-list.txt", "r").read().split('\n')
    @staticmethod
    def fonk1(b2):
        b2 = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*',' ', b2)
        b2 = b2.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        b2 = b2.translate(str.maketrans('', '', '1234567890'))
        return re.sub('\s+', ' ', b2).strip()
    @staticmethod
    def fonk2(b2):
        return b2.casefold()
    @staticmethod
    def fonk3(b2):
        return b2.split()
    @staticmethod
    def fonk4(b2):
        return [word for word in b2 if word not in class1.b1]
    @staticmethod
    def fonk5(b2):
        return list(collections.OrderedDict.fromkeys(b2))
    @staticmethod
    def fonk6(b2):
        b3 = StemmerFactory()
        b4 = b3.create_stemmer()
        return [b4.stem(word) for word in b2]
    @staticmethod
    def fonk7(b2):
        b2 = class1.fonk1(b2)
        b2 = class1.fonk2(b2)
        b2 = class1.fonk3(b2)
        b2 = class1.fonk4(b2)
        b2 = class1.fonk5(b2)
        b2 = class1.fonk6(b2)
        return b2
    @staticmethod
    def fonk8(b2):
        b2 = class1.fonk1(b2)
        b2 = class1.fonk2(b2)
        b2 = class1.fonk3(b2)
        b2 = class1.fonk4(b2)
        b2 = class1.fonk6(b2)
        return b2