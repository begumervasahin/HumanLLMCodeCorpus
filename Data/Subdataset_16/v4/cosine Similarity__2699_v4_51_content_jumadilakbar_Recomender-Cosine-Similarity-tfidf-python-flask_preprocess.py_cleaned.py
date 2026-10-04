import string
import pandas as pd
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
        b6 = b5.translate(str.maketrans('', '', string.punctuation)).split()
        return b6
def fonk3():
    b7 = class1()
    b8 = pd.read_csv('Coba.csv', sep=',')
    b8['preprocessed'] = b8['TOPIK'].apply(lambda x: ' '.join(b7.fonk2(x)))
    b8.to_csv('Coba_preprocessed.csv', b9 = False)
if b10 = = '__main__':
    fonk3()