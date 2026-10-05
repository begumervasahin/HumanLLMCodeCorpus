import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
print("Testing Naive Feature Selection (NFS) ...")
b1 = ['sci.med', 'sci.space']
b2 = ('headers', 'footers', 'quotes')
print("Loading 20 newsgroups dataset for b1:")
print(b1 if b1 else "all")
print()
b3 = fetch_20newsgroups(subset='train', b1=b1, shuffle=True, random_state=42, b2=b2)
b4 = fetch_20newsgroups(subset='test', b1=b1, shuffle=True, random_state=42, b2=b2)
b13, b5 = b3.target, b4.target
print("Extracting features from the training data using a sparse b6")
b6 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
b7 = b6.fit_transform(b3.data)
print("n_samples: %d, n_features: %d" % b7.shape)
print()
print("Extracting features from the test data using the same b6")
b8 = b6.transform(b4.data)
print("n_samples: %d, n_features: %d" % b8.shape)
print()
b9 = b6.get_feature_names()
a1 = 100
b10 = NaiveFeatureSelection(b18=a1, alpha=1e-4)
b11 = b10.fit_transform(b7, b13)
b12 = LinearSVC(random_state=0, tol=1e-5)
b12.fit(b11, b13 = = 1)
b14 = b10.transform(b8)
b15 = b12.predict(b14)
b16 = metrics.accuracy_score(b5 == 1, b15)
print("NFS accuracy:\t%0.3f" % b16)
print()
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
print("Pipeline accuracy:\t%0.3f" % b20)
print()
b21 = {'feature_selection__k': [10, 100, 500],
              'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]}
b22 = Pipeline([
    ('feature_selection', NaiveFeatureSelection()),
    ('classification', LinearSVC())
])
b17 = GridSearchCV(b22, b21, cv=5)
b17.fit(b7, b13)
print("Best cross validated b18: " + str(b17.best_params_['feature_selection__k']))
print("Best cross validated alpha: " + str(b17.best_params_['feature_selection__alpha']))