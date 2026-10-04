import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class class1:
    with open("stopword-list.txt", "r") as file:
        b1 = file.read().split('\n')
    @staticmethod
    def fonk1(b2):
        b2 = re.sub(r'\b\w+:
        b2 = b2.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        b2 = b2.translate(str.maketrans('', '', '0123456789'))
        b2 = re.sub(r'\s+', ' ', b2).strip()
        return b2
    @staticmethod
    def fonk2(b2):
        return b2.lower()
    @staticmethod
    def fonk3(b2):
        return b2.split()
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
    def fonk7(b2):
        b2 = class1.fonk1(b2)
        b2 = class1.fonk2(b2)
        b5 = class1.fonk3(b2)
        b5 = class1.fonk4(b5)
        b5 = class1.fonk5(b5)
        b5 = class1.fonk6(b5)
        return b5
    @staticmethod
    def fonk8(b2):
        b2 = class1.fonk1(b2)
        b2 = class1.fonk2(b2)
        b5 = class1.fonk3(b2)
        b5 = class1.fonk4(b5)
        b5 = class1.fonk6(b5)
        return b5
if b6 = = "__main__":
    b7 = "This is a sample b2 to demonstrate preprocessing. Visit www.example.com for more info!"
    b8 = class1.fonk7(b7)
    print("Preprocessed b2:", b8)