import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from math import log
from time import time
class class1:
    def fonk1(self, b1 = 1):
        self.b2 = b1
        self.b3 = []
        self.b4 = {}
        self.a1 = 0.0
    def fonk2(self, X, y):
        b5 = len(set(y))
        self.b3 = [0] * b5
        for i in range(b5):
            self.b4[i] = {}
        for instance, label in zip(X, y):
            self.b3[label] += 1.0
            for attr_idx, attr_val in enumerate(instance):
                if attr_idx in self.b4[label]:
                    self.b4[label][attr_idx] += float(attr_val)
                else:
                    self.b4[label][attr_idx] = float(attr_val)
    def fonk3(self, X):
        b6 = [0] * len(X)
        b5 = len(self.b3)
        for i, instance in enumerate(X):
            b7 = None
            b8 = -float('inf')
            for cls in range(b5):
                b9 = log((self.b3[cls] + self.b2) /
                               (sum(self.b3) + b5 * self.b2))
                for attr_idx, attr_val in enumerate(instance):
                    b10 = self.b3[cls] + 2.0 * self.b2
                    b11 = self.b4[cls].get(attr_idx, 0.0) + self.b2
                    b9 += attr_val * log(b11 / b10)
                if b9 > b8:
                    b8 = b9
                    b7 = cls
            b6[i] = b7
        return b6
class class2:
    def fonk4(self, b1 = 1):
        self.b2 = b1
    def fonk5(self, X, y):
        pass
    def fonk6(self, X):
        return np.zeros([X.shape[0], 1])
def fonk7(b16, b12 = ('headers', 'footers', 'quotes')):
    b13 = fetch_20newsgroups(subset='train', b16=b16,
                                    b14 = True, random_state=42, b12=b12)
    b15 = fetch_20newsgroups(subset='test', b16=b16,
                                   b14 = True, random_state=42, b12=b12)
    return b13, b15
def fonk8():
    b16 = [
        'alt.atheism',
        'talk.religion.misc',
        'comp.graphics',
        'sci.space',
    ]
    b13, b15 = fonk7(b16)
    print('Data loaded')
    y_train, b17 = b13.target, b15.target
    print("Extracting features from the training data using a count b19")
    b18 = time()
    b19 = CountVectorizer(stop_words='english', binary=True)
    b20 = b19.fit_transform(b13.data).toarray()
    b21 = b19.transform(b15.data).toarray()
    b22 = b19.get_feature_names_out()
    a2 = 1
    b23 = class1(a2)
    b23.fonk5(b20, y_train)
    b24 = b23.fonk6(b21)
    b25 = np.mean(b17 == b24)
    print(f'a2 = {a2} b25 = {b25:.4f}')
if b26 = = "__main__":
    fonk8()