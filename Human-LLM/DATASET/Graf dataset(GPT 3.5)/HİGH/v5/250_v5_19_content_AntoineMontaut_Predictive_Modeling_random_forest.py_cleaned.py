import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs',
                 'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs',
                 '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
def fonk1(b4):
    b4 = re.sub(r'[-(),]', '_', b4)
    b4 = b4.replace('()', '').replace('__', '_').replace('BodyBody', 'Body').replace('Body', '')
    if b4.endswith('_'):
        b4 = b4[:-1]
    return b4
with open('./UCI HAR Dataset/b5.txt', 'r') as file:
    b5 = [fonk1(line.split()[1]) for line in file]
b6 = pd.read_csv('./UCI HAR Dataset/train/b6.txt', delim_whitespace=True, names=b5)
b7 = pd.read_csv('./UCI HAR Dataset/train/b7.txt', header=None, names=['activity_cat'])
b7['activity'] = b7['activity_cat'].map(b3)
def fonk2():
    b6['activity'] = b7['activity']
    plt.figure(b8 = (10, 6))
    for b10, act in enumerate(b1, b9 = 1):
        plt.subplot(2, 3, b10)
        plt.hist(b6[b6['activity'] == act]['fAccMag_mean'])
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if b10 = = 1:
            plt.ylabel('Dynamic Activity')
        if b10 = = 4:
            plt.ylabel('Static Activity')
    plt.show()
    b6.drop('activity', b11 = 1, inplace=True)
def fonk3(b6):
    b12 = ['angle', 'band', 'arCoeff', 'Mag']
    b13 = ['mean', 'std', 'skewness', 'kurtosis']
    b14 = [col for col in b6.columns if not any(flag in col for flag in b12) and any(flag in col for flag in b13)]
    return b6[b14]
b6 = fonk3(b6)
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
b15 = RandomForestClassifier(n_estimators=50)
b15.fit(b6, b7['activity'])
b16 = accuracy_score(b7['activity'], b15.predict(b6))
print('Random Forest accuracy on training data:', round(b16, 5))
b17 = pd.Series(b15.feature_importances_, index=b6.columns).sort_values(ascending=False)
print('Most important b5:')
print(b17[:10])
b18 = pd.read_csv('./UCI HAR Dataset/test/b18.txt', delim_whitespace=True, names=b5)
b18 = fonk3(b18)
b19 = pd.read_csv('./UCI HAR Dataset/test/b19.txt', header=None, names=['activity_cat'])
b19['activity'] = b19['activity_cat'].map(b3)
b20 = b15.predict(b18)
b21 = accuracy_score(b19['activity'], b20)
b22 = precision_score(b19['activity'], b20, average='micro')
b23 = recall_score(b19['activity'], b20, average='micro')
b24 = f1_score(b19['activity'], b20, average='micro')
print('\nRandom Forest scores on test data (global):')
print('\tAccuracy:', round(b21, 5))
print('\tPrecision:', round(b22, 5))
print('\tRecall:', round(b23, 5))
print('\tF1:', round(b24, 5))
b25 = pd.DataFrame(confusion_matrix(b19['activity'], b20), columns=b2, index=b2)
print('\nConfusion matrix:')
print(b25)
print('\n\n-----BLACK BOX APPROACH-----\n')
b26 = RandomForestClassifier(n_estimators=50)
b26.fit(b6, b7['activity'])
b27 = accuracy_score(b7['activity'], b26.predict(b6))
print('Random Forest accuracy on training data (black box):', round(b27, 5))
b28 = pd.Series(b26.feature_importances_, index=b6.columns).sort_values(ascending=False)
print('Most important b5 (black box):')
print(b28[:10])
b29 = b26.predict(b18)
b30 = accuracy_score(b19['activity'], b29)
b31 = precision_score(b19['activity'], b29, average='micro')
b32 = recall_score(b19['activity'], b29, average='micro')
b33 = f1_score(b19['activity'], b29, average='micro')
print('\nRandom Forest scores on test data (global) - Black Box:')
print('\tAccuracy:', round(b30, 5))
print('\tPrecision:', round(b31, 5))
print('\tRecall:', round(b32, 5))
print('\tF1:', round(b33, 5))
b34 = pd.DataFrame(confusion_matrix(b19['activity'], b29), columns=b2, index=b2)
print('\nConfusion matrix (Black Box):')
print(b34)