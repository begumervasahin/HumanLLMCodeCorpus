import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import sklearn.metrics as skmet
activity_list = ['Walking', 'Walking upstairs', 'Walking downstairs', 'Sitting', 'Standing', 'Laying']
activity_list_abr = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
activity_dict = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs', '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
with open('./UCI HAR Dataset/features.txt', 'r') as open_features:
    features = []
    for line in open_features.readlines():
        dummy, feature = str(line).rstrip().split(' ')
        for char in ['-', '(', ',', ')']:
            feature = feature.replace(char, '_')
        feature = feature.replace('()', '')
        feature = feature.replace('__', '_')
        for elem in ['BodyBody', 'Body']:
            feature = feature.replace(elem, '')
        if feature[-1] == '_':
            feature = feature[:-1]
        features.append(feature)
X_train = pd.read_table('./UCI HAR Dataset/train/X_train.txt', sep='\s+', names=features)
with open('./UCI HAR Dataset/train/y_train.txt') as open_y_train:
    y_train = [str(line).rstrip()[0] for line in open_y_train.readlines()]
y_train = pd.DataFrame(y_train, columns=['activity_cat'])
y_train['activity'] = y_train.activity_cat.map(lambda x: activity_dict[x])
def preview_plots():
    X_train['activity'] = y_train.activity
    plt.figure(figsize=(12, 8))
    for i, act in enumerate(activity_list, 1):
        plt.subplot(2, 3, i)
        plt.hist(X_train[X_train.activity == act].fAccMag_mean, bins=30)
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if i == 1:
            plt.ylabel('Dynamic Activity')
        if i == 4:
            plt.ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    X_train.drop('activity', axis=1, inplace=True)
to_keep = []
flags_out = ['angle', 'band', 'arCoeff', 'Mag']
flags_in = ['mean', 'std', 'skewness', 'kurtosis']
for col in X_train.columns:
    reject = any(re.search(flag, col) for flag in flags_out)
    if not reject:
        reject = not any(re.search(flag, col) for flag in flags_in)
    if not reject and col not in to_keep:
        to_keep.append(col)
to_keep.sort()
X_train = X_train[to_keep]
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train.activity)
score_train = clf.score(X_train, y_train.activity)
print('Random Forest accuracy on training data: {0}'.format(round(score_train, 5)))
feat_imp = pd.Series(clf.feature_importances_, index=X_train.columns)
feat_imp_sorted = feat_imp.sort_values(ascending=False)
print('Most important features:')
print(feat_imp_sorted[:10])
X_test = pd.read_table('./UCI HAR Dataset/test/X_test.txt', sep='\s+', names=features)
X_test = X_test[to_keep]
with open('./UCI HAR Dataset/test/y_test.txt') as open_y_test:
    y_test = [str(line).rstrip()[0] for line in open_y_test.readlines()]
y_test = pd.DataFrame(y_test, columns=['activity_cat'])
y_test['activity'] = y_test.activity_cat.map(lambda x: activity_dict[x])
prediction = clf.predict(X_test)
score_test = clf.score(X_test, y_test.activity)
precision_test = skmet.precision_score(y_test.activity, prediction, average='micro')
recall_test = skmet.recall_score(y_test.activity, prediction, average='micro')
f1_test = skmet.f1_score(y_test.activity, prediction, average='micro')
scores_rounded = [round(x, 5) for x in [score_test, precision_test, recall_test, f1_test]]
print('\nRandom Forest scores on test data (global):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    scores_rounded[0], scores_rounded[1], scores_rounded[2], scores_rounded[3]))
precision_test = skmet.precision_score(y_test.activity, prediction, average='macro')
recall_test = skmet.recall_score(y_test.activity, prediction, average='macro')
f1_test = skmet.f1_score(y_test.activity, prediction, average='macro')
scores_rounded = [round(x, 5) for x in [score_test, precision_test, recall_test, f1_test]]
print('\nRandom Forest scores on test data (per label and unweighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    scores_rounded[0], scores_rounded[1], scores_rounded[2], scores_rounded[3]))
precision_test = skmet.precision_score(y_test.activity, prediction, average='weighted')
recall_test = skmet.recall_score(y_test.activity, prediction, average='weighted')
f1_test = skmet.f1_score(y_test.activity, prediction, average='weighted')
scores_rounded = [round(x, 5) for x in [score_test, precision_test, recall_test, f1_test]]
print('\nRandom Forest scores on test data (per label and weighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    scores_rounded[0], scores_rounded[1], scores_rounded[2], scores_rounded[3]))
conf_matrix = pd.DataFrame(skmet.confusion_matrix(y_test.activity, prediction), columns=activity_list_abr, index=activity_list_abr)
print('\nConfusion matrix:')
print(conf_matrix)
print('\n\n-----BLACK BOX APPROACH-----\n')
X_train_bb = pd.read_table('./UCI HAR Dataset/train/X_train.txt', sep='\s+', names=features)
clf_bb = RandomForestClassifier(n_estimators=50)
clf_bb.fit(X_train_bb, y_train.activity)
score_train = clf_bb.score(X_train_bb, y_train.activity)
print('Random Forest accuracy on training data: {0}'.format(round(score_train, 5)))
feat_imp = pd.Series(clf_bb.feature_importances_, index=X_train_bb.columns)
feat_imp_sorted = feat_imp.sort_values(ascending=False)
print('Most important features:')
print(feat_imp_sorted[:10])
X_test_bb = pd.read_table('./UCI HAR Dataset/test/X_test.txt', sep='\s+', names=features)
prediction_bb = clf_bb.predict(X_test_bb)
score_test_bb = clf_bb.score(X_test_bb, y_test.activity)
precision_test_bb = skmet.precision_score(y_test.activity, prediction_bb, average='micro')
recall_test_bb = skmet.recall_score(y_test.activity, prediction_bb, average='micro')
f1_test_bb = skmet.f1_score(y_test.activity, prediction_bb, average='micro')
scores_rounded_bb = [round(x, 5) for x in [score_test_bb, precision_test_bb, recall_test_bb, f1_test_bb]]
print('\nRandom Forest scores on test data (global):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    scores_rounded_bb[0], scores_rounded_bb[1], scores_rounded_bb[2], scores_rounded_bb[3]))
precision_test_bb = skmet.precision_score(y_test.activity, prediction_bb, average='macro')
recall_test_bb = skmet.recall_score(y_test.activity, prediction_bb, average='macro')
f1_test_bb = skmet.f1_score(y_test.activity, prediction_bb, average='macro')
scores_rounded_bb = [round(x, 5) for x in [score_test_bb, precision_test_bb, recall_test_bb, f1_test_bb]]
print('\nRandom Forest scores on test data (per label and unweighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    scores_rounded_bb[0], scores_rounded_bb[1], scores_rounded_bb[2], scores_rounded_bb[3]))
precision_test_bb = skmet.precision_score(y_test.activity, prediction_bb, average='weighted')
recall_test_bb = skmet.recall_score(y_test.activity, prediction_bb, average='weighted')
f1_test_bb = skmet.f1_score(y_test.activity, prediction_bb, average='weighted')
scores_rounded_bb = [round(x, 5) for x in [score_test_bb, precision_test_bb, recall_test_bb, f1_test_bb]]
print('\nRandom Forest scores on test data (per label and weighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    scores_rounded_bb[0], scores_rounded_bb[1], scores_rounded_bb[2], scores_rounded_bb[3]))
conf_matrix_bb = pd.DataFrame(skmet.confusion_matrix(y_test.activity, prediction_bb), columns=activity_list_abr, index=activity_list_abr)
print('\nConfusion matrix:')
print(conf_matrix_bb)