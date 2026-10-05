import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import sklearn.metrics as skmet
activity_list = ['Walking', 'Walking upstairs', 'Walking downstairs',
                 'Sitting', 'Standing', 'Laying']
activity_list_abr = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
activity_dict = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs',
                 '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
features = []
with open('./UCI HAR Dataset/features.txt', 'r') as open_features:
    for line in open_features.readlines():
        dummy, feature = str(line).rstrip().split(' ')
        feature = re.sub(r'[-(),]', '_', feature)
        feature = feature.replace('()', '')
        feature = feature.replace('__', '_')
        feature = feature.replace('BodyBody', 'Body').replace('Body', '')
        if feature[-1] == '_':
            feature = feature[:-1]
        features.append(feature)
X_train = pd.read_table('./UCI HAR Dataset/train/X_train.txt', sep='\s+', names=features)
y_train = pd.read_table('./UCI HAR Dataset/train/y_train.txt', header=None, names=['activity_cat'])
y_train['activity'] = y_train['activity_cat'].map(activity_dict)
def preview_plots():
    X_train['activity'] = y_train['activity']
    plt.figure(figsize=(10, 6))
    for i, act in enumerate(activity_list, start=1):
        plt.subplot(2, 3, i)
        plt.hist(X_train[X_train['activity'] == act]['fAccMag_mean'])
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if i == 1:
            plt.ylabel('Dynamic Activity')
        if i == 4:
            plt.ylabel('Static Activity')
    plt.show()
    X_train.drop('activity', axis=1, inplace=True)
to_keep = []
flags_out = ['angle', 'band', 'arCoeff', 'Mag']
flags_in = ['mean', 'std', 'skewness', 'kurtosis']
for col in X_train.columns:
    reject = any(re.search(flag, col) for flag in flags_out)
    if not reject:
        reject = not any(re.search(flag, col) for flag in flags_in)
    if not reject and (col not in to_keep):
        to_keep.append(col)
to_keep.sort()
X_train = X_train[to_keep]
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train['activity'])
score_train = clf.score(X_train, y_train['activity'])
print('Random Forest accuracy on training data:', round(score_train, 5))
feat_imp = pd.Series(clf.feature_importances_, index=X_train.columns).sort_values(ascending=False)
print('Most important features:')
print(feat_imp[:10])
X_test = pd.read_table('./UCI HAR Dataset/test/X_test.txt', sep='\s+', names=features)
X_test = X_test[to_keep]
y_test = pd.read_table('./UCI HAR Dataset/test/y_test.txt', header=None, names=['activity_cat'])
y_test['activity'] = y_test['activity_cat'].map(activity_dict)
prediction = clf.predict(X_test)
score_test = clf.score(X_test, y_test['activity'])
precision_test = skmet.precision_score(y_test['activity'], prediction, average='micro')
recall_test = skmet.recall_score(y_test['activity'], prediction, average='micro')
f1_test = skmet.f1_score(y_test['activity'], prediction, average='micro')
print('\nRandom Forest scores on test data (global):')
print('\tAccuracy:', round(score_test, 5))
print('\tPrecision:', round(precision_test, 5))
print('\tRecall:', round(recall_test, 5))
print('\tF1:', round(f1_test, 5))
conf_matrix = pd.DataFrame(skmet.confusion_matrix(y_test['activity'], prediction), columns=activity_list_abr, index=activity_list_abr)
print('\nConfusion matrix:')
print(conf_matrix)
print('\n\n-----BLACK BOX APPROACH-----\n')
clf_bb = RandomForestClassifier(n_estimators=50)
clf_bb.fit(X_train, y_train['activity'])
score_train_bb = clf_bb.score(X_train, y_train['activity'])
print('Random Forest accuracy on training data (black box):', round(score_train_bb, 5))
feat_imp_bb = pd.Series(clf_bb.feature_importances_, index=X_train.columns).sort_values(ascending=False)
print('Most important features (black box):')
print(feat_imp_bb[:10])
prediction_bb = clf_bb.predict(X_test)
score_test_bb = clf_bb.score(X_test, y_test['activity'])
precision_test_bb = skmet.precision_score(y_test['activity'], prediction_bb, average='micro')
recall_test_bb = skmet.recall_score(y_test['activity'], prediction_bb, average='micro')
f1_test_bb = skmet.f1_score(y_test['activity'], prediction_bb, average='micro')
print('\nRandom Forest scores on test data (global) - Black Box:')
print('\tAccuracy:', round(score_test_bb, 5))
print('\tPrecision:', round(precision_test_bb, 5))
print('\tRecall:', round(recall_test_bb, 5))
print('\tF1:', round(f1_test_bb, 5))
conf_matrix_bb = pd.DataFrame(skmet.confusion_matrix(y_test['activity'], prediction_bb), columns=activity_list_abr, index=activity_list_abr)
print('\nConfusion matrix (Black Box):')
print(conf_matrix_bb)