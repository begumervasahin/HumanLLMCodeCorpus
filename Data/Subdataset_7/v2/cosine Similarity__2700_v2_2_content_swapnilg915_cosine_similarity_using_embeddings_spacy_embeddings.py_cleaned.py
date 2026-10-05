import re
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords_en
class class1:
    def fonk1(self):
        self.b1 = spacy.load("en_core_web_lg")
    def fonk2(self, b2):
        b2 = re.sub(r"[^A-Za-z0-9]", " ", b2)
        b2 = re.sub(r"\s+", " ", b2)
        b2 = b2.lower().strip()
        return b2
    def fonk3(self, b2):
        b3 = [tok.lemma_.lower().strip() for tok in self.b1(b2) if (tok.lemma_ != '-PRON-' and tok.lemma_ not in stopwords_en and len(tok.lemma_)>1)]
        return " ".join(b3)
    def fonk4(self, b2):
        b2 = self.fonk2(b2)
        b2 = self.fonk3(b2)
        return b2
    def fonk5(self, vector_1, vector_2):
        return np.inner(vector_1, vector_2) / (np.linalg.norm(vector_1) * (np.linalg.norm(vector_2)))
    def fonk6(self, b11, b12):
        b4 = self.fonk4(b11)
        b5 = self.fonk4(b12)
        b6 = self.b1(b4).vector
        b7 = self.b1(b5).vector
        b8 = self.fonk5(b6, b7)
        print("\n Spacy Cosine Similarity:", b8)
if b9 = = '__main__':
    b10 = class1()
    b11 = "booking a flight is very easy"
    b12 = "reading a book is a good habit"
    b10.fonk6(b11, b12)