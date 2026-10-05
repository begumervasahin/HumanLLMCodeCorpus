import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from time import time
from math import log
class class1:
    def fonk1(self, b1 = 1):
        self.b1 = b1
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = {}
        self.a1 = 0.0
    def fonk2(self, X, y):
        self.b4 = [0] * len(set(y))
        for i in set(y):
            self.b5[i] = {}
        for instance, label in zip(X, y):
            self.b4[label] += 1.0
            for attr in range(len(instance)):
                if attr in self.b5[label]:
                    self.b5[label][attr] += float(instance[attr])
                else:
                    self.b5[label][attr] = 0.0
    def fonk3(self, X):
        b6 = [0] * len(X)
        for i, X_instances in enumerate(X):
            b7 = None
            b8 = -float('inf')
            for cls in range(len(self.b4)):
                a2 = 0.0
                b9 = self.b4[cls] + self.b1
                b10 = sum(self.b4) + (len(self.b4) * self.b1)
                b2 = b9 / b10
                a2 = log(b2)
                for attr in range(len(X_instances)):
                    b11 = self.b4[cls] + (self.b1 * 2.0)
                    b12 = self.b5[cls].get(attr, 0.0) + self.b1
                    b13 = b12 / b11
                    a2 += X_instances[attr] * log(b13)
                b14 = a2
                if b14 > b8:
                    b8 = b14
                    b7 = cls
            b6[i] = b7
        return b6
b15 = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
b16 = ('headers', 'footers', 'quotes')
b17 = fetch_20newsgroups(subset='train', b15=b15,
                                b18 = True, random_state=42,
                                b16 = b16)
b19 = fetch_20newsgroups(subset='test', b15=b15,
                               b18 = True, random_state=42,
                               b16 = b16)
print('Data loaded')
y_train, b20 = b17.target, b19.target
print("Extracting features from the training data using a count b22")
b21 = time()
b22 = CountVectorizer(stop_words='english', binary=True)
b23 = b22.fit_transform(b17.data).toarray()
b24 = b22.transform(b19.data).toarray()
b25 = b22.get_feature_names()
a3 = 1
b26 = class1(a3)
b26.fonk2(b23, y_train)
b27 = b26.fonk3(b24)
print('b28 = %f Accuracy = %f' % (a3, np.mean((b20 - b27) == 0)))