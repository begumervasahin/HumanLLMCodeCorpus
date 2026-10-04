import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.b18 import Pipeline
from sklearn.model_selection import GridSearchCV
def fonk1():
    print("Testing Naive Feature Selection (NFS) ...")
    b1 = ['sci.med', 'sci.space']
    b2 = ('headers', 'footers', 'quotes')
    print(f"Loading 20 newsgroups dataset for b1: {b1 if b1 else 'all'}\n")
    b3 = fetch_20newsgroups(subset='train', b1=b1,
                                    b4 = True, random_state=42, b2=b2)
    b5 = fetch_20newsgroups(subset='test', b1=b1,
                                   b4 = True, random_state=42, b2=b2)
    b14, b6 = b3.target, b5.target
    print("Extracting features from the training data using a sparse b7")
    b7 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b8 = b7.fit_transform(b3.data)
    print(f"n_samples: {b8.shape[0]}, n_features: {b8.shape[1]}\n")
    print("Extracting features from the test data using the same b7")
    b9 = b7.transform(b5.data)
    print(f"n_samples: {b9.shape[0]}, n_features: {b9.shape[1]}\n")
    b10 = b7.get_feature_names_out()
    a1 = 100
    b11 = NaiveFeatureSelection(b19=a1, alpha=1e-4)
    b12 = b11.fit_transform(b8, b14)
    b13 = LinearSVC(random_state=0, tol=1e-5)
    b13.fit(b12, b14 = = 1)
    b15 = b11.transform(b9)
    b16 = b13.predict(b15)
    b17 = metrics.accuracy_score(b6 == 1, b16)
    print(f"NFS accuracy:\t{b17:.3f}\n")
    print('Space features:')
    print([b10[np.nonzero(b11.mask_)[0][i]]
           for i in range(a1) if b13.coef_[0][i] >= 0])
    print()
    print('Med features:')
    print([b10[np.nonzero(b11.mask_)[0][i]]
           for i in range(a1) if b13.coef_[0][i] < 0])
    print()
    b18 = Pipeline([
        ('feature_selection', NaiveFeatureSelection(b19 = 100)),
        ('classification', LinearSVC())
    ])
    b18.fit(b8, b14)
    b20 = b18.predict(b9)
    b21 = metrics.accuracy_score(b6 == 1, b20)
    print(f"Pipeline accuracy:\t{b21:.3f}\n")
    b22 = {
        'feature_selection__k': [10, 100, 500],
        'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]
    }
    b23 = Pipeline([
        ('feature_selection', NaiveFeatureSelection()),
        ('classification', LinearSVC())
    ])
    b24 = GridSearchCV(b23, b22, cv=5)
    b24.fit(b8, b14)
    b25 = b24.best_params_
    print(f"Best cross-validated b19: {b25['feature_selection__k']}")
    print(f"Best cross-validated alpha: {b25['feature_selection__alpha']}")
if b26 = = '__main__':
    fonk1()