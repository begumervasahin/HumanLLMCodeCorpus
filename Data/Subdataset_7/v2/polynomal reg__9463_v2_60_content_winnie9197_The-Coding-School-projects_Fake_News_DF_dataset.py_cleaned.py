
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
b1 = pd.read_csv("news.csv")
train_data, b2 = train_test_split(b1, test_size=0.25, random_state=1)
x_train, b3 = train_data["text"], train_data["label"]
x_test, b4 = b2["text"], b2["label"]
b5 = TfidfVectorizer(stop_words="english", max_df=0.7)
b6 = b5.fit_transform(x_train)
b7 = b5.transform(x_test)
b8 = LogisticRegression(max_iter=50)
b8.fit(b6, b3)
b9 = b8.predict(b7)
b10 = accuracy_score(b4, b9)
print(f"Logistic Regression Accuracy Score: {round(b10 * 100, 2)}%")
b11 = confusion_matrix(b4, b9, labels=["FAKE", "REAL"])
print("Logistic Regression Confusion Matrix:")
print(b11)
b12 = classification_report(b4, b9)
print("Classification Report:")
print(b12)