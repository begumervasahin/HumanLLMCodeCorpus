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
                self.b4[clas][attr] = self.b4[clas].get(attr, 0.0) + float(ins[attr])
    def fonk3(self, X):
        b5 = [0] * len(X)
        for i, X_instances in enumerate(X):
            b6 = None
            b7 = -float('inf')
            for clas in range(len(self.b3)):
                a1 = 0.0
                b8 = self.b3[clas] + self.b2
                b9 = sum(self.b3) + (len(self.b3) * self.b2)
                b10 = b8 / b9
                a1 = log(b10)
                for attr in range(len(X_instances)):
                    b11 = self.b3[clas] + (self.b2 * 2.0)
                    b12 = self.b4[clas].get(attr, 0.0) + self.b2
                    b13 = b12 / b11
                    a1 += X_instances[attr] * log(b13)
                b14 = a1
                if b14 > b7:
                    b7 = b14
                    b6 = clas
            b5[i] = b6
        return b5
b15 = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
b16 = ('headers', 'footers', 'quotes')
b17 = fetch_20newsgroups(subset='train', b15=b15, shuffle=True, random_state=42, b16=b16)
b18 = fetch_20newsgroups(subset='test', b15=b15, shuffle=True, random_state=42, b16=b16)
print('Data loaded')
y_train, b19 = b17.target, b18.target
print("Extracting features from the training data using a count b21")
b20 = time()
b21 = CountVectorizer(stop_words='english', binary=True)
b22 = b21.fit_transform(b17.data).toarray()
b23 = b21.transform(b18.data).toarray()
b24 = b21.get_feature_names()
a2 = 1
b25 = class1(a2)
b25.fonk2(b22, y_train)
b26 = b25.fonk3(b23)
print('a2 = %f accuracy = %f' % (a2, np.mean((b19 - b26) == 0)))