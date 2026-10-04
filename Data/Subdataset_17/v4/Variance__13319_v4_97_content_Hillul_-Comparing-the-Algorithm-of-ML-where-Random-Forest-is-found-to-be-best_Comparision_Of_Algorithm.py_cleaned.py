
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
url = "https:
column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=column_names)
X = dataframe.iloc[:, 0:8].values
Y = dataframe.iloc[:, 8].values
seed = 7
models = [
    ('Logistic Regression', LogisticRegression()),
    ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
    ('K-Nearest Neighbors', KNeighborsClassifier()),
    ('Decision Tree', DecisionTreeClassifier()),
    ('Naive Bayes', GaussianNB()),
    ('Support Vector Machine', SVC())
]
results = []
model_names = []
scoring = 'accuracy'
for name, model in models:
    kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    model_names.append(name)
    print(f"{name}: {cv_results.mean():.4f} ({cv_results.std():.4f})")
plt.figure()
plt.title('Algorithm Comparison')
plt.boxplot(results)
plt.xticks(ticks=range(1, len(model_names) + 1), labels=model_names, rotation=45)
plt.show()