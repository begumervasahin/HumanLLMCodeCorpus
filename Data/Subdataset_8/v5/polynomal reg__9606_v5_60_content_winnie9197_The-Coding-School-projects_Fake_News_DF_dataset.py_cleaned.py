import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
df = pd.read_csv("news.csv")
print("Dataset:")
print(df)
x_train, x_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.25, random_state=1)
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
tfidf_train = vectorizer.fit_transform(x_train)
tfidf_test = vectorizer.transform(x_test)
logistic_regression_model = LogisticRegression(max_iter=50)
logistic_regression_model.fit(tfidf_train, y_train)
predictions = logistic_regression_model.predict(tfidf_test)
accuracy = accuracy_score(y_test, predictions)
confusion_mat = confusion_matrix(y_test, predictions, labels=["FAKE", "REAL"])
print(f"Logistic Regression Accuracy Score: {round(accuracy * 100, 2)}%")
print("Logistic Regression Confusion Matrix:")
print(confusion_mat)
print("Classification Report:")
print(classification_report(y_test, predictions))