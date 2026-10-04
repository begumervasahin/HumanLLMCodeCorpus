import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class class1:
    b1 = open("b1-list.txt", "r").read().split('\n')
    @staticmethod
    def fonk1(b2):
        b2 = re.sub(r'[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil)[\S]*', ' ', b2)
        b3 = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        b2 = b2.translate(b3)
        b2 = b2.translate(str.maketrans('', '', '1234567890'))
        b2 = re.sub(r'\s+', ' ', b2).strip()
        return b2
    @staticmethod
    def fonk2(b2):
        return b2.casefold()
    @staticmethod
    def fonk3(b2):
        return b2.split()
    @staticmethod
    def fonk4(words):
        return [word for word in words if word not in class1.b1]
    @staticmethod
    def fonk5(words):
        return list(collections.OrderedDict.fromkeys(words))
    @staticmethod
    def fonk6(words):
        b4 = StemmerFactory()
        b5 = b4.create_stemmer()
        return [b5.stem(word) for word in words]
    @staticmethod
    def fonk7(b2):
        b6 = class1.fonk1(b2)
        b7 = class1.fonk2(b6)
        b8 = class1.fonk3(b7)
        b9 = class1.fonk5(b8)
        b10 = class1.fonk6(b9)
        b11 = class1.fonk4(b10)
        return b11
    @staticmethod
    def fonk8(b2):
        print('class1...')
        print(b2)
        b6 = class1.fonk1(b2)
        b7 = class1.fonk2(b6)
        b8 = class1.fonk3(b7)
        b10 = class1.fonk6(b8)
        b11 = class1.fonk4(b10)
        return b11