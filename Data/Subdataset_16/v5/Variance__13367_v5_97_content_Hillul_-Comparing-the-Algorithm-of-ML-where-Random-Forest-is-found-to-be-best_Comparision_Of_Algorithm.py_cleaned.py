
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
def fonk1(url, column_names):
    return pd.read_csv(url, b1 = column_names)
def fonk2(b16, b14, b15, seed, b2 = 'accuracy'):
    b3 = []
    for name, model in b16:
        b4 = KFold(n_splits=10, random_state=seed, shuffle=True)
        b5 = cross_val_score(model, b14, b15, cv=b4, b2=b2)
        b3.append((name, b5))
        print(f"{name}: {b5.mean():.4f} ({b5.std():.4f})")
    return b3
def fonk3(b3):
    fig, b6 = plt.subplots()
    fig.suptitle('Algorithm Comparison')
    b7 = [name for name, _ in b3]
    b8 = [b5 for _, b5 in b3]
    b6.boxplot(b8)
    b6.set_xticklabels(b7, b9 = 45)
    plt.show()
if b10 = = "__main__":
    b11 = "https:
    b12 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    a1 = 7
    b13 = fonk1(b11, b12)
    b14 = b13.iloc[:, :-1].values
    b15 = b13.iloc[:, -1].values
    b16 = [
        ('Logistic Regression', LogisticRegression(b17 = 200)),
        ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
        ('K-Nearest Neighbors', KNeighborsClassifier()),
        ('Decision Tree', DecisionTreeClassifier()),
        ('Naive Bayes', GaussianNB()),
        ('Support Vector Machine', SVC())
    ]
    b3 = fonk2(b16, b14, b15, a1)
    fonk3(b3)