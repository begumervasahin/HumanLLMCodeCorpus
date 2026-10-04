import numpy as np
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from naive_feature_selection import NaiveFeatureSelection
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
def main():
    print("Testing Naive Feature Selection (NFS) ...")
    categories = ['sci.med', 'sci.space']
    remove = ('headers', 'footers', 'quotes')
    print(f"Loading 20 newsgroups dataset for categories: {categories if categories else 'all'}\n")
    data_train = fetch_20newsgroups(subset='train', categories=categories,
                                    shuffle=True, random_state=42, remove=remove)
    data_test = fetch_20newsgroups(subset='test', categories=categories,
                                   shuffle=True, random_state=42, remove=remove)
    y_train, y_test = data_train.target, data_test.target
    print("Extracting features from the training data using a sparse vectorizer")
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    X_train = vectorizer.fit_transform(data_train.data)
    print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}\n")
    print("Extracting features from the test data using the same vectorizer")
    X_test = vectorizer.transform(data_test.data)
    print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}\n")
    feature_names = vectorizer.get_feature_names_out()
    k_value = 100
    nfs = NaiveFeatureSelection(k=k_value, alpha=1e-4)
    X_new = nfs.fit_transform(X_train, y_train)
    classifier = LinearSVC(random_state=0, tol=1e-5)
    classifier.fit(X_new, y_train == 1)
    X_test_new = nfs.transform(X_test)
    y_pred_nfs = classifier.predict(X_test_new)
    nfs_accuracy = metrics.accuracy_score(y_test == 1, y_pred_nfs)
    print(f"NFS accuracy:\t{nfs_accuracy:.3f}\n")
    print('Space features:')
    print([feature_names[np.nonzero(nfs.mask_)[0][i]]
           for i in range(k_value) if classifier.coef_[0][i] >= 0])
    print()
    print('Med features:')
    print([feature_names[np.nonzero(nfs.mask_)[0][i]]
           for i in range(k_value) if classifier.coef_[0][i] < 0])
    print()
    pipeline = Pipeline([
        ('feature_selection', NaiveFeatureSelection(k=100)),
        ('classification', LinearSVC())
    ])
    pipeline.fit(X_train, y_train)
    y_pred_pipeline = pipeline.predict(X_test)
    pipeline_accuracy = metrics.accuracy_score(y_test == 1, y_pred_pipeline)
    print(f"Pipeline accuracy:\t{pipeline_accuracy:.3f}\n")
    parameters = {
        'feature_selection__k': [10, 100, 500],
        'feature_selection__alpha': [1e-10, 1e-5, 1e-3, 1e-2, 1e-1, 1, 10, 100]
    }
    grid_search_pipeline = Pipeline([
        ('feature_selection', NaiveFeatureSelection()),
        ('classification', LinearSVC())
    ])
    grid_search = GridSearchCV(grid_search_pipeline, parameters, cv=5)
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print(f"Best cross-validated k: {best_params['feature_selection__k']}")
    print(f"Best cross-validated alpha: {best_params['feature_selection__alpha']}")
if __name__ == '__main__':
    main()