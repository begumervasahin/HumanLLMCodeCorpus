import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
class Preprocess:
    def __init__(self):
        self.stemmer = StemmerFactory().create_stemmer()
        self.remover = StopWordRemoverFactory().create_stop_word_remover()
    def preprocess(self, text):
        text_stem = self.stemmer.stem(text)
        text_clean = self.remover.remove(text_stem)
        lowercase = text_clean.lower()
        preprocessed_text = lowercase.translate(None, string.punctuation).split()
        return preprocessed_text
if __name__ == '__main__':
    preprocess = Preprocess()
    import pandas as pd
    data = pd.read_csv('Coba.csv', sep=',')
    preprocessed_documents = []
    titles = data.TOPIK.tolist()
    for title in titles:
        preprocessed = preprocess.preprocess(title)
        preprocessed_documents.append(' '.join(preprocessed))
    data['preprocessed'] = preprocessed_documents
    data.to_csv('Coba.csv')