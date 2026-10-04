import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
activity_list = ['Walking', 'Walking upstairs', 'Walking downstairs', 'Sitting', 'Standing', 'Laying']
activity_list_abr = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
activity_dict = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs', '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
features_file = './UCI HAR Dataset/features.txt'
train_data_file = './UCI HAR Dataset/train/X_train.txt'
train_labels_file = './UCI HAR Dataset/train/y_train.txt'
test_data_file = './UCI HAR Dataset/test/X_test.txt'
test_labels_file = './UCI HAR Dataset/test/y_test.txt'
def load_features(file_path):
    with open(file_path, 'r') as f:
        features = []
        for line in f:
            _, feature = line.strip().split(' ')
            feature = re.sub(r'[-(),]', '_', feature).replace('BodyBody', 'Body').strip('_')
            features.append(feature)
        return features
features = load_features(features_file)
def load_data(data_file, labels_file, features):
    X = pd.read_table(data_file, sep='\s+', names=features)
    with open(labels_file, 'r') as f:
        y = [line.strip() for line in f]
    y = pd.DataFrame(y, columns=['activity_cat'])
    y['activity'] = y['activity_cat'].map(activity_dict)
    return X, y
X_train, y_train = load_data(train_data_file, train_labels_file, features)
def preview_plots(X_train, y_train):
    X_train['activity'] = y_train['activity']
    plt.figure(figsize=(12, 8))
    for i, act in enumerate(activity_list, 1):
        plt.subplot(2, 3, i)
        plt.hist(X_train[X_train['activity'] == act]['fAccMag_mean'], bins=30)
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if i == 1:
            plt.ylabel('Dynamic Activity')
        if i == 4:
            plt.ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    X_train.drop('activity', axis=1, inplace=True)
def select_features(X_train):
    to_keep = []
    flags_out = ['angle', 'band', 'arCoeff', 'Mag']
    flags_in = ['mean', 'std', 'skewness', 'kurtosis']
    for col in X_train.columns:
        if not any(re.search(flag, col) for flag in flags_out) and any(re.search(flag, col) for flag in flags_in):
            to_keep.append(col)
    to_keep.sort()
    return X_train[to_keep]
X_train_selected = select_features(X_train)
def train_random_forest(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=50)
    clf.fit(X_train, y_train)
    return clf
def evaluate_model(clf, X_test, y_test, activity_list_abr):
    prediction = clf.predict(X_test)
    scores = {
        'accuracy': clf.score(X_test, y_test),
        'precision': precision_score(y_test, prediction, average='micro'),
        'recall': recall_score(y_test, prediction, average='micro'),
        'f1': f1_score(y_test, prediction, average='micro')
    }
    scores_rounded = {k: round(v, 5) for k, v in scores.items()}
    print(f'\nRandom Forest scores on test data (global):\n\tAccuracy: {scores_rounded["accuracy"]}\n\tPrecision: {scores_rounded["precision"]}\n\tRecall: {scores_rounded["recall"]}\n\tF1: {scores_rounded["f1"]}')
    conf_matrix = pd.DataFrame(confusion_matrix(y_test, prediction), columns=activity_list_abr, index=activity_list_abr)
    print('\nConfusion matrix:')
    print(conf_matrix)
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
clf_domain = train_random_forest(X_train_selected, y_train['activity'])
evaluate_model(clf_domain, X_train_selected, y_train['activity'], activity_list_abr)
print('\n\n-----BLACK BOX APPROACH-----\n')
clf_blackbox = train_random_forest(X_train, y_train['activity'])
evaluate_model(clf_blackbox, X_train, y_train['activity'], activity_list_abr)
X_test, y_test = load_data(test_data_file, test_labels_file, features)
X_test_selected = select_features(X_test)
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
evaluate_model(clf_domain, X_test_selected, y_test['activity'], activity_list_abr)
print('\n\n-----BLACK BOX APPROACH-----\n')
evaluate_model(clf_blackbox, X_test, y_test['activity'], activity_list_abr)