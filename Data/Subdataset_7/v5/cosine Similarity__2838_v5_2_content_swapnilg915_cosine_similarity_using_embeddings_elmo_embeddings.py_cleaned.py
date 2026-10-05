import regex as re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from abydos.distance import Jaccard
class class1:
    def fonk1(self):
        self.b1 = set(stopwords.words('english'))
        self.b2 = WordNetLemmatizer()
        self.b3 = Jaccard()
        self.b4 = hub.Module("https:
    def fonk2(self, b6, b5 = False):
        b6 = str(b6)
        b6 = re.sub(r"([\w].)([\~\!\@\
        b6 = re.sub(r"\s+", " ", b6)
        b6 = word_tokenize(b6.lower())
        if b5:
            b6 = [self.b2.lemmatize(token, 'v') for token in b6 if token.isalpha() and token not in self.b1]
        else:
            b6 = [token for token in b6 if token.isalpha() and token not in self.b1]
        return " ".join(b6)
    def fonk3(self, a, b):
        return np.inner(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))
    def fonk4(self, sentences):
        b7 = self.b4(sentences, signature="default", as_dict=True)["b4"]
        with tf.Session() as sess:
            sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
            return sess.run(b7)[0]
    def fonk5(self):
        b8 = 'machine learning'
        b9 = 'lead learning'
        print("=" * 75)
        print("\n Job Description:\n", b8, "\n Resume:\n", b9)
        b10 = self.fonk4([self.fonk2(b8)])
        print("\n Job Description Embeddings:\n", b10, "\n Shape:", b10.shape)
        b11 = self.fonk4([self.fonk2(b9)])
        b12 = self.fonk3(b10, b11)
        print("\n ELMo Cosine Similarity between Job Description and Resume:\n", b12)
if b13 = = '__main__':
    b14 = class1()
    b14.fonk5()