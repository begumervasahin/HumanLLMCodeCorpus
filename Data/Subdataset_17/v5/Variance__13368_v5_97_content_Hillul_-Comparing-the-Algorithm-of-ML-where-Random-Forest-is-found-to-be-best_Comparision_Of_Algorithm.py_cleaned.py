
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
def load_data(url, column_names):
    return pd.read_csv(url, names=column_names)
def evaluate_models(models, X, Y, seed, scoring='accuracy'):
    results = []
    for name, model in models:
        kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
        cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
        results.append((name, cv_results))
        print(f"{name}: {cv_results.mean():.4f} ({cv_results.std():.4f})")
    return results
def plot_results(results):
    fig, ax = plt.subplots()
    fig.suptitle('Algorithm Comparison')
    model_names = [name for name, _ in results]
    scores = [cv_results for _, cv_results in results]
    ax.boxplot(scores)
    ax.set_xticklabels(model_names, rotation=45)
    plt.show()
if __name__ == "__main__":
    DATA_URL = "https:
    COLUMN_NAMES = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    SEED = 7
    dataframe = load_data(DATA_URL, COLUMN_NAMES)
    X = dataframe.iloc[:, :-1].values
    Y = dataframe.iloc[:, -1].values
    models = [
        ('Logistic Regression', LogisticRegression(max_iter=200)),
        ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
        ('K-Nearest Neighbors', KNeighborsClassifier()),
        ('Decision Tree', DecisionTreeClassifier()),
        ('Naive Bayes', GaussianNB()),
        ('Support Vector Machine', SVC())
    ]
    results = evaluate_models(models, X, Y, SEED)
    plot_results(results)