
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
def fonk1(b7, b8):
    return pd.read_csv(b7, b1 = b8)
def fonk2(b12, b10, b11, scoring, a1):
    b2 = []
    b3 = []
    for name, model in b12:
        b4 = KFold(n_splits=10, random_state=a1, shuffle=True)
        b5 = cross_val_score(model, b10, b11, cv=b4, scoring=scoring)
        b2.append(b5)
        b3.append(name)
        print(f"{name}: {b5.mean():.6f} ({b5.std():.6f})")
    return b2, b3
def fonk3(b2, b3):
    plt.figure()
    plt.title('Algorithm Comparison')
    plt.boxplot(b2)
    plt.xticks(range(1, len(b3) + 1), b3, b6 = 45, ha='right')
    plt.tight_layout()
    plt.show()
def fonk4():
    b7 = "https:
    b8 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    b9 = fonk1(b7, b8)
    b10 = b9.iloc[:, 0:8].values
    b11 = b9.iloc[:, 8].values
    a1 = 7
    b12 = [
        ('Logistic Regression', LogisticRegression(b13 = 'liblinear')),
        ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
        ('K-Nearest Neighbors', KNeighborsClassifier()),
        ('Decision Tree', DecisionTreeClassifier()),
        ('Naive Bayes', GaussianNB()),
        ('Support Vector Machine', SVC(b14 = 'auto'))
    ]
    b2, b3 = fonk2(b12, b10, b11, scoring='accuracy', a1=a1)
    fonk3(b2, b3)
if b15 = = "__main__":
    fonk4()