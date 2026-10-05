import pandas
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
b1 = pandas.read_csv("news.csv")
print(b1)
x_train, x_test, y_train, b2 = train_test_split(b1["text"], b1["label"], test_size=0.25, random_state=1)
b3 = TfidfVectorizer(stop_words="english", max_df=0.7)
b4 = b3.fit_transform(x_train)
b5 = b3.transform(x_test)
b6 = LogisticRegression(max_iter=50)
b6.fit(b4, y_train)
b7 = []
b8 = b6.predict(b5)
b9 = accuracy_score(b2, b8)
print(f"Logistic Regression Accuracy Score: {round(b9*100,2)}%")
b10 = confusion_matrix(b2, b8, labels=["FAKE","REAL"])
print("Logistic Regression Confusion Matrix:")
print(b10)
print(classification_report(b2, b8))