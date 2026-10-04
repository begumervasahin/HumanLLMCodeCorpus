
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
def evaluate_models(models, X, Y, scoring, seed):
    results = []
    model_names = []
    for name, model in models:
        kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
        cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
        results.append(cv_results)
        model_names.append(name)
        print(f"{name}: {cv_results.mean():.6f} ({cv_results.std():.6f})")
    return results, model_names
def plot_results(results, model_names):
    plt.figure()
    plt.title('Algorithm Comparison')
    plt.boxplot(results)
    plt.xticks(range(1, len(model_names) + 1), model_names, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
def main():
    url = "https:
    column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    dataframe = load_data(url, column_names)
    X = dataframe.iloc[:, 0:8].values
    Y = dataframe.iloc[:, 8].values
    seed = 7
    models = [
        ('Logistic Regression', LogisticRegression(solver='liblinear')),
        ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
        ('K-Nearest Neighbors', KNeighborsClassifier()),
        ('Decision Tree', DecisionTreeClassifier()),
        ('Naive Bayes', GaussianNB()),
        ('Support Vector Machine', SVC(gamma='auto'))
    ]
    results, model_names = evaluate_models(models, X, Y, scoring='accuracy', seed=seed)
    plot_results(results, model_names)
if __name__ == "__main__":
    main()