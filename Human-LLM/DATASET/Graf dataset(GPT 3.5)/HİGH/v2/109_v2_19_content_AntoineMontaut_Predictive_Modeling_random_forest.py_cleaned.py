import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import sklearn.metrics as skmet
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs',
                'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs',
                 '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
b4 = open('./UCI HAR Dataset/b5.txt', 'r')
b5 = []
for line in b4.readlines():
    dummy, b6 = str(line).rstrip().split(' ')
    b6 = re.sub(r'[-(),]', '_', b6)
    b6 = b6.replace('()', '').replace('__', '_').replace('BodyBody', 'Body')
    if b6[-1] == '_':
        b6 = b6[:-1]
    b5.append(b6)
b7 = pd.read_table('./UCI HAR Dataset/train/b7.txt', sep='\s+', names=b5)
b8 = pd.read_table('./UCI HAR Dataset/train/b8.txt', header=None, names=['activity_cat'])
b8['b9'] = b8['activity_cat'].map(b3)
def fonk1():
    b7.b9 = b8.b9
    fig, b10 = plt.subplots(2, 3, figsize=(15, 10))
    for ax, act in zip(b10.ravel(), b1):
        ax.hist(b7[b7.b9 = = act]['fAccMag_mean'], bins=20)
        ax.set_xlim([-1.0, 1.0])
        ax.set_title(act)
        if ax.is_first_row():
            ax.set_ylabel('Dynamic Activity')
        if ax.is_last_row():
            ax.set_ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    b7.drop('b9', b11 = 1, inplace=True)
def fonk2(b7):
    b12 = ['angle', 'band', 'arCoeff', 'Mag']
    b13 = ['mean', 'std', 'skewness', 'kurtosis']
    b14 = [col for col in b7.columns if not any(flag in col for flag in b12) and any(flag in col for flag in b13)]
    return b7[b14]
b7 = fonk2(b7)
b15 = RandomForestClassifier(n_estimators=50)
b15.fit(b7, b8['b9'])
b16 = b15.score(b7, b8['b9'])
print('Random Forest accuracy on training data:', round(b16, 5))
b17 = pd.Series(b15.feature_importances_, index=b7.columns)
b18 = b17.sort_values(ascending=False)
print('Most important b5:')
print(b18[:10])
b19 = pd.read_table('./UCI HAR Dataset/test/b19.txt', sep='\s+', names=b5)
b19 = fonk2(b19)
b20 = pd.read_table('./UCI HAR Dataset/test/b20.txt', header=None, names=['activity_cat'])
b20['b9'] = b20['activity_cat'].map(b3)
b21 = b15.predict(b19)
b22 = b15.score(b19, b20['b9'])
b23 = skmet.precision_score(b20['b9'], b21, average='micro')
b24 = skmet.recall_score(b20['b9'], b21, average='micro')
b25 = skmet.f1_score(b20['b9'], b21, average='micro')
print('\nRandom Forest scores on test data (global):')
print('\tAccuracy:', round(b22, 5))
print('\tPrecision:', round(b23, 5))
print('\tRecall:', round(b24, 5))
print('\tF1:', round(b25, 5))
b23 = skmet.precision_score(b20['b9'], b21, average='macro')
b24 = skmet.recall_score(b20['b9'], b21, average='macro')
b25 = skmet.f1_score(b20['b9'], b21, average='macro')
print('\nRandom Forest scores on test data (per label and unweighted averaged):')
print('\tPrecision:', round(b23, 5))
print('\tRecall:', round(b24, 5))
print('\tF1:', round(b25, 5))
b23 = skmet.precision_score(b20['b9'], b21, average='weighted')
b24 = skmet.recall_score(b20['b9'], b21, average='weighted')
b25 = skmet.f1_score(b20['b9'], b21, average='weighted')
print('\nRandom Forest scores on test data (per label and weighted averaged):')
print('\tPrecision:', round(b23, 5))
print('\tRecall:', round(b24, 5))
print('\tF1:', round(b25, 5))
b26 = pd.DataFrame(skmet.confusion_matrix(b20['b9'], b21), columns=b2, index=b2)
print('\nConfusion matrix:')
print(b26)