import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
print("Testing NFS ...")
b1 = [
        'sci.med',
        'sci.space'
    ]
b2 = ('headers', 'footers', 'quotes')
print("Loading 20 newsgroups dataset for b1:")
print(b1 if b1 else "all")
print()
b3 = fetch_20newsgroups(subset='train', b1=b1,
                                b4 = True, random_state=42, b2=b2)
b5 = fetch_20newsgroups(subset='test', b1=b1,
                               b4 = True, random_state=42, b2=b2)
b15, b6 = b3.target, b5.target
print("Extracting features from the training data using a sparse b7")
b7 = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             b8 = 'english')
b9 = b7.fit_transform(b3.data)
print("n_samples: %d, n_features: %d" % b9.shape)
print()
print("Extracting features from the test data using the same b7")
b10 = b7.transform(b5.data)
print("n_samples: %d, n_features: %d" % b10.shape)
print()
b11 = b7.get_feature_names()
a1 = 100
b12 = NaiveFeatureSelection(b20=a1, alpha=1e-4)
b13 = b12.fit_transform(b9, b15)
b14 = LinearSVC(random_state=0, tol=1e-5)
b14.fit(b13, b15 = = 1)
b16 = b12.transform(b10)
b17 = b14.predict(b16)
b18 = metrics.accuracy_score(b6 == 1, b17)
print("NFS accuracy:\t%0.3f" % b18)
print("")
print('Space features:')
print([b11[np.nonzero(b12.mask_)[0][i]]
       for i in range(a1) if b14.coef_[0][i] >= 0])
print()
print('Med features:')
print([b11[np.nonzero(b12.mask_)[0][i]] for i in range(a1) if b14.coef_[0][i]<0])
print("")
from sklearn.pipeline import Pipeline
b19 = Pipeline([
  ('feature_selection', NaiveFeatureSelection(b20 = 100)),
  ('classification', LinearSVC())
])
b19.fit(b9, b15)
b21 = b19.predict(b10)
b22 = metrics.accuracy_score(b6 == 1, b21)
print("Pipeline accuracy:\t%0.3f" % b22)
print("")
from sklearn.model_selection import GridSearchCV
b23 = {'feature_selection__k': [10, 100, 500],
  'feature_selection__alpha': [1e-10,1e-5,1e-3,1e-2,1e-1, 1, 10, 100]}
b24 = Pipeline([
  ('feature_selection', NaiveFeatureSelection()),
  ('classification', LinearSVC())
])
b19 = GridSearchCV(b24, b23, cv=5)
b19.fit(b9, b15)
b19.best_params_
print("Best cross validated b20: " + str(b19.best_params_['feature_selection__k']))
print("Best cross validated alpha: " + str(b19.best_params_['feature_selection__alpha']))