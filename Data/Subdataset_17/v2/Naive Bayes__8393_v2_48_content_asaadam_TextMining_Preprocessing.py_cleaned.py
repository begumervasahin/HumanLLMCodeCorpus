import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class Preprocessing:
    with open("stopword-list.txt", "r") as file:
        stopwords = file.read().split('\n')
    @staticmethod
    def clean_text(text):
        text = re.sub(r'\b\w+:
        text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        text = text.translate(str.maketrans('', '', '0123456789'))
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    @staticmethod
    def case_fold(text):
        return text.lower()
    @staticmethod
    def tokenize(text):
        return text.split()
    @staticmethod
    def remove_stopwords(words):
        return [word for word in words if word not in Preprocessing.stopwords]
    @staticmethod
    def get_unique_words(words):
        return list(collections.OrderedDict.fromkeys(words))
    @staticmethod
    def stem_words(words):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        return [stemmer.stem(word) for word in words]
    @staticmethod
    def preprocess(text):
        text = Preprocessing.clean_text(text)
        text = Preprocessing.case_fold(text)
        words = Preprocessing.tokenize(text)
        words = Preprocessing.remove_stopwords(words)
        words = Preprocessing.get_unique_words(words)
        words = Preprocessing.stem_words(words)
        return words
    @staticmethod
    def preprocess_without_unique(text):
        text = Preprocessing.clean_text(text)
        text = Preprocessing.case_fold(text)
        words = Preprocessing.tokenize(text)
        words = Preprocessing.remove_stopwords(words)
        words = Preprocessing.stem_words(words)
        return words
if __name__ == "__main__":
    sample_text = "This is a sample text to demonstrate preprocessing. Visit www.example.com for more info!"
    preprocessed_text = Preprocessing.preprocess(sample_text)
    print("Preprocessed text:", preprocessed_text)