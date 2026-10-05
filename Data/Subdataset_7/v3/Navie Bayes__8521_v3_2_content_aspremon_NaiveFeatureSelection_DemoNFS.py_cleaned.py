import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
def fonk1(b5, b6):
    print("Loading 20 newsgroups dataset for b5:")
    print(b5 if b5 else "all")
    print()
    b1 = fetch_20newsgroups(subset='train', b5=b5, shuffle=True, random_state=42, b6=b6)
    b2 = fetch_20newsgroups(subset='test', b5=b5, shuffle=True, random_state=42, b6=b6)
    b14, b3 = b1.target, b2.target
    return b1, b2, b14, b3
def fonk2(b7, data):
    b4 = b7.transform(data)
    print("n_samples: %d, n_features: %d" % b4.shape)
    print()
    return b4
def fonk3(b11, b13, b10):
    print('Space b4:')
    print([b10[np.nonzero(b11.mask_)[0][i]] for i in range(b11.b19) if b13.coef_[0][i] >= 0])
    print()
    print('Med b4:')
    print([b10[np.nonzero(b11.mask_)[0][i]] for i in range(b11.b19) if b13.coef_[0][i] < 0])
    print()
def fonk4():
    print("Testing Naive Feature Selection (NFS) ...")
    b5 = ['sci.med', 'sci.space']
    b6 = ('headers', 'footers', 'quotes')
    b1, b2, b14, b3 = fonk1(b5, b6)
    print("Extracting b4 from the training data using a sparse b7")
    b7 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    b8 = fonk2(b7, b1.data)
    print("Extracting b4 from the test data using the same b7")
    b9 = fonk2(b7, b2.data)
    b10 = b7.get_feature_names()
    a1 = 100
    b11 = NaiveFeatureSelection(b19=a1, alpha=1e-4)
    b12 = b11.fit_transform(b8, b14)
    b13 = LinearSVC(random_state=0, tol=1e-5)
    b13.fit(b12, b14 = = 1)
    b15 = b11.transform(b9)
    b16 = b13.predict(b15)
    b17 = metrics.accuracy_score(b3 == 1, b16)
    print("NFS accuracy:\t%0.3f" % b17)
    print()
    fonk3(b11, b13, b10)
    b18 = Pipeline([
        ('feature_selection', NaiveFeatureSelection(b19 = 100)),
        ('classification', LinearSVC())
    ])
    b18.fit(b8, b14)
    b20 = b18.predict(b9)
    b21 = metrics.accuracy_score(b3 == 1, b20)
    print("Pipeline accuracy:\t%0.3f" % b21)
    print()
    b22 = {'feature_selection__k': [10, 100, 500],
                  'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]}
    b23 = Pipeline([
        ('feature_selection', NaiveFeatureSelection()),
        ('classification', LinearSVC())
    ])
    b18 = GridSearchCV(b23, b22, cv=5)
    b18.fit(b8, b14)
    print("Best cross validated b19: " + str(b18.best_params_['feature_selection__k']))
    print("Best cross validated alpha: " + str(b18.best_params_['feature_selection__alpha']))
if b24 = = "__main__":
    fonk4()