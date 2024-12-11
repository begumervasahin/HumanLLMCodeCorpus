import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def fonk1(file_path, b1 = 0.25, random_state=1):
    b2 = pd.read_csv(file_path)
    train_data, b3 = train_test_split(b2, b1=b1, random_state=random_state)
    return train_data, b3
def fonk2(train_data, b3, b4 = "text", label_column="label"):
    x_train, b5 = train_data[b4], train_data[label_column]
    x_test, b6 = b3[b4], b3[label_column]
    return x_train, b5, x_test, b6
def fonk3(x_train, x_test, b7 = 0.7):
    b8 = TfidfVectorizer(stop_words="english", b7=b7)
    b9 = b8.fit_transform(x_train)
    b10 = b8.transform(x_test)
    return b9, b10
def fonk4(b9, b5, b11 = 50):
    b12 = LogisticRegression(b11=b11)
    b12.fit(b9, b5)
    return b12
def fonk5(b6, b17):
    b13 = accuracy_score(b6, b17)
    print(f"Accuracy Score: {round(b13 * 100, 2)}%")
    b14 = confusion_matrix(b6, b17, labels=["FAKE", "REAL"])
    print("Confusion Matrix:")
    print(b14)
    b15 = classification_report(b6, b17)
    print("Classification Report:")
    print(b15)
def fonk6():
    train_data, b3 = fonk1("news.csv")
    x_train, b5, x_test, b6 = fonk2(train_data, b3)
    b9, b10 = fonk3(x_train, x_test)
    b16 = fonk4(b9, b5)
    b17 = b16.predict(b10)
    fonk5(b6, b17)
if b18 = = "__main__":
    fonk6()