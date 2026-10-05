import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
import codecs
import re
def load_batting():
    pass
def load_allstars():
    pass
def load():
    return load_batting(), load_allstars()
def get_input():
    OMDB = True
    IMDB_experience = True
    IMDB_oscar_prior = True
    PLOT = False
    year_range_min = 1990
    year_range_max = 2015
    omdb_file = './data/omdb_data.txt'
    omdb_feats = {}
    with codecs.open(omdb_file, 'r', encoding='utf-8') as r:
        for line in r.readlines():
            l = eval(line)
    actor_oscar_info = './data/actor_oscar_prior.txt'
    actor_oscar_feats = {}
    actor_oscar_size = 10
    actor_experience_data = './data/actor_experience.txt'
    actor_ex_feats = {}
    actor_ex_size = 10
    plot_embedding_data = './data/plot_embeddings.txt'
    plot_embedding_feats = {}
    plot_embedding_size = 128
    feats = {}
    return feats
def determine_y(encoding):
    if encoding < 1:
        return 0
    else:
        return 1
def get_output():
    oscars = {}
    oscar_file = './data/oscar_y_full.txt'
    year_data = {}
    with codecs.open(oscar_file, 'r', encoding='utf-8') as r:
        for line in r.readlines():
            l = eval(line)
            y = determine_y(l[1])
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