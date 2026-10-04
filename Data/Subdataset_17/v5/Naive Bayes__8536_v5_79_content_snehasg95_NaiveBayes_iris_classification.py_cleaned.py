
import pandas as pd
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def load_and_prepare_data():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=0)
    return X_train, X_test, y_train, y_test
def train_and_evaluate(X_train, X_test, y_train, y_test):
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    return accuracy_score(y_test, y_predict)
def main():
    X_train, X_test, y_train, y_test = load_and_prepare_data()
    score = train_and_evaluate(X_train, X_test, y_train, y_test)
    print(f"Accuracy score: {score:.2f}")
if __name__ == "__main__":
    main()