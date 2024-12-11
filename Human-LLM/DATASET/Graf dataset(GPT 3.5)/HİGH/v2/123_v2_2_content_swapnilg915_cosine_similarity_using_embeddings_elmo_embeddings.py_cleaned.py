import regex as re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from keras import backend as K
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from abydos.distance import Jaccard
class class1:
    def fonk1(self):
        self.b1 = set(stopwords.words('english'))
        self.b2 = WordNetLemmatizer()
        self.b3 = hub.Module("https:
    def fonk2(self, b5, b4 = False):
        b5 = str(b5)
        b5 = re.sub(r"([\w].)([\~\!\@\
        b5 = re.sub(r"\s+", " ", b5)
        b5 = word_tokenize(b5.lower())
        if b4:
            b5 = [self.b2.lemmatize(token, 'v') for token in b5 if token.isalpha() and token not in self.b1]
        else:
            b5 = [token for token in b5 if token.isalpha() and token not in self.b1]
        return " ".join(b5)
    def fonk3(self, a, b):
        return np.inner(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    def fonk4(self, sentences):
        b3 = hub.Module("https:
        b6 = b3(sentences, signature="default", as_dict=True)["b3"]
        with tf.Session() as sess:
            sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
            return sess.run(b6)[0]
    def fonk5(self):
        b7 = 'machine learning'
        b8 = 'lead learning'
        print("=" * 75)
        print("\n ", b7, "\n ", b8)
        b9 = self.fonk4([self.fonk2(b7)])
        print("\n b9 --- ", b9, b9.shape)
        b10 = self.fonk4([self.fonk2(b8)])
        b11 = self.fonk3(b9, b10)
        print("\n b3 similarity --- ", b11)
if b12 = = '__main__':
    b13 = class1()
    b13.fonk5()