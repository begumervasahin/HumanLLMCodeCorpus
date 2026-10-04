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
b6 = './UCI HAR Dataset/train/b26.txt'
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
def fonk2(data_file, labels_file, b9):
    b11 = pd.read_table(data_file, sep='\s+', names=b9)
    with open(labels_file, 'r') as f:
        b12 = [line.strip() for line in f]
    b12 = pd.DataFrame(b12, columns=['activity_cat'])
    b12['activity'] = b12['activity_cat'].map(b3)
    return b11, b12
def fonk3(X_train, b26):
    X_train['activity'] = b26['activity']
    plt.figure(b13 = (12, 8))
    for b15, act in enumerate(b1, 1):
        plt.subplot(2, 3, b15)
        plt.hist(X_train[X_train['activity'] == act]['fAccMag_mean'], b14 = 30)
        plt.xlim([-1.0, 1.0])
        plt.title(act)
        if b15 = = 1:
            plt.ylabel('Dynamic Activity')
        if b15 = = 4:
            plt.ylabel('Static Activity')
    plt.tight_layout()
    plt.show()
    X_train.drop('activity', b16 = 1, inplace=True)
def fonk4(X_train):
    b17 = []
    b18 = ['angle', 'band', 'arCoeff', 'Mag']
    b19 = ['mean', 'std', 'skewness', 'kurtosis']
    for col in X_train.columns:
        if not any(re.search(flag, col) for flag in b18) and any(re.search(flag, col) for flag in b19):
            b17.append(col)
    b17.sort()
    return X_train[b17]
def fonk5(X_train, b26):
    b20 = RandomForestClassifier(n_estimators=50)
    b20.fit(X_train, b26)
    return b20
def fonk6(b20, X_test, b30, activity_list_abr):
    b21 = b20.predict(X_test)
    b22 = {
        'accuracy': b20.score(X_test, b30),
        'precision': precision_score(b30, b21, b23 = 'micro'),
        'recall': recall_score(b30, b21, b23 = 'micro'),
        'f1': f1_score(b30, b21, b23 = 'micro')
    }
    b24 = {k: round(v, 5) for k, v in b22.items()}
    print(f'\nRandom Forest b22 on test data (global):\n\tAccuracy: {b24["accuracy"]}\n\tPrecision: {b24["precision"]}\n\tRecall: {b24["recall"]}\n\tF1: {b24["f1"]}')
    b25 = pd.DataFrame(confusion_matrix(b30, b21), columns=activity_list_abr, index=activity_list_abr)
    print('\nConfusion matrix:')
    print(b25)
def fonk7():
    b9 = fonk1(b4)
    X_train, b26 = fonk2(b5, b6, b9)
    print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
    b27 = fonk4(X_train)
    b28 = fonk5(b27, b26['activity'])
    fonk6(b28, b27, b26['activity'], b2)
    print('\n\n-----BLACK BOX APPROACH-----\n')
    b29 = fonk5(X_train, b26['activity'])
    fonk6(b29, X_train, b26['activity'], b2)
    X_test, b30 = fonk2(b7, b8, b9)
    b31 = fonk4(X_test)
    print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
    fonk6(b28, b31, b30['activity'], b2)
    print('\n\n-----BLACK BOX APPROACH-----\n')
    fonk6(b29, X_test, b30['activity'], b2)
if b32 = = "__main__":
    fonk7()