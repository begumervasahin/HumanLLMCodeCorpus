import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import sklearn.metrics as skmet
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs',
                'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down',
                     'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs',
                 '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
b4 = open('./UCI HAR Dataset/b5.txt', 'r')
b5 = []
for line in b4.readlines():
    dummy, b6 = str(line).rstrip().split(' ')
    for char in ['-', '(', ',']:
        b6 = b6.replace(char, '_')
    b6 = b6.replace('()', '')
    b6 = b6.replace(')', '')
    b6 = b6.replace('__', '_')
    for elem in ['BodyBody', 'Body']:
        b6 = b6.replace(elem, '')
    if b6[-1] == '_':
        b6 = b6[:-1]
    b5.append(b6)
b7 = pd.read_table('./UCI HAR Dataset/train/b7.txt', sep='\s+', names=b5)
b8 = open('./UCI HAR Dataset/train/b9.txt')
b9 = [str(line).rstrip()[0] for line in b8.readlines()]
b9 = pd.DataFrame(b9, columns=['activity_cat'])
b9['b10'] = b9.activity_cat.map(lambda x: b3[x])
def fonk1():
    b7.b10 = b9.b10
    a1 = 0
    for act in b1:
        a1 += 1
        plt.subplot(2, 3, a1)
        plt.hist(b7[b7.b10 = = act].fAccMag_mean)
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if a1 = = 1:
            plt.ylabel('Dynamic Activity')
        if a1 = = 4:
            plt.ylabel('Static Activity')
    plt.show()
    b7.drop('b10', b11 = 1, inplace=True)
b12 = []
b13 = ['angle', 'band', 'arCoeff', 'Mag']
b14 = ['mean', 'std', 'skewness', 'kurtosis']
for col in b7.columns:
    b15 = False
    for flag in b13:
        if re.search(flag, col):
            b15 = True
            break
    if not b15:
        b15 = True
        for flag in b14:
            if re.search(flag, col):
                b15 = False
                break
    if not b15 and (col not in b12):
        b12.append(col)
b12.sort()
b7 = b7[b12]
b16 = RandomForestClassifier(n_estimators=50)
b16 = b16.fit(b7, b9.b10)
b17 = b16.score(b7, b9.b10)
print('Random Forest accuracy on training data: {0}'.format(round(b17, 5)))
b18 = pd.Series(b16.feature_importances_, b30=b7.columns)
b19 = b18.sort_values(ascending=False)
print('Most important b5:')
print(b19[:10])
b20 = pd.read_table('./UCI HAR Dataset/test/b20.txt', sep='\s+', names=b5)
b20 = b20[b12]
b21 = open('./UCI HAR Dataset/test/b22.txt')
b22 = [str(line).rstrip()[0] for line in b21.readlines()]
b22 = pd.DataFrame(b22, columns=['activity_cat'])
b22['b10'] = b22.activity_cat.map(lambda x: b3[x])
b23 = b16.predict(b20)
b24 = b16.score(b20, b22.b10)
b25 = skmet.precision_score(b22.b10, b23, average='micro')
b26 = skmet.recall_score(b22.b10, b23, average='micro')
b27 = skmet.f1_score(b22.b10, b23, average='micro')
b28 = map(lambda x: round(x, 5), [b24, b25, b26, b27])
print('\nRandom Forest scores on test data (global):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b28[0], b28[1], b28[2], b28[3]))
b25 = skmet.precision_score(b22.b10, b23, average='macro')
b26 = skmet.recall_score(b22.b10, b23, average='macro')
b27 = skmet.f1_score(b22.b10, b23, average='macro')
b28 = map(lambda x: round(x, 5), [b25, b26, b27])
print('\nRandom Forest scores on test data (per label and unweighted averaged):\n\tPrecision: {0}\n\tRecall: {1}\n\tF1: {2}'.format(
    b28[0], b28[1], b28[2]))
b25 = skmet.precision_score(b22.b10, b23, average='weighted')
b26 = skmet.recall_score(b22.b10, b23, average='weighted')
b27 = skmet.f1_score(b22.b10, b23, average='weighted')
b28 = map(lambda x: round(x, 5), [b25, b26, b27])
print('\nRandom Forest scores on test data (per label and weighted averaged):\n\tPrecision: {0}\n\tRecall: {1}\n\tF1: {2}'.format(
    b28[0], b28[1], b28[2]))
b29 = pd.DataFrame(skmet.confusion_matrix(b22.b10, b23), columns=b2,
                           b30 = b2)
print('\nConfusion matrix:')
print(b29)
b31 = pd.read_table('./UCI HAR Dataset/train/b7.txt', sep='\s+', names=b5)
b32 = RandomForestClassifier(n_estimators=50)
b32.fit(b31, b9.b10)
b17 = b32.score(b31, b9.b10)
print('Random Forest accuracy on training data: {0}'.format(round(b17, 5)))
b18 = pd.Series(b32.feature_importances_, b30=b31.columns)
b19 = b18.sort_values(ascending=False)
print('Most important b5:')
print(b19[:10])
b33 = pd.read_table('./UCI HAR Dataset/test/b20.txt', sep='\s+', names=b5)
b21 = open('./UCI HAR Dataset/test/b22.txt')
b22 = [str(line).rstrip()[0] for line in b21.readlines()]
b22 = pd.DataFrame(b22, columns=['activity_cat'])
b22['b10'] = b22.activity_cat.map(lambda x: b3[x])
b23 = b32.predict(b33)
b24 = b32.score(b33, b22.b10)
b25 = skmet.precision_score(b22.b10, b23, average='micro')
b26 = skmet.recall_score(b22.b10, b23, average='micro')
b27 = skmet.f1_score(b22.b10, b23, average='micro')
b28 = map(lambda x: round(x, 5), [b24, b25, b26, b27])
print('\nRandom Forest scores on test data (global):\n\tAccuracy: {0}\n\tPrecision: {1}\n\tRecall: {2}\n\tF1: {3}'.format(
    b28[0], b28[1], b28[2], b28[3]))
b25 = skmet.precision_score(b22.b10, b23, average='macro')
b26 = skmet.recall_score(b22.b10, b23, average='macro')
b27 = skmet.f1_score(b22.b10, b23, average='macro')
b28 = map(lambda x: round(x, 5), [b25, b26, b27])
print('\nRandom Forest scores on test data (per label and unweighted averaged):\n\tPrecision: {0}\n\tRecall: {1}\n\tF1: {2}'.format(
    b28[0], b28[1], b28[2]))
b25 = skmet.precision_score(b22.b10, b23, average='weighted')
b26 = skmet.recall_score(b22.b10, b23, average='weighted')
b27 = skmet.f1_score(b22.b10, b23, average='weighted')
b28 = map(lambda x: round(x, 5), [b25, b26, b27])
print('\nRandom Forest scores on test data (per label and weighted averaged):\n\tPrecision: {0}\n\tRecall: {1}\n\tF1: {2}'.format(
    b28[0], b28[1], b28[2]))
b29 = pd.DataFrame(skmet.confusion_matrix(b22.b10, b23), columns=b2,
                           b30 = b2)
print('\nConfusion matrix:')
print(b29)