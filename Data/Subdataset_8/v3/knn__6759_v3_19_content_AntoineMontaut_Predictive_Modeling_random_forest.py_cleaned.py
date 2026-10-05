import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as skmet
ACTIVITY_LIST = ['Walking', 'Walking upstairs', 'Walking downstairs',
                 'Sitting', 'Standing', 'Laying']
ACTIVITY_LIST_ABR = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
ACTIVITY_DICT = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs',
                 '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
def load_feature_names(file_path):
    features = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            _, feature = str(line).rstrip().split(' ')
            feature = re.sub(r'[-(),]', '_', feature)
            feature = feature.replace('()', '').replace('__', '_').replace('BodyBody', 'Body')
            if feature[-1] == '_':
                feature = feature[:-1]
            features.append(feature)
    return features
def load_data(file_path, features):
    data = pd.read_table(file_path, sep='\s+', names=features)
    return data
def visualize_data(X, y):
    X['activity'] = y['activity']
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    for ax, act in zip(axes.ravel(), ACTIVITY_LIST):
        ax.hist(X[X.activity == act]['fAccMag_mean'], bins=20)
        ax.set_xlim([-1.0, 1.0])
        ax.set_title(act)
        if ax.is_first_row():
            ax.set_ylabel('Dynamic Activity')
        if ax.is_last_row():
            ax.set_ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    X.drop('activity', axis=1, inplace=True)
def filter_features(X):
    flags_out = ['angle', 'band', 'arCoeff', 'Mag']
    flags_in = ['mean', 'std', 'skewness', 'kurtosis']
    to_keep = [col for col in X.columns if not any(flag in col for flag in flags_out) and any(flag in col for flag in flags_in)]
    return X[to_keep]
def train_evaluate_classifier(X_train, y_train, X_test, y_test):
    clf = RandomForestClassifier(n_estimators=50)
    clf.fit(X_train, y_train)
    score_train = clf.score(X_train, y_train)
    print('Random Forest accuracy on training data:', round(score_train, 5))
    feat_imp = pd.Series(clf.feature_importances_, index=X_train.columns)
    feat_imp_sorted = feat_imp.sort_values(ascending=False)
    print('Most important features:')
    print(feat_imp_sorted[:10])
    score_test = clf.score(X_test, y_test)
    prediction = clf.predict(X_test)
    print('\nRandom Forest scores on test data (global):')
    print('\tAccuracy:', round(score_test, 5))
    precision_test = skmet.precision_score(y_test, prediction, average='micro')
    recall_test = skmet.recall_score(y_test, prediction, average='micro')
    f1_test = skmet.f1_score(y_test, prediction, average='micro')
    print('\tPrecision:', round(precision_test, 5))
    print('\tRecall:', round(recall_test, 5))
    print('\tF1:', round(f1_test, 5))
    conf_matrix = pd.DataFrame(skmet.confusion_matrix(y_test, prediction), columns=ACTIVITY_LIST_ABR, index=ACTIVITY_LIST_ABR)
    print('\nConfusion matrix:')
    print(conf_matrix)
def main():
    features = load_feature_names('./UCI HAR Dataset/features.txt')
    X_train = load_data('./UCI HAR Dataset/train/X_train.txt', features)
    y_train = pd.read_table('./UCI HAR Dataset/train/y_train.txt', header=None, names=['activity_cat'])
    y_train['activity'] = y_train['activity_cat'].map(ACTIVITY_DICT)
    X_test = load_data('./UCI HAR Dataset/test/X_test.txt', features)
    y_test = pd.read_table('./UCI HAR Dataset/test/y_test.txt', header=None, names=['activity_cat'])
    y_test['activity'] = y_test['activity_cat'].map(ACTIVITY_DICT)
    visualize_data(X_train.copy(), y_train.copy())
    X_train_filtered = filter_features(X_train.copy())
    X_test_filtered = filter_features(X_test.copy())
    train_evaluate_classifier(X_train_filtered, y_train['activity'], X_test_filtered, y_test['activity'])
if __name__ == "__main__":
    main()