import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class Preprocessing:
    stopword = open("stopword-list.txt", "r").read().split('\n')
    @staticmethod
    def cleaning(text):
        remove_link = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*',' ',text)
        replace_punctuation = remove_link.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = remove_link.translate(replace_punctuation)
        cleaning = text.translate(str.maketrans('', '', '1234567890'))
        return re.sub('\s+', ' ', cleaning).strip()
    @staticmethod
    def case_folding(text):
        return str.casefold(text)
    @staticmethod
    def tokenisasi(text):
        return text.split()
    @staticmethod
    def filtering(text):
        return [text for text in text if text not in Preprocessing.stopword]
    @staticmethod
    def type(text):
        return list(collections.OrderedDict([(word, None) for word in text]))
    @staticmethod
    def stemming(text):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        return [stemmer.stem(x) for x in text]
    @staticmethod
    def all_in_one(text):
        return Preprocessing.filtering(
                Preprocessing.stemming(
                    Preprocessing.type(
                        Preprocessing.tokenisasi(
                            Preprocessing.case_folding(
                                Preprocessing.cleaning(text)
                            )
                        )
                    )
                )
            )
    @staticmethod
    def all_in_one_without_type(text):
        return Preprocessing.filtering(
                Preprocessing.stemming(
                    Preprocessing.tokenisasi(
                        Preprocessing.case_folding(
                            Preprocessing.cleaning(text)
                        )
                    )
                )
            )