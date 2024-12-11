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
        b3 = [token.lemma_.lower().strip() for token in self.b1(b2)
                             if (token.lemma_ != '-PRON-' and token.lemma_ not in stopwords_en and len(token.lemma_)>1)]
        return " ".join(b3)
    def fonk4(self, b2):
        b4 = self.fonk2(b2)
        b5 = self.fonk3(b4)
        return b5
    def fonk5(self, vector_1, vector_2):
        b6 = np.inner(vector_1, vector_2) / (np.linalg.norm(vector_1) * (np.linalg.norm(vector_2)))
        return b6
    def fonk6(self, b14, b15):
        b7 = self.fonk4(b14)
        b8 = self.fonk4(b15)
        b9 = self.b1(b7).vector
        b10 = self.b1(b8).vector
        b11 = self.fonk5(b9, b10)
        print("\n Spacy Cosine Similarity:", b11)
if b12 = = '__main__':
    b13 = class1()
    b14 = "booking a flight is very easy"
    b15 = "reading a book is a good habit"
    b13.fonk6(b14, b15)