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
def load_omdb_features(file_path, year_range_min=1990, year_range_max=2015):
    omdb_feats = {}
    print("Getting OMDB features")
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = eval(line)
            assert len(data) == 14
            year = int(re.findall(r'\d{4}', data[2]).pop())
            if year < year_range_min or year > year_range_max:
                continue
            features = [
                float(data[3]),
                float(data[4]) if data[4] != 'N/A' else 0,
                float(data[6].split()[0]) if data[6] != 'N/A' else 0,
                float(data[7]) if data[7] != 'N/A' else 0,
                float(data[10].replace(",", '')) if data[10] != 'N/A' else 0,
                float(data[11].replace(",", '')) if data[11] != 'N/A' else 0
            ]
            title_year = (data[1], year)
            omdb_feats[title_year] = features
    return omdb_feats
def load_actor_features(file_path):
    actor_feats = {}
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = eval(line)
            actor_feats[data[0]] = data[1]
    return actor_feats
def load_plot_embeddings(file_path, embedding_size=128):
    plot_embeddings = {}
    print("Getting plot vector representations")
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = eval(line)
            assert len(data[1]) == embedding_size
            title, year = data[0]
            plot_embeddings[(title, str(year))] = data[1]
    return plot_embeddings
def get_combined_features(omdb_feats, actor_ex_feats, actor_oscar_feats, plot_embedding_feats, include_omdb=True, include_experience=True, include_oscar=True, include_plot=False):
    combined_feats = {}
    for key in omdb_feats.keys():
        a = omdb_feats[key] if include_omdb else []
        b = actor_ex_feats.get(key, [0] * 10) if include_experience else []
        c = actor_oscar_feats.get(key, [0] * 10) if include_oscar else []
        d = plot_embedding_feats.get(key, [0] * 128) if include_plot else []
        combined_feats[key] = np.array(a + b + c + d)
    return combined_feats
def determine_y(encoding):
    return 0 if encoding < 1 else 1
def load_oscar_data(file_path):
    oscars = {}
    year_data = {}
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = eval(line)
            y = determine_y(data[1])
            year = str(data[0][1])
            if year not in year_data:
                year_data[year] = {"nom": 0, "not": 0}
            if y:
                year_data[year]["nom"] += 1
                oscars[(data[0][0], year)] = y
            else:
                year_data[year]["not"] += 1
    return oscars
def get_X_y(input_dict, output_dict):
    X = [input_dict.get(key, np.zeros(20)) for key in input_dict.keys()]
    y = [output_dict.get(key, 0) for key in input_dict.keys()]
    return np.array(X), np.array(y)
def test_classifier(clf, X, y):
    folds = StratifiedKFold(n_splits=5)
    aucs = []
    for train_index, test_index in folds.split(X, y):
        clf.fit(X[train_index], y[train_index])
        prediction = clf.predict_proba(X[test_index])
        aucs.append(roc_auc_score(y[test_index], prediction[:, 1]))
    print(f"{clf.__class__.__name__} AUC: {aucs}, Mean AUC: {np.mean(aucs)}")
def main():
    omdb_feats = load_omdb_features('./data/omdb_data.txt')
    actor_ex_feats = load_actor_features('./data/actor_experience.txt')
    actor_oscar_feats = load_actor_features('./data/actor_oscar_prior.txt')
    plot_embedding_feats = load_plot_embeddings('./data/plot_embeddings.txt')
    combined_feats = get_combined_features(omdb_feats, actor_ex_feats, actor_oscar_feats, plot_embedding_feats)
    oscars = load_oscar_data('./data/oscar_y_full.txt')
    X, y = get_X_y(combined_feats, oscars)
    classifiers = [
        linear_model.SGDClassifier(loss='log'),
        GaussianNB(),
        RandomForestClassifier(n_estimators=10, max_depth=10)
    ]
    for clf in classifiers:
        test_classifier(clf, X, y)
if __name__ == '__main__':
    main()