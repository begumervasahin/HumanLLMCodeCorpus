
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
def load_data(train_path, test_path):
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    y_train = train_data.iloc[:, 0].values
    X_train = train_data.iloc[:, 4:].values
    y_test = test_data.iloc[:, 0].values
    X_test = test_data.iloc[:, 4:].values
    return X_train, y_train, X_test, y_test
def train_classifier(X_train, y_train):
    classifier = RandomForestClassifier(
        max_features='log2',
        n_estimators=100,
        criterion='entropy',
        random_state=0
    )
    classifier.fit(X_train, y_train)
    return classifier
def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)
    accuracy = accuracy_score(y_test, y_pred)
    print("\nAccuracy:", accuracy)
    f1 = f1_score(y_test, y_pred, average='macro')
    print("F1 Score:", f1)
def main():
    train_path = 'dota2Train.csv'
    test_path = 'dota2Test.csv'
    X_train, y_train, X_test, y_test = load_data(train_path, test_path)
    classifier = train_classifier(X_train, y_train)
    evaluate_classifier(classifier, X_test, y_test)
if __name__ == "__main__":
    main()