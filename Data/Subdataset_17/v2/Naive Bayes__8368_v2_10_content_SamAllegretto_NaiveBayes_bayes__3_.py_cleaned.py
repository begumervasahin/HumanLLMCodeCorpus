import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from time import time
from math import log
class MyBayesClassifier:
    def __init__(self, smooth=1):
        self._smooth = smooth
        self._Ncls = []
        self._Nfeat = {}
    def train(self, X, y):
        num_classes = len(set(y))
        self._Ncls = [0] * num_classes
        for i in set(y):
            self._Nfeat[i] = {}
        for instance, label in zip(X, y):
            self._Ncls[label] += 1.0
            for attr in range(len(instance)):
                if attr in self._Nfeat[label]:
                    self._Nfeat[label][attr] += float(instance[attr])
                else:
                    self._Nfeat[label][attr] = float(instance[attr])
    def predict(self, X):
        predictions = [0] * len(X)
        for i, X_instance in enumerate(X):
            decision = None
            top_prob = -float('inf')
            for clas in range(len(self._Ncls)):
                total_prob = 0.0
                curr_class = self._Ncls[clas] + self._smooth
                total_class = sum(self._Ncls) + (len(self._Ncls) * self._smooth)
                class_prob = curr_class / total_class
                total_prob = log(class_prob)
                for attr in range(len(X_instance)):
                    total_attr = self._Ncls[clas] + (self._smooth * 2.0)
                    curr_attr = self._Nfeat[clas].get(attr, 0.0) + self._smooth
                    prob_attr = curr_attr / total_attr
                    total_prob += X_instance[attr] * log(prob_attr)
                if total_prob > top_prob:
                    top_prob = total_prob
                    decision = clas
            predictions[i] = decision
        return predictions
def load_and_prepare_data(categories):
    remove = ('headers', 'footers', 'quotes')
    data_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42, remove=remove)
    data_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42, remove=remove)
    y_train, y_test = data_train.target, data_test.target
    vectorizer = CountVectorizer(stop_words='english', binary=True)
    X_train = vectorizer.fit_transform(data_train.data).toarray()
    X_test = vectorizer.transform(data_test.data).toarray()
    return X_train, X_test, y_train, y_test
def main():
    categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
    print('Loading data...')
    X_train, X_test, y_train, y_test = load_and_prepare_data(categories)
    print('Data loaded')
    print("Extracting features from the training data using a count vectorizer")
    t0 = time()
    alpha = 1
    clf = MyBayesClassifier(alpha)
    clf.train(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = np.mean(y_pred == y_test)
    print(f'alpha={alpha} accuracy={accuracy:.4f}')
if __name__ == '__main__':
    main()