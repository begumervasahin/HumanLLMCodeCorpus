import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.b21 import Pipeline
from sklearn.model_selection import GridSearchCV
def fonk1(b10, b11):
    b1 = fetch_20newsgroups(subset='train', b10=b10, shuffle=True, random_state=42, b11=b11)
    b2 = fetch_20newsgroups(subset='test', b10=b10, shuffle=True, random_state=42, b11=b11)
    return b1.data, b2.data, b1.target, b2.target
def fonk2(b1, b2):
    b3 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b4 = b3.fit_transform(b1)
    b5 = b3.transform(b2)
    return b4, b5, b3.get_feature_names_out()
def fonk3(b13, b14, b16, a1):
    b6 = np.nonzero(b14.mask_)[0]
    b7 = b16.coef_[0]
    print('Space features:')
    b8 = [b13[b6[i]] for i in range(a1) if b7[i] >= 0]
    print(b8)
    print()
    print('Med features:')
    b9 = [b13[b6[i]] for i in range(a1) if b7[i] < 0]
    print(b9)
    print()
def fonk4():
    b10 = ['sci.med', 'sci.space']
    b11 = ('headers', 'footers', 'quotes')
    a1 = 100
    print("Testing Naive Feature Selection (NFS) ...")
    print(f"Loading 20 newsgroups dataset for b10: {b10}\n")
    b1, b2, b17, b12 = fonk1(b10, b11)
    print("Extracting features from the training and test data using a sparse b3")
    b4, b5, b13 = fonk2(b1, b2)
    print(f"n_samples: {b4.shape[0]}, n_features: {b4.shape[1]}\n")
    b14 = NaiveFeatureSelection(b22=a1, alpha=1e-4)
    b15 = b14.fit_transform(b4, b17)
    b16 = LinearSVC(random_state=0, tol=1e-5)
    b16.fit(b15, b17 = = 1)
    b18 = b14.transform(b5)
    b19 = b16.predict(b18)
    b20 = metrics.accuracy_score(b12 == 1, b19)
    print(f"NFS accuracy:\t{b20:.3f}\n")
    fonk3(b13, b14, b16, a1)
    b21 = Pipeline([
        ('feature_selection', NaiveFeatureSelection(b22 = 100)),
        ('classification', LinearSVC())
    ])
    b21.fit(b4, b17)
    b23 = b21.predict(b5)
    b24 = metrics.accuracy_score(b12 == 1, b23)
    print(f"Pipeline accuracy:\t{b24:.3f}\n")
    b25 = {
        'feature_selection__k': [10, 100, 500],
        'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]
    }
    b26 = GridSearchCV(b21, b25, cv=5)
    b26.fit(b4, b17)
    b27 = b26.best_params_
    print(f"Best cross-validated b22: {b27['feature_selection__k']}")
    print(f"Best cross-validated alpha: {b27['feature_selection__alpha']}")
if b28 = = '__main__':
    fonk4()