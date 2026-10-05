import string
import re
import collections
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
class Preprocessing:
    with open("stopword-list.txt", "r") as f:
        stopword = f.read().split('\n')
    @staticmethod
    def cleaning(text):
        cleaned_text = re.sub('[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*', ' ', text)
        cleaned_text = cleaned_text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        cleaned_text = cleaned_text.translate(str.maketrans('', '', '1234567890'))
        cleaned_text = re.sub('\s+', ' ', cleaned_text).strip()
        return cleaned_text
    @staticmethod
    def case_folding(text):
        return text.lower()
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
    def all_in_one(text):
        text = Preprocessing.cleaning(text)
        text = Preprocessing.case_folding(text)
        text = Preprocessing.tokenization(text)
        text = Preprocessing.filtering(text)
        text = Preprocessing.remove_duplicates(text)
        text = Preprocessing.stemming(text)
        return text
    @staticmethod
    def all_in_one_without_type(text):
        text = Preprocessing.cleaning(text)
        text = Preprocessing.case_folding(text)
        text = Preprocessing.tokenization(text)
        text = Preprocessing.filtering(text)
        text = Preprocessing.stemming(text)
        return text
text = "This is an example text with some numbers 123 and links http:
processed_text = Preprocessing.all_in_one(text)
print("Processed text with type removal:", processed_text)
processed_text_without_type = Preprocessing.all_in_one_without_type(text)
print("Processed text without type removal:", processed_text_without_type)