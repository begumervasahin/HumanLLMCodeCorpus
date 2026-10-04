import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import sklearn.metrics as skmet
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs', 'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs', '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
with open('./UCI HAR Dataset/b4.txt', 'r') as open_features:
    b4 = []
    for line in open_features.readlines():
        dummy, b5 = str(line).rstrip().split(' ')
        for char in ['-', '(', ',', ')']:
            b5 = b5.replace(char, '_')
        b5 = b5.replace('()', '')
        b5 = b5.replace('__', '_')
        for elem in ['BodyBody', 'Body']:
            b5 = b5.replace(elem, '')
        if b5[-1] == '_':
            b5 = b5[:-1]
        b4.append(b5)
b6 = pd.read_table('./UCI HAR Dataset/train/b6.txt', sep='\s+', names=b4)
with open('./UCI HAR Dataset/train/b7.txt') as open_y_train:
    b7 = [str(line).rstrip()[0] for line in open_y_train.readlines()]
b7 = pd.DataFrame(b7, columns=['activity_cat'])
b7['b9'] = b7.activity_cat.map(lambda x: b3[x])
def fonk1():
    b6['b9'] = b7.b9
    plt.figure(b8 = (12, 8))
    for b10, act in enumerate(b1, 1):
        plt.subplot(2, 3, b10)
        plt.hist(b6[b6.b9 = = act].fAccMag_mean, bins=30)
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if b10 = = 1:
            plt.ylabel('Dynamic Activity')
        if b10 = = 4:
            plt.ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    b6.drop('b9', b11 = 1, inplace=True)
b12 = []
b13 = ['angle', 'band', 'arCoeff', 'Mag']
b14 = ['mean', 'std', 'skewness', 'kurtosis']
for col in b6.columns:
    b15 = any(re.search(flag, col) for flag in b13)
    if not b15:
        b15 = not any(re.search(flag, col) for flag in b14)
    if not b15 and col not in b12:
        b12.append(col)
b12.sort()
b6 = b6[b12]
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
b16 = RandomForestClassifier(n_estimators=50)
b16.fit(b6, b7.b9)
b17 = b16.score(b6, b7.b9)
print('Random Forest accuracy on training data: {0}'.format(round(b17, 5)))
b18 = pd.Series(b16.feature_importances_, index=b6.columns)
b19 = b18.sort_values(ascending=False)
print('Most important b4:')
print(b19[:10])
b20 = pd.read_table('./UCI HAR Dataset/test/b20.txt', sep='\s+', names=b4)
b20 = b20[b12]
with open('./UCI HAR Dataset/test/b21.txt') as open_y_test:
    b21 = [str(line).rstrip()[0] for line in open_y_test.readlines()]
b21 = pd.DataFrame(b21, columns=['activity_cat'])
b21['b9'] = b21.activity_cat.map(lambda x: b3[x])
b22 = b16.predict(b20)
b23 = b16.score(b20, b21.b9)
b24 = skmet.precision_score(b21.b9, b22, average='micro')
b25 = skmet.recall_score(b21.b9, b22, average='micro')
b26 = skmet.f1_score(b21.b9, b22, average='micro')
b27 = [round(x, 5) for x in [b23, b24, b25, b26]]
print('\nRandom Forest scores on test data (global):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b27[0], b27[1], b27[2], b27[3]))
b24 = skmet.precision_score(b21.b9, b22, average='macro')
b25 = skmet.recall_score(b21.b9, b22, average='macro')
b26 = skmet.f1_score(b21.b9, b22, average='macro')
b27 = [round(x, 5) for x in [b23, b24, b25, b26]]
print('\nRandom Forest scores on test data (per label and unweighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b27[0], b27[1], b27[2], b27[3]))
b24 = skmet.precision_score(b21.b9, b22, average='weighted')
b25 = skmet.recall_score(b21.b9, b22, average='weighted')
b26 = skmet.f1_score(b21.b9, b22, average='weighted')
b27 = [round(x, 5) for x in [b23, b24, b25, b26]]
print('\nRandom Forest scores on test data (per label and weighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b27[0], b27[1], b27[2], b27[3]))
b28 = pd.DataFrame(skmet.confusion_matrix(b21.b9, b22), columns=b2, index=b2)
print('\nConfusion matrix:')
print(b28)
print('\n\n-----BLACK BOX APPROACH-----\n')
b29 = pd.read_table('./UCI HAR Dataset/train/b6.txt', sep='\s+', names=b4)
b30 = RandomForestClassifier(n_estimators=50)
b30.fit(b29, b7.b9)
b17 = b30.score(b29, b7.b9)
print('Random Forest accuracy on training data: {0}'.format(round(b17, 5)))
b18 = pd.Series(b30.feature_importances_, index=b29.columns)
b19 = b18.sort_values(ascending=False)
print('Most important b4:')
print(b19[:10])
b31 = pd.read_table('./UCI HAR Dataset/test/b20.txt', sep='\s+', names=b4)
b32 = b30.predict(b31)
b33 = b30.score(b31, b21.b9)
b34 = skmet.precision_score(b21.b9, b32, average='micro')
b35 = skmet.recall_score(b21.b9, b32, average='micro')
b36 = skmet.f1_score(b21.b9, b32, average='micro')
b37 = [round(x, 5) for x in [b33, b34, b35, b36]]
print('\nRandom Forest scores on test data (global):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b37[0], b37[1], b37[2], b37[3]))
b34 = skmet.precision_score(b21.b9, b32, average='macro')
b35 = skmet.recall_score(b21.b9, b32, average='macro')
b36 = skmet.f1_score(b21.b9, b32, average='macro')
b37 = [round(x, 5) for x in [b33, b34, b35, b36]]
print('\nRandom Forest scores on test data (per label and unweighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b37[0], b37[1], b37[2], b37[3]))
b34 = skmet.precision_score(b21.b9, b32, average='weighted')
b35 = skmet.recall_score(b21.b9, b32, average='weighted')
b36 = skmet.f1_score(b21.b9, b32, average='weighted')
b37 = [round(x, 5) for x in [b33, b34, b35, b36]]
print('\nRandom Forest scores on test data (per label and weighted averaged):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b37[0], b37[1], b37[2], b37[3]))
b38 = pd.DataFrame(skmet.confusion_matrix(b21.b9, b32), columns=b2, index=b2)
print('\nConfusion matrix:')
print(b38)