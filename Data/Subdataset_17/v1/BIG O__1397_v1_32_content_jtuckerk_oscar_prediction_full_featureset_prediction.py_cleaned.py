import numpy as np
import requests
from sklearn import linear_model
from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import codecs
import re
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'www.plantcell.org'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text
def load():
    return load_batting(), load_allstars()
def get_input():
    OMDB = True
    IMDB_experience = True
    IMDB_oscar_prior = True
    PLOT = False
    year_range_min = 1990
    year_range_max = 2015
    ombd_file = './data/omdb_data.txt'
    omdb_feats = {}
    print("Getting OMDB features")
    with codecs.open(ombd_file, 'r', encoding='utf-8') as r:
        for line in r:
            l = eval(line)
            assert len(l) == 14
            critic_score = float(l[3])
            audience_score = float(l[4]) if l[4] != 'N/A' else 0
            duration = float(l[6].split()[0]) if l[6] != 'N/A' else 0
            metascore = float(l[7]) if l[7] != 'N/A' else 0
            imdb_rating = float(l[10].replace(",", '')) if l[10] != 'N/A' else 0
            imdb_votes = float(l[11].replace(",", '')) if l[11] != 'N/A' else 0
            year = int(re.findall(r'\d{4}', l[2]).pop())
            if year < year_range_min or year > year_range_max:
                continue
            assert year != 1924
            features = [critic_score, audience_score, duration, metascore, imdb_rating, imdb_votes]
            title_year = (l[1], re.findall(r'\d{4}', l[2]).pop())
            omdb_feats[title_year] = features
    actor_oscar_info = './data/actor_oscar_prior.txt'
    actor_oscar_feats = {}
    actor_oscar_size = 10
    print("Getting IMDB actor related features")
    with codecs.open(actor_oscar_info, 'r', encoding='utf-8') as r:
        for line in r:
            l = eval(line)
            assert len(l[1]) == 10
            actor_oscar_feats[l[0]] = l[1]
    actor_experience_data = './data/actor_experience.txt'
    actor_ex_feats = {}
    actor_ex_size = 10
    with codecs.open(actor_experience_data, 'r', encoding='utf-8') as r:
        for line in r:
            l = eval(line)
            assert len(l[1]) == 10
            actor_ex_feats[l[0]] = l[1]
    plot_embedding_data = './data/plot_embeddings.txt'
    plot_embedding_feats = {}
    plot_embedding_size = 128
    print("Getting plot vector representations")
    with codecs.open(plot_embedding_data, 'r', encoding='utf-8') as r:
        for line in r:
            l = eval(line)
            assert len(l[1]) == plot_embedding_size
            title = l[0][0]
            year = str(l[0][1])
            plot_embedding_feats[(title, year)] = l[1]
    feats = {}
    for k in omdb_feats.keys():
        a = omdb_feats[k] if OMDB else []
        b = actor_ex_feats.get(k, [0] * actor_ex_size) if IMDB_experience else []
        c = actor_oscar_feats.get(k, [0] * actor_oscar_size) if IMDB_oscar_prior else []
        d = plot_embedding_feats.get(k, [0] * plot_embedding_size) if PLOT else []
        feats[k] = np.array(a + b + c + d)
    return feats
def determine_y(encoding):
    return 0 if encoding < 1 else 1
def get_output():
    oscars = {}
    oscar_file = './data/oscar_y_full.txt'
    year_data = {}
    with codecs.open(oscar_file, 'r', encoding='utf-8') as r:
        for line in r:
            l = eval(line)
            y = determine_y(l[1])
            year = str(l[0][1])
            if year not in year_data:
                year_data[year] = {"nom": 0, "not": 0}
            if y:
                year_data[year]["nom"] += 1
                oscars[(l[0][0], year)] = y
            else:
                year_data[year]["not"] += 1
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
    for train_index, test_index in folds.split(X, Y):
        clf.fit(X[train_index], Y[train_index])
        prediction = clf.predict_proba(X[test_index])
        aucs.append(roc_auc_score(Y[test_index], prediction[:, 1]))
    print(f"{clf.__class__.__name__} AUC: {aucs}, Mean AUC: {np.mean(aucs)}")
def main():
    X, Y = get_X_y(get_input(), get_output())
    classifiers = [
        linear_model.SGDClassifier(loss='log'),
        GaussianNB(),
        RandomForestClassifier(n_estimators=10, max_depth=10)
    ]
    for clf in classifiers:
        test_classifier(clf, X, Y)
if __name__ == '__main__':
    main()