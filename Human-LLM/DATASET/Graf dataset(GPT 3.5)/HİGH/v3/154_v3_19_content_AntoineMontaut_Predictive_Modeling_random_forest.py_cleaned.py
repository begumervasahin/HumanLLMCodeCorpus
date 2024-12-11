import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as skmet
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs',
                 'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs',
                 '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
def fonk1(file_path):
    b4 = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            _, b5 = str(line).rstrip().split(' ')
            b5 = re.sub(r'[-(),]', '_', b5)
            b5 = b5.replace('()', '').replace('__', '_').replace('BodyBody', 'Body')
            if b5[-1] == '_':
                b5 = b5[:-1]
            b4.append(b5)
    return b4
def fonk2(file_path, b4):
    b6 = pd.read_table(file_path, sep='\s+', names=b4)
    return b6
def fonk3(X, y):
    X['b8'] = y['b8']
    fig, b7 = plt.subplots(2, 3, figsize=(15, 10))
    for ax, act in zip(b7.ravel(), b1):
        ax.hist(X[X.b8 = = act]['fAccMag_mean'], bins=20)
        ax.set_xlim([-1.0, 1.0])
        ax.set_title(act)
        if ax.is_first_row():
            ax.set_ylabel('Dynamic Activity')
        if ax.is_last_row():
            ax.set_ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    X.drop('b8', b9 = 1, inplace=True)
def fonk4(X):
    b10 = ['angle', 'band', 'arCoeff', 'Mag']
    b11 = ['mean', 'std', 'skewness', 'kurtosis']
    b12 = [col for col in X.columns if not any(flag in col for flag in b10) and any(flag in col for flag in b11)]
    return X[b12]
def fonk5(b23, b24, b25, b26):
    b13 = RandomForestClassifier(n_estimators=50)
    b13.fit(b23, b24)
    b14 = b13.score(b23, b24)
    print('Random Forest accuracy on training b6:', round(b14, 5))
    b15 = pd.Series(b13.feature_importances_, index=b23.columns)
    b16 = b15.sort_values(ascending=False)
    print('Most important b4:')
    print(b16[:10])
    b17 = b13.score(b25, b26)
    b18 = b13.predict(b25)
    print('\nRandom Forest scores on test b6 (global):')
    print('\tAccuracy:', round(b17, 5))
    b19 = skmet.precision_score(b26, b18, average='micro')
    b20 = skmet.recall_score(b26, b18, average='micro')
    b21 = skmet.f1_score(b26, b18, average='micro')
    print('\tPrecision:', round(b19, 5))
    print('\tRecall:', round(b20, 5))
    print('\tF1:', round(b21, 5))
    b22 = pd.DataFrame(skmet.confusion_matrix(b26, b18), columns=b2, index=b2)
    print('\nConfusion matrix:')
    print(b22)
def fonk6():
    b4 = fonk1('./UCI HAR Dataset/b4.txt')
    b23 = fonk2('./UCI HAR Dataset/train/b23.txt', b4)
    b24 = pd.read_table('./UCI HAR Dataset/train/b24.txt', header=None, names=['activity_cat'])
    b24['b8'] = b24['activity_cat'].map(b3)
    b25 = fonk2('./UCI HAR Dataset/test/b25.txt', b4)
    b26 = pd.read_table('./UCI HAR Dataset/test/b26.txt', header=None, names=['activity_cat'])
    b26['b8'] = b26['activity_cat'].map(b3)
    fonk3(b23.copy(), b24.copy())
    b27 = fonk4(b23.copy())
    b28 = fonk4(b25.copy())
    fonk5(b27, b24['b8'], b28, b26['b8'])
if b29 = = "__main__":
    fonk6()