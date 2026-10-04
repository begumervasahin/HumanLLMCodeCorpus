import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class class1:
    b1 = open("b1-list.txt", "r").read().split('\n')
    @staticmethod
    def fonk1(b4):
        b2 = re.sub(r'[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*', ' ', b4)
        b3 = b2.maketrans(string.punctuation, ' ' * len(string.punctuation))
        b4 = b2.translate(b3)
        b5 = b4.translate(str.maketrans('', '', '1234567890'))
        return re.sub(r'\s+', ' ', b5).strip()
    @staticmethod
    def fonk2(b4):
        return str.casefold(b4)
    @staticmethod
    def fonk3(b4):
        return b4.split()
    @staticmethod
    def fonk4(words):
        return [word for word in words if word not in class1.b1]
    @staticmethod
    def fonk5(words):
        return list(collections.OrderedDict.fromkeys(words))
    @staticmethod
    def fonk6(words):
        b6 = StemmerFactory()
        b7 = b6.create_stemmer()
        return [b7.stem(word) for word in words]
    @staticmethod
    def fonk7(b4):
        return class1.fonk4(
            class1.fonk6(
                class1.fonk5(
                    class1.fonk3(
                        class1.fonk2(
                            class1.fonk1(b4)
                        )
                    )
                )
            )
        )
    @staticmethod
    def fonk8(b4):
        print('preprocessing')
        print(b4)
        return class1.fonk4(
            class1.fonk6(
                class1.fonk3(
                    class1.fonk2(
                        class1.fonk1(b4)
                    )
                )
            )
        )
if b8 = = "__main__":
    b9 = "This is a sample b4 to demonstrate preprocessing. Visit www.example.com for more info!"
    b10 = class1.fonk7(b9)
    print("Preprocessed b4:", b10)