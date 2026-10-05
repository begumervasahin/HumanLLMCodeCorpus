import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def load_and_split_data(file_path, test_size=0.25, random_state=1):
    df = pd.read_csv(file_path)
    train_data, test_data = train_test_split(df, test_size=test_size, random_state=random_state)
    return train_data, test_data
def preprocess_text_data(train_data, test_data, text_column="text", label_column="label"):
    x_train, y_train = train_data[text_column], train_data[label_column]
    x_test, y_test = test_data[text_column], test_data[label_column]
    return x_train, y_train, x_test, y_test
def tfidf_vectorization(x_train, x_test, max_df=0.7):
    vectorizer = TfidfVectorizer(stop_words="english", max_df=max_df)
    tfidf_train = vectorizer.fit_transform(x_train)
    tfidf_test = vectorizer.transform(x_test)
    return tfidf_train, tfidf_test
def train_logistic_regression(tfidf_train, y_train, max_iter=50):
    logistic_regression = LogisticRegression(max_iter=max_iter)
    logistic_regression.fit(tfidf_train, y_train)
    return logistic_regression
def evaluate_model(y_test, predictions):
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy Score: {round(accuracy * 100, 2)}%")
    confusion_matrix_result = confusion_matrix(y_test, predictions, labels=["FAKE", "REAL"])
    print("Confusion Matrix:")
    print(confusion_matrix_result)
    classification_report_result = classification_report(y_test, predictions)
    print("Classification Report:")
    print(classification_report_result)
def main():
    train_data, test_data = load_and_split_data("news.csv")
    x_train, y_train, x_test, y_test = preprocess_text_data(train_data, test_data)
    tfidf_train, tfidf_test = tfidf_vectorization(x_train, x_test)
    logistic_regression_model = train_logistic_regression(tfidf_train, y_train)
    predictions = logistic_regression_model.predict(tfidf_test)
    evaluate_model(y_test, predictions)
if __name__ == "__main__":
    main()