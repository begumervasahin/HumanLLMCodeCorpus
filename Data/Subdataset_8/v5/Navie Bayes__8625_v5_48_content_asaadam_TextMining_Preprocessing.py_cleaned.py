import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class Preprocessing:
    stopword = open("stopword-list.txt", "r").read().split('\n')
    @staticmethod
    def cleaning(text):
        text = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*',' ', text)
        text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        text = text.translate(str.maketrans('', '', '1234567890'))
        return re.sub('\s+', ' ', text).strip()
    @staticmethod
    def case_folding(text):
        return text.casefold()
    @staticmethod
    def tokenization(text):
        return text.split()
    @staticmethod
    def filtering(text):
        return [word for word in text if word not in Preprocessing.stopword]
    @staticmethod
    def remove_duplicates(text):
        return list(collections.OrderedDict.fromkeys(text))
    @staticmethod
    def stemming(text):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        return [stemmer.stem(word) for word in text]
    @staticmethod
    def preprocess_all(text):
        text = Preprocessing.cleaning(text)
        text = Preprocessing.case_folding(text)
        text = Preprocessing.tokenization(text)
        text = Preprocessing.filtering(text)
        text = Preprocessing.remove_duplicates(text)
        text = Preprocessing.stemming(text)
        return text
    @staticmethod
    def preprocess_without_duplicates(text):
        text = Preprocessing.cleaning(text)
        text = Preprocessing.case_folding(text)
        text = Preprocessing.tokenization(text)
        text = Preprocessing.filtering(text)
        text = Preprocessing.stemming(text)
        return text