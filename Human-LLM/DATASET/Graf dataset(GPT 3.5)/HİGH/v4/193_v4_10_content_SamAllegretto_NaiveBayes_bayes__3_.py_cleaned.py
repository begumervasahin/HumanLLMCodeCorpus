import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from time import time
from math import log
class class1:
    def fonk1(self, b1 = 1):
        self.b2 = b1
        self.b3 = []
        self.b4 = {}
    def fonk2(self, X, y):
        self.b3 = [0] * len(set(y))
        for i in set(y):
            self.b4[i] = {}
        for ins, clas in zip(X, y):
            self.b3[clas] += 1.0
            for attr in range(len(ins)):
                if attr in self.b4[clas]:
                    self.b4[clas][attr] += float(ins[attr])
                else:
                    self.b4[clas][attr] = 0.0
    def fonk3(self, X):
        b5 = [0] * len(X)
        for i, X_instances in enumerate(X):
            b6 = None
            b7 = -float('inf')
            for clas in range(len(self.b3)):
                a1 = 0.0
                a2 = 0.0
                b8 = sum(self.b3)
                a2 = self.b3[clas] + self.b2
                b8 = b8 + (len(self.b3) * self.b2)
                b9 = a2 / b8
                a1 = log(b9)
                for attr in range(len(X_instances)):
                    b10 = self.b3[clas] + (self.b2 * 2.0)
                    b11 = self.b4[clas].get(attr, 0.0) + self.b2
                    b12 = b11 / b10
                    a1 += X_instances[attr] * log(b12)
                b13 = a1
                if b13 > b7:
                    b7 = b13
                    b6 = clas
            b5[i] = b6
        return b5
b14 = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
b15 = ('headers', 'footers', 'quotes')
b16 = fetch_20newsgroups(subset='train', b14=b14, shuffle=True, random_state=42, b15=b15)
b17 = fetch_20newsgroups(subset='test', b14=b14, shuffle=True, random_state=42, b15=b15)
print('Data loaded')
y_train, b18 = b16.target, b17.target
print("Extracting features from the training data using a count b20")
b19 = time()
b20 = CountVectorizer(stop_words='english', binary=True)
b21 = b20.fit_transform(b16.data).toarray()
b22 = b20.transform(b17.data).toarray()
b23 = b20.get_feature_names()
a3 = 1
b24 = class1(a3)
b24.fonk2(b21, y_train)
b25 = b24.fonk3(b22)
print('a3 = %f accuracy = %f' % (a3, np.mean((b18 - b25) == 0)))