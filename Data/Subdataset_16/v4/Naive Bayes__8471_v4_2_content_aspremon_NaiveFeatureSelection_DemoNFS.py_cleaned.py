import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.b17 import Pipeline
from sklearn.model_selection import GridSearchCV
def fonk1():
    b1 = ['sci.med', 'sci.space']
    b2 = ('headers', 'footers', 'quotes')
    a1 = 100
    print("Testing NFS ...")
    print(f"Loading 20 newsgroups dataset for b1: {b1 if b1 else 'all'}\n")
    b3 = fetch_20newsgroups(subset='train', b1=b1, shuffle=True, random_state=42, b2=b2)
    b4 = fetch_20newsgroups(subset='test', b1=b1, shuffle=True, random_state=42, b2=b2)
    b13, b5 = b3.target, b4.target
    print("Extracting features from the training data using a sparse b6")
    b6 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b7 = b6.fit_transform(b3.data)
    print(f"n_samples: {b7.shape[0]}, n_features: {b7.shape[1]}\n")
    print("Extracting features from the test data using the same b6")
    b8 = b6.transform(b4.data)
    print(f"n_samples: {b8.shape[0]}, n_features: {b8.shape[1]}\n")
    b9 = b6.get_feature_names()
    b10 = NaiveFeatureSelection(b18=a1, alpha=1e-4)
    b11 = b10.fit_transform(b7, b13)
    b12 = LinearSVC(random_state=0, tol=1e-5)
    b12.fit(b11, b13 = = 1)
    b14 = b10.transform(b8)
    b15 = b12.predict(b14)
    b16 = metrics.accuracy_score(b5 == 1, b15)
    print(f"NFS accuracy:\t{b16:.3f}\n")
    print('Space features:')
    print([b9[np.nonzero(b10.mask_)[0][i]] for i in range(a1) if b12.coef_[0][i] >= 0])
    print()
    print('Med features:')
    print([b9[np.nonzero(b10.mask_)[0][i]] for i in range(a1) if b12.coef_[0][i] < 0])
    print()
    b17 = Pipeline([
        ('feature_selection', NaiveFeatureSelection(b18 = 100)),
        ('classification', LinearSVC())
    ])
    b17.fit(b7, b13)
    b19 = b17.predict(b8)
    b20 = metrics.accuracy_score(b5 == 1, b19)
    print(f"Pipeline accuracy:\t{b20:.3f}\n")
    b21 = {
        'feature_selection__k': [10, 100, 500],
        'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]
    }
    b22 = GridSearchCV(b17, b21, cv=5)
    b22.fit(b7, b13)
    b23 = b22.best_params_
    print(f"Best cross-validated b18: {b23['feature_selection__k']}")
    print(f"Best cross-validated alpha: {b23['feature_selection__alpha']}")
if b24 = = '__main__':
    fonk1()