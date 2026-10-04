import pandas as pd
import matplotlib.pyplot as plt
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import sklearn.metrics as skmet
b1 = ['Walking', 'Walking upstairs', 'Walking downstairs', 'Sitting', 'Standing', 'Laying']
b2 = ['Walk', 'Walk up', 'Walk down', 'Sit', 'Stand', 'Lay']
b3 = {'1': 'Walking', '2': 'Walking upstairs', 'b9': 'Walking downstairs', '4': 'Sitting', '5': 'Standing', '6': 'Laying'}
def fonk1(b4):
    b4 = b4.replace('-', '_').replace('(', '_').replace(')', '').replace(',', '').replace('__', '_')
    b4 = b4.replace('BodyBody', 'Body').replace('Body', '')
    return b4.rstrip('_')
def fonk2(filepath):
    with open(filepath, 'r') as file:
        b5 = [fonk1(line.split()[1]) for line in file]
    return b5
def fonk3(b5):
    b6 = pd.read_table('./UCI HAR Dataset/train/b6.txt', sep='\s+', names=b5)
    b7 = pd.read_table('./UCI HAR Dataset/train/b7.txt', header=None, names=['activity_cat'])
    b7['activity'] = b7['activity_cat'].map(b3)
    return b6, b7
def fonk4(b6, b7):
    b6['activity'] = b7['activity']
    plt.figure(b8 = (12, 8))
    for i, activity in enumerate(b1):
        plt.subplot(2, b9, i + 1)
        plt.hist(b6[b6['activity'] == activity]['fAccMag_mean'])
        plt.xlim([-1.0, 1.0])
        plt.title(activity)
        if i % b9 = = 0:
            plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    b6.drop('activity', b10 = 1, inplace=True)
def fonk5(b6):
    b11 = []
    b12 = ['angle', 'band', 'arCoeff', 'Mag']
    b13 = ['mean', 'std', 'skewness', 'kurtosis']
    for col in b6.b22:
        if not any(flag in col for flag in b12) and any(flag in col for flag in b13):
            b11.append(col)
    return b6[b11]
def fonk6(b6, b7):
    b14 = RandomForestClassifier(n_estimators=50, random_state=0)
    b14.fit(b6, b7['activity'])
    return b14
def fonk7(b14, b18, b19):
    b15 = b14.predict(b18)
    b16 = {
        'Accuracy': skmet.accuracy_score(b19['activity'], b15),
        'Precision': skmet.precision_score(b19['activity'], b15, b17 = 'micro'),
        'Recall': skmet.recall_score(b19['activity'], b15, b17 = 'micro'),
        'F1': skmet.f1_score(b19['activity'], b15, b17 = 'micro'),
    }
    return b16, skmet.confusion_matrix(b19['activity'], b15)
def fonk8(b5, b11):
    b18 = pd.read_table('./UCI HAR Dataset/test/b18.txt', sep='\s+', names=b5)
    b18 = b18[b11]
    b19 = pd.read_table('./UCI HAR Dataset/test/b19.txt', header=None, names=['activity_cat'])
    b19['activity'] = b19['activity_cat'].map(b3)
    return b18, b19
def fonk9():
    b5 = fonk2('./UCI HAR Dataset/b5.txt')
    b6, b7 = fonk3(b5)
    b6 = fonk5(b6)
    print('\n\n-----DOMAIN KNOWLEDGE APPROACH-----\n')
    b14 = fonk6(b6, b7)
    b20 = b14.score(b6, b7['activity'])
    print(f'Random Forest accuracy on training data: {b20:.5f}')
    b18, b19 = fonk8(b5, b6.b22)
    b16, b21 = fonk7(b14, b18, b19)
    print(f'\nRandom Forest b16 on test data (global):\n\tAccuracy: {b16["Accuracy"]:.5f}\n\tPrecision: {b16["Precision"]:.5f}\n\tRecall: {b16["Recall"]:.5f}\n\tF1: {b16["F1"]:.5f}')
    print('\nConfusion matrix:')
    print(pd.DataFrame(b21, b22 = b2, index=b2))
    print('\n\n-----BLACK BOX APPROACH-----\n')
    b23 = pd.read_table('./UCI HAR Dataset/train/b6.txt', sep='\s+', names=b5)
    b24 = RandomForestClassifier(n_estimators=50, random_state=0)
    b24.fit(b23, b7['activity'])
    b25 = b24.score(b23, b7['activity'])
    print(f'Random Forest accuracy on training data: {b25:.5f}')
    b26 = pd.read_table('./UCI HAR Dataset/test/b18.txt', sep='\s+', names=b5)
    scores_bb, b27 = fonk7(b24, b26, b19)
    print(f'\nRandom Forest b16 on test data (global):\n\tAccuracy: {scores_bb["Accuracy"]:.5f}\n\tPrecision: {scores_bb["Precision"]:.5f}\n\tRecall: {scores_bb["Recall"]:.5f}\n\tF1: {scores_bb["F1"]:.5f}')
    print('\nConfusion matrix:')
    print(pd.DataFrame(b27, b22 = b2, index=b2))
if b28 = = "__main__":
    fonk9()