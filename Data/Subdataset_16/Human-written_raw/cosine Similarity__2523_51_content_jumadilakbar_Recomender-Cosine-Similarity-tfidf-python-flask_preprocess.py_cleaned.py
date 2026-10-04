import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
class class1:
    def fonk1(self):
        self.b1 = StemmerFactory().create_stemmer()
        self.b2 = StopWordRemoverFactory().create_stop_word_remover()
    def fonk2(self, text):
        b3 = self.b1.stem(text)
        b4 = self.b2.remove(b3)
        b5 = b4.lower()
        b6 = b5.translate(None, string.punctuation).split()
        return b6
if b7 = = '__main__':
    b8 = class1()
    import pandas as pd
    b9 = pd.read_csv('Coba.csv', sep=',')
    b10 = []
    b11 = b9.TOPIK.tolist()
    for title in b11:
        b12 = b8.fonk2(title)
        b10.append(' '.join(b12))
    b9['b12'] = b10
    b9.to_csv('Coba.csv')