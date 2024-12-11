
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from google.colab import drive
drive.mount('/content/gdrive')
def fonk1(b12):
    return pd.read_csv(b12)
def fonk2(data):
    b1 = (2, 6.5, 8)
    b2 = ["bad", "good"]
    data["quality"] = pd.cut(data["quality"], b1 = b1, labels=b2)
    b3 = LabelEncoder()
    data["quality"] = b3.fit_transform(data["quality"])
    return data
def fonk3(data):
    plt.figure(b4 = (6, 4))
    sns.countplot(data["quality"])
    plt.title("Count of Wine Quality Categories")
    plt.xlabel("Quality")
    plt.ylabel("Count")
    plt.show()
def fonk4(data):
    b5 = data.drop("quality", axis=1)
    b6 = data["quality"]
    return b5, b6
def fonk5(X_train, X_test):
    b7 = StandardScaler()
    b8 = b7.fit_transform(X_train)
    b9 = b7.transform(X_test)
    return b8, b9
def fonk6(X_train, y_train):
    b10 = RandomForestClassifier(n_estimators=200)
    b10.fit(X_train, y_train)
    return b10
def fonk7(classifier, X_test, b14):
    b11 = classifier.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(b14, b11))
b12 = '/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv'
b13 = fonk1(b12)
b13 = fonk2(b13)
print("First few rows of the dataset:")
print(b13.head())
fonk3(b13)
b5, b6 = fonk4(b13)
X_train, X_test, y_train, b14 = train_test_split(b5, b6, test_size=0.2, random_state=42)
b8, b9 = fonk5(X_train, X_test)
b10 = fonk6(b8, y_train)
fonk7(b10, b9, b14)