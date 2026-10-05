import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
import logging
import sys
from time import time
from math import log
class class1():
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
        return
    def fonk3(self, X):
        b7 = [0] * len(X)
        for i, X_instances in enumerate(X):
            b8 = None
            b9 = -float('inf')
            for clas in range(len(self.b5)):
                a2 = 0.0
                a3 = 0.0
                a4 = 0.0
                for j in range(len(self.b5)):
                    a4 += self.b5[j]
                a3 = self.b5[clas] + self.b2
                a4 = a4 + (len(self.b5) * self.b2)
                b10 = (a3/a4)
                a2 = log(b10)
                for attr in range(len(X_instances)):
                    b11 = self.b5[clas] + (self.b2 * 2.0)
                    b12 = self.b6[clas][attr] + self.b2
                    b13 = b12/b11
                    a2 += X_instances[attr] * log(b13)
                b14 = a2
                if b14 > b9:
                    b9 = b14
                    b8 = clas
            b7[i] = b8
        return b7
class class2():
    def fonk4(self, b1 = 1):
        self.b2 = b1
        self.b3 = []
        self.b4 = []
        self.b5 = []
        self.b6 = []
    def fonk5(self, X, y):
        return
    def fonk6(self, X):
        return np.zeros([X.shape[0],1])
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
print('data loaded')
y_train, b20 = b17.target, b19.target
print("Extracting features from the training data using a count b22")
b21 = time()
b22 = CountVectorizer(stop_words='english', binary=True)
b23 = b22.fit_transform(b17.data).toarray()
b24 = b22.transform(b19.data).toarray()
b25 = b22.get_feature_names()
a5 = 1
b26 = class1(a5)
b26.fonk5(b23,y_train)
b27 = b26.fonk6(b24)
print ('a5 = %f accuracy = %f' %(a5, np.mean((b20-b27)==0)))