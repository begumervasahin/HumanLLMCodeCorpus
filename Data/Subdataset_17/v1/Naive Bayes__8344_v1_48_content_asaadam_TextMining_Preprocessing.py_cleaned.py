import string
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import collections
class Preprocessing:
    stopword = open("stopword-list.txt", "r").read().split('\n')
    @staticmethod
    def cleaning(text):
        remove_link = re.sub(r'[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil)[\S]*', ' ', text)
        replace_punctuation = remove_link.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = remove_link.translate(replace_punctuation)
        cleaning = text.translate(str.maketrans('', '', '1234567890'))
        return re.sub(r'\s+', ' ', cleaning).strip()
    @staticmethod
    def case_folding(text):
        return str.casefold(text)
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
        print('preprocessing')
        print(text)
        return Preprocessing.filtering(
            Preprocessing.stemming(
                Preprocessing.tokenisasi(
                    Preprocessing.case_folding(
                        Preprocessing.cleaning(text)
                    )
                )
            )
        )
if __name__ == "__main__":
    sample_text = "This is a sample text to demonstrate preprocessing. Visit www.example.com for more info!"
    preprocessed_text = Preprocessing.all_in_one(sample_text)
    print("Preprocessed text:", preprocessed_text)