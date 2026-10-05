import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
import codecs
DATA_DIR = './data/'
OMDB_FILE = DATA_DIR + 'omdb_data.txt'
ACTOR_OSCAR_FILE = DATA_DIR + 'actor_oscar_prior.txt'
ACTOR_EXPERIENCE_FILE = DATA_DIR + 'actor_experience.txt'
PLOT_EMBEDDING_FILE = DATA_DIR + 'plot_embeddings.txt'
OSCAR_Y_FILE = DATA_DIR + 'oscar_y_full.txt'
def load_batting():
    pass
def load_allstars():
    pass
def load():
    return load_batting(), load_allstars()
def get_input():
    omdb_feats = {}
    actor_oscar_feats = {}
    actor_ex_feats = {}
    plot_embedding_feats = {}
    with codecs.open(OMDB_FILE, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            pass
    with codecs.open(ACTOR_OSCAR_FILE, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            pass
    with codecs.open(ACTOR_EXPERIENCE_FILE, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            pass
    with codecs.open(PLOT_EMBEDDING_FILE, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            pass
    feats = {}
    return feats
def determine_y(encoding):
    return 1 if encoding >= 1 else 0
def get_output():
    oscars = {}
    with codecs.open(OSCAR_Y_FILE, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            pass
    return oscars
def get_X_y(input_dict, output_dict):
    X = []
    y = []
    for k in input_dict.keys():
        X.append(input_dict.get(k, np.zeros(20)))
        y.append(output_dict.get(k, 0))
    return np.array(X), np.array(y)
def test_classifier(clf, X, Y):
    folds = StratifiedKFold(n_splits=5)
    aucs = []
    for train, test in folds.split(X, Y):
        clf.fit(X[train], Y[train])
        prediction = clf.predict_proba(X[test])
        aucs.append(roc_auc_score(Y[test], prediction[:, 1]))
    print(clf.__class__.__name__, aucs, np.mean(aucs))
def main():
    X, Y = get_X_y(get_input(), get_output())
    clf = SGDClassifier(loss='log')
    test_classifier(clf, X, Y)
    clf = GaussianNB()
    test_classifier(clf, X, Y)
    clf = RandomForestClassifier(n_estimators=10, max_depth=10)
    test_classifier(clf, X, Y)
if __name__ == '__main__':
    main()