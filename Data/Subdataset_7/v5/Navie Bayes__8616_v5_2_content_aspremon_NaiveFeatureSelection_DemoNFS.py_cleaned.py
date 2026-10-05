import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
def fonk1(b19, b1 = ('headers', 'footers', 'quotes')):
    print("Loading 20 newsgroups dataset for b19:")
    print(b19 if b19 else "all")
    print()
    b2 = fetch_20newsgroups(subset='train', b19=b19,
                                    b3 = True, random_state=42, b1=b1)
    b4 = fetch_20newsgroups(subset='test', b19=b19,
                                   b3 = True, random_state=42, b1=b1)
    return b2, b4
def fonk2(b2, b4):
    print("Extracting features from the training data using a sparse b5")
    b5 = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 b6 = 'english')
    b7 = b5.fit_transform(b2.data)
    print("n_samples: %d, n_features: %d" % b7.shape)
    print()
    print("Extracting features from the test data using the same b5")
    b8 = b5.transform(b4.data)
    print("n_samples: %d, n_features: %d" % b8.shape)
    print()
    b9 = b5.get_feature_names()
    return b7, b8, b9
def fonk3(b7, y_train, b10 = 100, alpha=1e-4):
    b11 = NaiveFeatureSelection(b16=b10, alpha=alpha)
    b12 = b11.fit_transform(b7, y_train)
    return b11, b12
def fonk4(b7, y_train):
    b13 = LinearSVC(random_state=0, tol=1e-5)
    b13.fit(b7, y_train)
    return b13
def fonk5(b13, b8, y_test):
    b14 = b13.predict(b8)
    b15 = metrics.accuracy_score(y_test, b14)
    return b14, b15
def fonk6(b11, b13, b9, b10 = 100):
    print('Space features:')
    print([b9[np.nonzero(b11.mask_)[0][i]]
           for i in range(b10) if b13.coef_[0][i] >= 0])
    print()
    print('Med features:')
    print([b9[np.nonzero(b11.mask_)[0][i]]
           for i in range(b10) if b13.coef_[0][i] < 0])
    print()
def fonk7(b7, y_train, b16 = 100):
    b13 = Pipeline([
        ('feature_selection', NaiveFeatureSelection(b16 = b16)),
        ('classification', LinearSVC())
    ])
    b13.fit(b7, y_train)
    return b13
def fonk8(b7, y_train):
    b17 = {
        'feature_selection__k': [10, 100, 500],
        'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]
    }
    b18 = Pipeline([
        ('feature_selection', NaiveFeatureSelection()),
        ('classification', LinearSVC())
    ])
    b13 = GridSearchCV(b18, b17, cv=5)
    b13.fit(b7, y_train)
    return b13
def fonk9():
    b19 = ['sci.med', 'sci.space']
    b2, b4 = fonk1(b19)
    b7, b8, b9 = fonk2(b2, b4)
    b11, b12 = fonk3(b7, b2.target)
    b13 = fonk4(b12, b2.target)
    print("NFS accuracy:\t%0.3f" % fonk5(b13, b11.transform(b8), b4.target)[1])
    fonk6(b11, b13, b9)
    b20 = fonk7(b7, b2.target)
    print("Pipeline accuracy:\t%0.3f" % fonk5(b20, b8, b4.target)[1])
    b21 = fonk8(b7, b2.target)
    print("Best cross-validated b16: " + str(b21.best_params_['feature_selection__k']))
    print("Best cross-validated alpha: " + str(b21.best_params_['feature_selection__alpha']))
if b22 = = "__main__":
    fonk9()