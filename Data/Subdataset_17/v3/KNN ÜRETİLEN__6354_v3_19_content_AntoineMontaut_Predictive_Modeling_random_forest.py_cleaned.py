import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
ACTIVITY_LIST = ['Walking', 'Walking upstairs', 'Walking downstairs', 'Sitting', 'Standing', 'Laying']
ACTIVITY_LIST_ABR = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
ACTIVITY_DICT = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs', '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
FEATURES_FILE = './UCI HAR Dataset/features.txt'
TRAIN_DATA_FILE = './UCI HAR Dataset/train/X_train.txt'
TRAIN_LABELS_FILE = './UCI HAR Dataset/train/y_train.txt'
TEST_DATA_FILE = './UCI HAR Dataset/test/X_test.txt'
TEST_LABELS_FILE = './UCI HAR Dataset/test/y_test.txt'
def load_features(file_path):
    with open(file_path, 'r') as f:
        features = []
        for line in f:
            _, feature = line.strip().split(' ')
            feature = re.sub(r'[-(),]', '_', feature).replace('BodyBody', 'Body').strip('_')
            features.append(feature)
        return features
def load_data(data_file, labels_file, features):
    X = pd.read_table(data_file, sep='\s+', names=features)
    with open(labels_file, 'r') as f:
        y = [line.strip() for line in f]
    y = pd.DataFrame(y, columns=['activity_cat'])
    y['activity'] = y['activity_cat'].map(ACTIVITY_DICT)
    return X, y
def preview_plots(X_train, y_train):
    X_train['activity'] = y_train['activity']
    plt.figure(figsize=(12, 8))
    for i, act in enumerate(ACTIVITY_LIST, 1):
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
def main():
    features = load_features(FEATURES_FILE)
    X_train, y_train = load_data(TRAIN_DATA_FILE, TRAIN_LABELS_FILE, features)
    print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
    X_train_selected = select_features(X_train)
    clf_domain = train_random_forest(X_train_selected, y_train['activity'])
    evaluate_model(clf_domain, X_train_selected, y_train['activity'], ACTIVITY_LIST_ABR)
    print('\n\n-----BLACK BOX APPROACH-----\n')
    clf_blackbox = train_random_forest(X_train, y_train['activity'])
    evaluate_model(clf_blackbox, X_train, y_train['activity'], ACTIVITY_LIST_ABR)
    X_test, y_test = load_data(TEST_DATA_FILE, TEST_LABELS_FILE, features)
    X_test_selected = select_features(X_test)
    print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
    evaluate_model(clf_domain, X_test_selected, y_test['activity'], ACTIVITY_LIST_ABR)
    print('\n\n-----BLACK BOX APPROACH-----\n')
    evaluate_model(clf_blackbox, X_test, y_test['activity'], ACTIVITY_LIST_ABR)
if __name__ == "__main__":
    main()