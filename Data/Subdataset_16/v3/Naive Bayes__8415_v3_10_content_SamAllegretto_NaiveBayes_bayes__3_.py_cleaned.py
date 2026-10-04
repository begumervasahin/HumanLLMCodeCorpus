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
        b5 = len(set(y))
        self.b3 = [0] * b5
        for i in set(y):
            self.b4[i] = {}
        for instance, label in zip(X, y):
            self.b3[label] += 1.0
            for attr in range(len(instance)):
                if attr in self.b4[label]:
                    self.b4[label][attr] += float(instance[attr])
                else:
                    self.b4[label][attr] = float(instance[attr])
    def fonk3(self, X):
        b6 = [0] * len(X)
        for i, X_instance in enumerate(X):
            b7 = None
            b8 = -float('inf')
            for clas in range(len(self.b3)):
                a1 = 0.0
                b9 = self.b3[clas] + self.b2
                b10 = sum(self.b3) + (len(self.b3) * self.b2)
                b11 = b9 / b10
                a1 = log(b11)
                for attr in range(len(X_instance)):
                    b12 = self.b3[clas] + (self.b2 * 2.0)
                    b13 = self.b4[clas].get(attr, 0.0) + self.b2
                    b14 = b13 / b12
                    a1 += X_instance[attr] * log(b14)
                if a1 > b8:
                    b8 = a1
                    b7 = clas
            b6[i] = b7
        return b6
def fonk4(b22):
    b15 = ('headers', 'footers', 'quotes')
    b16 = fetch_20newsgroups(subset='train', b22=b22, shuffle=True, random_state=42, b15=b15)
    b17 = fetch_20newsgroups(subset='test', b22=b22, shuffle=True, random_state=42, b15=b15)
    y_train, b18 = b16.target, b17.target
    b19 = CountVectorizer(stop_words='english', binary=True)
    b20 = b19.fit_transform(b16.data).toarray()
    b21 = b19.transform(b17.data).toarray()
    return b20, b21, y_train, b18
def fonk5():
    b22 = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
    print('Loading data...')
    b20, b21, y_train, b18 = fonk4(b22)
    print('Data loaded')
    print("Training Naive Bayes classifier")
    b23 = time()
    a2 = 1
    b24 = class1(a2)
    b24.fonk2(b20, y_train)
    b25 = b24.fonk3(b21)
    b26 = np.mean(b25 == b18)
    print(f'a2 = {a2} b26={b26:.4f}')
    print(f"Training and prediction took {time() - b23:.2f}s")
if b27 = = '__main__':
    fonk5()