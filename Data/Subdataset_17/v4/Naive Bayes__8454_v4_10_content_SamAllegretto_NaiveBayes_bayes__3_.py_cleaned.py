import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from math import log
from time import time
class MyBayesClassifier:
    def __init__(self, smooth=1):
        self._smooth = smooth
        self._class_counts = []
        self._feature_counts = {}
        self._total_samples = 0.0
    def train(self, X, y):
        num_classes = len(set(y))
        self._class_counts = [0] * num_classes
        for i in range(num_classes):
            self._feature_counts[i] = {}
        for instance, label in zip(X, y):
            self._class_counts[label] += 1.0
            for attr_idx, attr_val in enumerate(instance):
                if attr_idx in self._feature_counts[label]:
                    self._feature_counts[label][attr_idx] += float(attr_val)
                else:
                    self._feature_counts[label][attr_idx] = float(attr_val)
    def predict(self, X):
        predictions = [0] * len(X)
        num_classes = len(self._class_counts)
        for i, instance in enumerate(X):
            best_class = None
            highest_log_prob = -float('inf')
            for cls in range(num_classes):
                log_prob = log((self._class_counts[cls] + self._smooth) /
                               (sum(self._class_counts) + num_classes * self._smooth))
                for attr_idx, attr_val in enumerate(instance):
                    total_count = self._class_counts[cls] + 2.0 * self._smooth
                    attr_count = self._feature_counts[cls].get(attr_idx, 0.0) + self._smooth
                    log_prob += attr_val * log(attr_count / total_count)
                if log_prob > highest_log_prob:
                    highest_log_prob = log_prob
                    best_class = cls
            predictions[i] = best_class
        return predictions
class MyMultinomialBayesClassifier:
    def __init__(self, smooth=1):
        self._smooth = smooth
    def train(self, X, y):
        pass
    def predict(self, X):
        return np.zeros([X.shape[0], 1])
def main():
    categories = [
        'alt.atheism',
        'talk.religion.misc',
        'comp.graphics',
        'sci.space',
    ]
    remove = ('headers', 'footers', 'quotes')
    data_train = fetch_20newsgroups(subset='train', categories=categories,
                                    shuffle=True, random_state=42, remove=remove)
    data_test = fetch_20newsgroups(subset='test', categories=categories,
                                   shuffle=True, random_state=42, remove=remove)
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
    accuracy = np.mean(y_test == y_pred)
    print(f'alpha={alpha} accuracy = {accuracy:.4f}')
if __name__ == "__main__":
    main()