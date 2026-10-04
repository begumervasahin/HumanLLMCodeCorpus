import string
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
class Preprocess:
    def __init__(self):
        self.stemmer = StemmerFactory().create_stemmer()
        self.remover = StopWordRemoverFactory().create_stop_word_remover()
    def preprocess(self, text):
        text_stemmed = self.stemmer.stem(text)
        text_clean = self.remover.remove(text_stemmed)
        text_lower = text_clean.lower()
        preprocessed_text = text_lower.translate(str.maketrans('', '', string.punctuation)).split()
        return preprocessed_text
def main():
    preprocess = Preprocess()
    data = pd.read_csv('Coba.csv', sep=',')
    data['preprocessed'] = data['TOPIK'].apply(lambda x: ' '.join(preprocess.preprocess(x)))
    data.to_csv('Coba_preprocessed.csv', index=False)
if __name__ == '__main__':
    main()