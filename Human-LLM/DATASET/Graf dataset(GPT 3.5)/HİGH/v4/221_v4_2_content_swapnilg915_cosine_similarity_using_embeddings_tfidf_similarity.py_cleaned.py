import json
import os
import traceback
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
class class1:
    def fonk1(self):
        self.b1 = list(stopwords.words('english'))
        self.b2 = WordNetLemmatizer()
    def fonk2(self, text):
        b3 = pos_tag(word_tokenize(text))
        return " ".join([token for token, pos in b3 if pos in ['NN', 'VB']])
    def fonk3(self, b5, b4 = False):
        b5 = str(b5)
        b5 = re.sub(r"([\w].)([\~\!\@\
        b5 = re.sub(r"\s+", " ", b5)
        if b4:
            b5 = word_tokenize(b5.lower())
            b5 = [self.b2.lemmatize(token, 'v') for token in b5 if token not in self.b1 and token.isalpha()]
            return " ".join(b5)
        else:
            b5 = word_tokenize(b5.lower())
            b5 = [token for token in b5 if token not in self.b1 and token.isalpha()]
            return " ".join(b5)
    def fonk4(self, b11, b12):
        b6 = ''
        try:
            print("\n TF-IDF Vectorizer --- ")
            print("\n JD --- ", b11, len(b11))
            print("\n Resume --- ", b12, len(b12))
            b7 = set(b11.split()) & set(b12.split())
            print("\n Common words --- ", b7, len(b7))
            b8 = TfidfVectorizer(use_idf=True, sublinear_tf=True, lowercase=True)
            b9 = b8.fit_transform([b11])
            b10 = b8.transform([b12])
            b6 = cosine_similarity(b9, b10).flatten()[0]
            print("\n TF-IDF similarity --- ", b6)
        except Exception as e:
            print("\n Error in fonk4():", e, "\n", traceback.format_exc())
        return b6
    def fonk5(self, b11, b12):
        b11 = self.fonk3(b11, True)
        b12 = self.fonk3(b12, True)
        b12 = self.fonk2(b12)
        return self.fonk4(b11, b12)
    def fonk6(self):
        b11 = "Sample job description text"
        b12 = "Sample b12 text"
        self.fonk5(b11, b12)
if b13 = = '__main__':
    b14 = class1()
    b14.fonk6()