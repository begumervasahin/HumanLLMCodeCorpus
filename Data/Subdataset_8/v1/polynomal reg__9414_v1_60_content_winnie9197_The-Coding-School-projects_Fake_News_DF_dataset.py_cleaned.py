import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
df = pd.read_csv("news.csv")
x_train, x_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.25, random_state=1)
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
tfidf_train = vectorizer.fit_transform(x_train)
tfidf_test = vectorizer.transform(x_test)
logit = LogisticRegression(max_iter=50)
logit.fit(tfidf_train, y_train)
logit_y_pred = logit.predict(tfidf_test)
logit_score = accuracy_score(y_test, logit_y_pred)
print(f"Logistic Regression Accuracy Score: {round(logit_score*100, 2)}%")
logit_cf = confusion_matrix(y_test, logit_y_pred, labels=["FAKE", "REAL"])
print("Logistic Regression Confusion Matrix:")
print(logit_cf)
print("Classification Report:")
print(classification_report(y_test, logit_y_pred))