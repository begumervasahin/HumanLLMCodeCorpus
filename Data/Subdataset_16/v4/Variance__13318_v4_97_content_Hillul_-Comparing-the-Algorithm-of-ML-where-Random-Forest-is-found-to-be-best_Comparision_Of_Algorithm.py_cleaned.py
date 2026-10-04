
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
    ('Logistic Regression', LogisticRegression()),
    ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Decision Tree', DecisionTreeClassifier()),
    ('Naive Bayes', GaussianNB()),
    ('Support Vector Machine', SVC())
]
b7 = []
b8 = []
b9 = 'accuracy'
for name, model in b6:
    b10 = KFold(n_splits=10, random_state=a1, shuffle=True)
    b11 = cross_val_score(model, b4, b5, cv=b10, b9=b9)
    b7.append(b11)
    b8.append(name)
    print(f"{name}: {b11.mean():.4f} ({b11.std():.4f})")
plt.figure()
plt.title('Algorithm Comparison')
plt.boxplot(b7)
plt.xticks(b12 = range(1, len(b8) + 1), labels=b8, rotation=45)
plt.show()