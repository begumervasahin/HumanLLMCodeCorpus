import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs', 'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', '3': 'Walking downstairs', '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
b4 = './UCI HAR Dataset/b9.txt'
b5 = './UCI HAR Dataset/train/X_train.txt'
b6 = './UCI HAR Dataset/train/b13.txt'
b7 = './UCI HAR Dataset/test/X_test.txt'
b8 = './UCI HAR Dataset/test/b30.txt'
def fonk1(file_path):
    with open(file_path, 'r') as f:
        b9 = []
        for line in f:
            _, b10 = line.strip().split(' ')
            b10 = re.sub(r'[-(),]', '_', b10).replace('BodyBody', 'Body').strip('_')
            b9.append(b10)
        return b9
b9 = fonk1(b4)
def fonk2(data_file, labels_file, b9):
    b11 = pd.read_table(data_file, sep='\s+', names=b9)
    with open(labels_file, 'r') as f:
        b12 = [line.strip() for line in f]
    b12 = pd.DataFrame(b12, columns=['activity_cat'])
    b12['activity'] = b12['activity_cat'].map(b3)
    return b11, b12
X_train, b13 = fonk2(b5, b6, b9)
def fonk3(X_train, b13):
    X_train['activity'] = b13['activity']
    plt.figure(b14 = (12, 8))
    for b16, act in enumerate(b1, 1):
        plt.subplot(2, 3, b16)
        plt.hist(X_train[X_train['activity'] == act]['fAccMag_mean'], b15 = 30)
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if b16 = = 1:
            plt.ylabel('Dynamic Activity')
        if b16 = = 4:
            plt.ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    X_train.drop('activity', b17 = 1, inplace=True)
def fonk4(X_train):
    b18 = []
    b19 = ['angle', 'band', 'arCoeff', 'Mag']
    b20 = ['mean', 'std', 'skewness', 'kurtosis']
    for col in X_train.columns:
        if not any(re.search(flag, col) for flag in b19) and any(re.search(flag, col) for flag in b20):
            b18.append(col)
    b18.sort()
    return X_train[b18]
b21 = fonk4(X_train)
def fonk5(X_train, b13):
    b22 = RandomForestClassifier(n_estimators=50)
    b22.fit(X_train, b13)
    return b22
def fonk6(b22, X_test, b30, b2):
    b23 = b22.predict(X_test)
    b24 = {
        'accuracy': b22.score(X_test, b30),
        'precision': precision_score(b30, b23, b25 = 'micro'),
        'recall': recall_score(b30, b23, b25 = 'micro'),
        'f1': f1_score(b30, b23, b25 = 'micro')
    }
    b26 = {k: round(v, 5) for k, v in b24.items()}
    print(f'\nRandom Forest b24 on test data (global):\n\tAccuracy: {b26["accuracy"]}\n\tPrecision: {b26["precision"]}\n\tRecall: {b26["recall"]}\n\tF1: {b26["f1"]}')
    b27 = pd.DataFrame(confusion_matrix(b30, b23), columns=b2, index=b2)
    print('\nConfusion matrix:')
    print(b27)
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
b28 = fonk5(b21, b13['activity'])
fonk6(b28, b21, b13['activity'], b2)
print('\n\n-----BLACK BOX APPROACH-----\n')
b29 = fonk5(X_train, b13['activity'])
fonk6(b29, X_train, b13['activity'], b2)
X_test, b30 = fonk2(b7, b8, b9)
b31 = fonk4(X_test)
print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
fonk6(b28, b31, b30['activity'], b2)
print('\n\n-----BLACK BOX APPROACH-----\n')
fonk6(b29, X_test, b30['activity'], b2)