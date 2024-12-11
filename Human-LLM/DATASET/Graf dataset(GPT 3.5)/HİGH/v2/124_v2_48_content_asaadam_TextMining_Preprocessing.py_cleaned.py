import string
import re
import collections
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
class class1:
    with open("b1-list.txt", "r") as f:
        b1 = f.read().split('\n')
    @staticmethod
    def fonk1(b5):
        b2 = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*', ' ', b5)
        b2 = b2.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        b2 = b2.translate(str.maketrans('', '', '1234567890'))
        b2 = re.sub('\s+', ' ', b2).strip()
        return b2
    @staticmethod
    def fonk2(b5):
        return b5.lower()
    @staticmethod
    def fonk3(b5):
        return b5.split()
    @staticmethod
    def fonk4(b5):
        return [word for word in b5 if word not in class1.b1]
    @staticmethod
    def fonk5(b5):
        return list(collections.OrderedDict.fromkeys(b5))
    @staticmethod
    def fonk6(b5):
        b3 = StemmerFactory()
        b4 = b3.create_stemmer()
        return [b4.stem(word) for word in b5]
    @staticmethod
    def fonk7(b5):
        b5 = class1.fonk1(b5)
        b5 = class1.fonk2(b5)
        b5 = class1.fonk3(b5)
        b5 = class1.fonk4(b5)
        b5 = class1.fonk5(b5)
        b5 = class1.fonk6(b5)
        return b5
    @staticmethod
    def fonk8(b5):
        b5 = class1.fonk1(b5)
        b5 = class1.fonk2(b5)
        b5 = class1.fonk3(b5)
        b5 = class1.fonk4(b5)
        b5 = class1.fonk6(b5)
        return b5
b5 = "This is an example b5 with some numbers 123 and links http:
b6 = class1.fonk7(b5)
print("Processed b5 with type removal:", b6)
b7 = class1.fonk8(b5)
print("Processed b5 without type removal:", b7)