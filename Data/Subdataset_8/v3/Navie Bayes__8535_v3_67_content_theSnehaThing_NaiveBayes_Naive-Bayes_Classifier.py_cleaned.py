import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    X = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, 4].values
    return X, y
def split_dataset(X, y, test_size=0.25, random_state=0):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled
def train_classifier(X_train, y_train):
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    return classifier
def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    return cm
def plot_classification_result(X_set, y_set, classifier, title):
    X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                         np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
    plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    for i, j in enumerate(np.unique(y_set)):
        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                    c=ListedColormap(('red', 'green'))(i), label=j)
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.legend()
    plt.show()
def main():
    X, y = load_dataset('Social_Network_Ads.csv')
    X_train, X_test, y_train, y_test = split_dataset(X, y)
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    classifier = train_classifier(X_train_scaled, y_train)
    cm = evaluate_classifier(classifier, X_test_scaled, y_test)
    plot_classification_result(X_train_scaled, y_train, classifier, 'Naive Bayes Classifier (Training set)')
    plot_classification_result(X_test_scaled, y_test, classifier, 'Naive Bayes Classifier (Test set)')
if __name__ == "__main__":
    main()