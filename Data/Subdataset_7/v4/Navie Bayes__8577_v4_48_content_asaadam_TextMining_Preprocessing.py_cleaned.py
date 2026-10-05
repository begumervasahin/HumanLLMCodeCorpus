import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class class1:
    b1 = open("b1-list.txt", "r").read().split('\n')
    @staticmethod
    def fonk1(b4):
        b2 = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*',' ',b4)
        b3 = b2.maketrans(string.punctuation, ' ' * len(string.punctuation))
        b4 = b2.translate(b3)
        b5 = b4.translate(str.maketrans('', '', '1234567890'))
        return re.sub('\s+', ' ', b5).strip()
    @staticmethod
    def fonk2(b4):
        return str.casefold(b4)
    @staticmethod
    def fonk3(b4):
        return b4.split()
    @staticmethod
    def fonk4(b4):
        return [b4 for b4 in b4 if b4 not in class1.b1]
    @staticmethod
    def fonk5(b4):
        return list(collections.OrderedDict([(word, None) for word in b4]))
    @staticmethod
    def fonk6(b4):
        b6 = StemmerFactory()
        b7 = b6.create_stemmer()
        return [b7.stem(x) for x in b4]
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
        return class1.fonk4(
                class1.fonk6(
                    class1.fonk3(
                        class1.fonk2(
                            class1.fonk1(b4)
                        )
                    )
                )
            )