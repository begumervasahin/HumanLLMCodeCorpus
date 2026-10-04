
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
b1 = "https:
b2 = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
b3 = pd.read_csv(b1, names=b2)
b4 = b3.iloc[:, 0:8].values
b5 = b3.iloc[:, 8].values
a1 = 7
b6 = [
    ('Logistic Regression', LogisticRegression(b7 = 'liblinear')),
    ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Decision Tree', DecisionTreeClassifier()),
    ('Naive Bayes', GaussianNB()),
    ('Support Vector Machine', SVC(b8 = 'auto'))
]
b9 = []
b10 = []
b11 = 'accuracy'
for name, model in b6:
    b12 = KFold(n_splits=10, random_state=a1, shuffle=True)
    b13 = cross_val_score(model, b4, b5, cv=b12, b11=b11)
    b9.append(b13)
    b10.append(name)
    print(f"{name}: {b13.mean():.6f} ({b13.std():.6f})")
plt.figure()
plt.title('Algorithm Comparison')
plt.boxplot(b9)
plt.xticks(range(1, len(b10) + 1), b10, b14 = 45, ha='right')
plt.tight_layout()
plt.show()