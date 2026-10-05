import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from time import time
from math import log
class MyBayesClassifier:
    def __init__(self, smooth=1):
        self.smooth = smooth
        self.class_prob = []
        self.feature_prob = []
        self.class_counts = []
        self.feature_counts = {}
        self.train_len = 0.0
    def train(self, X, y):
        self.class_counts = [0] * len(set(y))
        for i in set(y):
            self.feature_counts[i] = {}
        for instance, label in zip(X, y):
            self.class_counts[label] += 1.0
            for attr in range(len(instance)):
                if attr in self.feature_counts[label]:
                    self.feature_counts[label][attr] += float(instance[attr])
                else:
                    self.feature_counts[label][attr] = 0.0
    def predict(self, X):
        predictions = [0] * len(X)
        for i, X_instances in enumerate(X):
            decision = None
            top_prob = -float('inf')
            for cls in range(len(self.class_counts)):
                total_prob = 0.0
                curr_class = self.class_counts[cls] + self.smooth
                total_class = sum(self.class_counts) + (len(self.class_counts) * self.smooth)
                class_prob = curr_class / total_class
                total_prob = log(class_prob)
                for attr in range(len(X_instances)):
                    total_attr = self.class_counts[cls] + (self.smooth * 2.0)
                    curr_attr = self.feature_counts[cls].get(attr, 0.0) + self.smooth
                    prob_attr = curr_attr / total_attr
                    total_prob += X_instances[attr] * log(prob_attr)
                y_hat = total_prob
                if y_hat > top_prob:
                    top_prob = y_hat
                    decision = cls
            predictions[i] = decision
        return predictions
categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
remove = ('headers', 'footers', 'quotes')
data_train = fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42,
                                remove=remove)
data_test = fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42,
                               remove=remove)
print('Data loaded')
y_train, y_test = data_train.target, data_test.target
print("Extracting features from the training data using a count vectorizer")
t0 = time()
vectorizer = CountVectorizer(stop_words='english', binary=True)
X_train = vectorizer.fit_transform(data_train.data).toarray()
X_test = vectorizer.transform(data_test.data).toarray()
feature_names = vectorizer.get_feature_names()
alpha = 1
clf = MyBayesClassifier(alpha)
clf.train(X_train, y_train)
y_pred = clf.predict(X_test)
print('Alpha=%f Accuracy = %f' % (alpha, np.mean((y_test - y_pred) == 0)))