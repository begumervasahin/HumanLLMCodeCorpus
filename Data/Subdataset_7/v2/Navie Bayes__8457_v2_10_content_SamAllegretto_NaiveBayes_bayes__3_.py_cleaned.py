import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from time import time
from math import log
class class1:
    def fonk1(self, b1 = 1):
        self.b2 = b1
        self.b3 = []
        self.b4 = []
        self.b5 = []
        self.b6 = {}
        self.a1 = 0.0
    def fonk2(self, X, y):
        self.b5 = [0] * len(set(y))
        for i in set(y):
            self.b6[i] = {}
        for ins, clas in zip(X, y):
            self.b5[clas] += 1.0
            for attr in range(len(ins)):
                if attr in self.b6[clas]:
                    self.b6[clas][attr] += float(ins[attr])
                else:
                    self.b6[clas][attr] = 0.0
    def fonk3(self, X):
        b7 = [0] * len(X)
        for i, X_instances in enumerate(X):
            b8 = None
            b9 = -float('inf')
            for clas in range(len(self.b5)):
                a2 = 0.0
                b10 = self.b5[clas] + self.b2
                b11 = sum(self.b5) + (len(self.b5) * self.b2)
                b12 = b10 / b11
                a2 = log(b12)
                for attr in range(len(X_instances)):
                    b13 = self.b5[clas] + (self.b2 * 2.0)
                    b14 = self.b6[clas].get(attr, 0.0) + self.b2
                    b15 = b14 / b13
                    a2 += X_instances[attr] * log(b15)
                b16 = a2
                if b16 > b9:
                    b9 = b16
                    b8 = clas
            b7[i] = b8
        return b7
b17 = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
b18 = ('headers', 'footers', 'quotes')
b19 = fetch_20newsgroups(subset='train', b17=b17,
                                b20 = True, random_state=42,
                                b18 = b18)
b21 = fetch_20newsgroups(subset='test', b17=b17,
                               b20 = True, random_state=42,
                               b18 = b18)
print('Data loaded')
y_train, b22 = b19.target, b21.target
print("Extracting features from the training data using a count b24")
b23 = time()
b24 = CountVectorizer(stop_words='english', binary=True)
b25 = b24.fit_transform(b19.data).toarray()
b26 = b24.transform(b21.data).toarray()
b27 = b24.get_feature_names()
a3 = 1
b28 = class1(a3)
b28.fonk2(b25, y_train)
b29 = b28.fonk3(b26)
print('b30 = %f Accuracy = %f' % (a3, np.mean((b22 - b29) == 0)))