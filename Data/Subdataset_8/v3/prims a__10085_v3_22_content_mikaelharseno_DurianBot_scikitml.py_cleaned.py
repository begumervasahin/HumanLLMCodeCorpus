import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def load_data(file_path):
    data = pd.read_csv(file_path, sep=" ", header=None)
    data.columns = ['worst_case_prob', 'scout_report', 'actual_value']
    return data
def train_logistic_regression(X_train, Y_train):
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    return model
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
def load_model(filename):
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model
def evaluate_model(model, X_test, Y_test):
    accuracy = model.score(X_test, Y_test)
    return accuracy
def main():
    file_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_directory, 'results.txt')
    data = load_data(file_path)
    features, target = data.iloc[:, :2], data.iloc[:, 2]
    test_size = 0.2
    X_train, X_test, Y_train, Y_test = train_test_split(features, target, test_size=test_size)
    model = train_logistic_regression(X_train, Y_train)
    predicted_probabilities = model.predict_proba(X_test)
    print("Predicted Probabilities:", predicted_probabilities)
    accuracy = evaluate_model(model, X_test, Y_test)
    print("Model Accuracy:", accuracy)
    model_filename = 'finalized_model.sav'
    save_model(model, model_filename)
    loaded_model = load_model(model_filename)
    loaded_model_accuracy = evaluate_model(loaded_model, X_test, Y_test)
    print("Loaded Model Accuracy:", loaded_model_accuracy)
if __name__ == "__main__":
    main()