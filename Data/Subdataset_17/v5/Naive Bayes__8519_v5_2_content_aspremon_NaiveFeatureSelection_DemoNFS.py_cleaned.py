import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
def load_data(categories, remove):
    data_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42, remove=remove)
    data_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42, remove=remove)
    return data_train.data, data_test.data, data_train.target, data_test.target
def extract_features(data_train, data_test):
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    X_train = vectorizer.fit_transform(data_train)
    X_test = vectorizer.transform(data_test)
    return X_train, X_test, vectorizer.get_feature_names_out()
def print_features(feature_names, nfs, clf, kv):
    mask_indices = np.nonzero(nfs.mask_)[0]
    coef = clf.coef_[0]
    print('Space features:')
    space_features = [feature_names[mask_indices[i]] for i in range(kv) if coef[i] >= 0]
    print(space_features)
    print()
    print('Med features:')
    med_features = [feature_names[mask_indices[i]] for i in range(kv) if coef[i] < 0]
    print(med_features)
    print()
def main():
    categories = ['sci.med', 'sci.space']
    remove = ('headers', 'footers', 'quotes')
    kv = 100
    print("Testing Naive Feature Selection (NFS) ...")
    print(f"Loading 20 newsgroups dataset for categories: {categories}\n")
    data_train, data_test, y_train, y_test = load_data(categories, remove)
    print("Extracting features from the training and test data using a sparse vectorizer")
    X_train, X_test, feature_names = extract_features(data_train, data_test)
    print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}\n")
    nfs = NaiveFeatureSelection(k=kv, alpha=1e-4)
    X_train_new = nfs.fit_transform(X_train, y_train)
    clf = LinearSVC(random_state=0, tol=1e-5)
    clf.fit(X_train_new, y_train == 1)
    X_test_new = nfs.transform(X_test)
    y_pred_NFS = clf.predict(X_test_new)
    score_nfs = metrics.accuracy_score(y_test == 1, y_pred_NFS)
    print(f"NFS accuracy:\t{score_nfs:.3f}\n")
    print_features(feature_names, nfs, clf, kv)
    pipeline = Pipeline([
        ('feature_selection', NaiveFeatureSelection(k=100)),
        ('classification', LinearSVC())
    ])
    pipeline.fit(X_train, y_train)
    y_pred_pp = pipeline.predict(X_test)
    score_pp = metrics.accuracy_score(y_test == 1, y_pred_pp)
    print(f"Pipeline accuracy:\t{score_pp:.3f}\n")
    parameters = {
        'feature_selection__k': [10, 100, 500],
        'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]
    }
    grid_search = GridSearchCV(pipeline, parameters, cv=5)
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print(f"Best cross-validated k: {best_params['feature_selection__k']}")
    print(f"Best cross-validated alpha: {best_params['feature_selection__alpha']}")
if __name__ == '__main__':
    main()