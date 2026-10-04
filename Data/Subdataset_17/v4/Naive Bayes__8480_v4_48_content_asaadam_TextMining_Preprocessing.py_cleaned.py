import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class Preprocessing:
    stopword = open("stopword-list.txt", "r").read().split('\n')
    @staticmethod
    def cleaning(text):
        text = re.sub(r'[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil)[\S]*', ' ', text)
        replace_punctuation = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = text.translate(replace_punctuation)
        text = text.translate(str.maketrans('', '', '1234567890'))
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    @staticmethod
    def case_folding(text):
        return text.casefold()
    @staticmethod
    def tokenisasi(text):
        return text.split()
    @staticmethod
    def filtering(words):
        return [word for word in words if word not in Preprocessing.stopword]
    @staticmethod
    def type(words):
        return list(collections.OrderedDict.fromkeys(words))
    @staticmethod
    def stemming(words):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        return [stemmer.stem(word) for word in words]
    @staticmethod
    def all_in_one(text):
        cleaned_text = Preprocessing.cleaning(text)
        folded_text = Preprocessing.case_folding(cleaned_text)
        tokens = Preprocessing.tokenisasi(folded_text)
        unique_tokens = Preprocessing.type(tokens)
        stemmed_words = Preprocessing.stemming(unique_tokens)
        filtered_words = Preprocessing.filtering(stemmed_words)
        return filtered_words
    @staticmethod
    def all_in_one_without_type(text):
        print('Preprocessing...')
        print(text)
        cleaned_text = Preprocessing.cleaning(text)
        folded_text = Preprocessing.case_folding(cleaned_text)
        tokens = Preprocessing.tokenisasi(folded_text)
        stemmed_words = Preprocessing.stemming(tokens)
        filtered_words = Preprocessing.filtering(stemmed_words)
        return filtered_words