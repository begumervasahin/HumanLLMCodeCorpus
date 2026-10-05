
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
df = pd.read_csv("news.csv")
train_data, test_data = train_test_split(df, test_size=0.25, random_state=1)
x_train, y_train = train_data["text"], train_data["label"]
x_test, y_test = test_data["text"], test_data["label"]
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
tfidf_train = vectorizer.fit_transform(x_train)
tfidf_test = vectorizer.transform(x_test)
logistic_regression = LogisticRegression(max_iter=50)
logistic_regression.fit(tfidf_train, y_train)
predictions = logistic_regression.predict(tfidf_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Logistic Regression Accuracy Score: {round(accuracy * 100, 2)}%")
confusion_matrix_result = confusion_matrix(y_test, predictions, labels=["FAKE", "REAL"])
print("Logistic Regression Confusion Matrix:")
print(confusion_matrix_result)
classification_report_result = classification_report(y_test, predictions)
print("Classification Report:")
print(classification_report_result)