import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
class class1:
    def fonk1(self):
        self.b1 = set(stopwords.words('english'))
        self.b2 = WordNetLemmatizer()
    def fonk2(self, text):
        b3 = pos_tag(word_tokenize(text))
        return " ".join([token for token, pos in b3 if pos in ['NN', 'VB']])
    def fonk3(self, b5, b4 = False):
        b5 = str(b5)
        b5 = re.sub(r"([\w].)([\~\!\@\
        b5 = re.sub(r"\s+", " ", b5)
        b5 = word_tokenize(b5.lower())
        if b4:
            b5 = [self.b2.lemmatize(token, 'v') for token in b5 if token not in self.b1 and token.isalpha()]
        else:
            b5 = [token for token in b5 if token not in self.b1 and token.isalpha()]
        return " ".join(b5)
    def fonk4(self, b10, b11):
        try:
            b6 = TfidfVectorizer(use_idf=True, sublinear_tf=True, lowercase=True)
            b7 = b6.fit_transform([b10])
            b8 = b6.transform([b11])
            b9 = cosine_similarity(b7, b8).flatten()[0]
            return b9
        except Exception as e:
            print("\n Error in fonk4():", e)
    def fonk5(self, b10, b11):
        b10 = self.fonk3(b10, True)
        b11 = self.fonk3(b11, True)
        b11 = self.fonk2(b11)
        return self.fonk4(b10, b11)
    def fonk6(self):
        b10 = "Sample job description text"
        b11 = "Sample resume text"
        b12 = self.fonk5(b10, b11)
        if b12:
            print("\n TF-IDF similarity:", b12)
if b13 = = '__main__':
    b14 = class1()
    b14.fonk6()