import regex as re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from keras import backend as K
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from abydos.distance import Jaccard
class class1(object):
    def fonk1(self):
        self.b1 = list(stopwords.words('english'))
        self.b2 = WordNetLemmatizer()
        self.b3 = Jaccard()
        self.b4 = hub.Module("https:
    def fonk2(self, b6, b5 = False):
        b6 = str(b6)
        b6 = re.sub(r"([\w].)([\~\!\@\
        b6 = re.sub(r"\s+", " ", b6)
        if b5:
            return " ".join([self.b2.lemmatize(token, 'v') for token in word_tokenize(b6.lower()) if token not in self.b1 and token.isalpha()])
        else:
            return " ".join([token for token in word_tokenize(b6.lower()) if token not in self.b1 and token.isalpha()])
    def fonk3(self, a, b):
        return np.inner(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))
    def fonk4(self, sentences):
        b4 = hub.Module("https:
        b7 = b4(
            sentences,
            b8 = "default",
            b9 = True)["b4"]
        return self.fonk5(b7)[0]
    def fonk5(self, tensor):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.tables_initializer())
            return sess.run(tensor)
    def fonk6(self, embeddings):
        return embeddings.sum(b10 = 1)
    def fonk7(self):
        b11 = 'machine learning'
        b12 = 'lead learning'
        print("==="*25)
        print("\n ", b11, "\n ", b12)
        b13 = self.fonk4([b11])
        print("\n b13 --- ", b13, b13.shape)
        b14 = self.fonk4([b12])
        b15 = self.fonk3(b13, b14)
        print("\n b4 similarity --- ", b15)
if b16 = = '__main__':
    b17 = class1()
    b17.fonk7()