
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
def fonk1(b8, b9):
    return pd.read_csv(b8, b1 = b9)
def fonk2(b13, b11, b12, b2 = 'accuracy', seed=7):
    b3 = []
    b4 = []
    for name, model in b13:
        b5 = KFold(n_splits=10, random_state=seed, shuffle=True)
        b6 = cross_val_score(model, b11, b12, cv=b5, b2=b2)
        b3.append(b6)
        b4.append(name)
        print(f"{name}: {b6.mean():.6f} ({b6.std():.6f})")
    return b3, b4
def fonk3(b3, b4):
    plt.figure()
    plt.title('Algorithm Comparison')
    plt.boxplot(b3)
    plt.xticks(range(1, len(b4) + 1), b4, b7 = 45, ha='right')
    plt.tight_layout()
    plt.show()
def fonk4():
    b8 = "https:
    b9 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    b10 = fonk1(b8, b9)
    b11 = b10.iloc[:, 0:8].values
    b12 = b10.iloc[:, 8].values
    b13 = [
        ('Logistic Regression', LogisticRegression(b14 = 'liblinear')),
        ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
        ('K-Nearest Neighbors', KNeighborsClassifier()),
        ('Decision Tree', DecisionTreeClassifier()),
        ('Naive Bayes', GaussianNB()),
        ('Support Vector Machine', SVC(b15 = 'auto'))
    ]
    b3, b4 = fonk2(b13, b11, b12)
    fonk3(b3, b4)
if b16 = = "__main__":
    fonk4()