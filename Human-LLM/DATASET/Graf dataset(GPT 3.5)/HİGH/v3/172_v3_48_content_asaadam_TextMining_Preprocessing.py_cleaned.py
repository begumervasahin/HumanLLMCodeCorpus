import string
import re
import collections
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
class class1:
    with open("b1-list.txt", "r") as f:
        b1 = f.read().split('\n')
    @staticmethod
    def fonk1(b6):
        b2 = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*', ' ', b6)
        b2 = b2.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        b2 = b2.translate(str.maketrans('', '', '1234567890'))
        b2 = re.sub('\s+', ' ', b2).strip()
        return b2
    @staticmethod
    def fonk2(b6):
        return b6.lower()
    @staticmethod
    def fonk3(b6):
        return b6.split()
    @staticmethod
    def fonk4(b6):
        return [word for word in b6 if word not in class1.b1]
    @staticmethod
    def fonk5(b6):
        return list(collections.OrderedDict.fromkeys(b6))
    @staticmethod
    def fonk6(b6):
        b3 = StemmerFactory()
        b4 = b3.create_stemmer()
        return [b4.stem(word) for word in b6]
    @staticmethod
    def fonk7(b6, b5 = True):
        b6 = class1.fonk1(b6)
        b6 = class1.fonk2(b6)
        b6 = class1.fonk3(b6)
        b6 = class1.fonk4(b6)
        if b5:
            b6 = class1.fonk5(b6)
        b6 = class1.fonk6(b6)
        return b6
b6 = "This is an example b6 with some numbers 123 and links http:
b7 = class1.fonk7(b6)
print("Processed b6 with duplicate removal:", b7)
b8 = class1.fonk7(b6, b5=False)
print("Processed b6 without duplicate removal:", b8)