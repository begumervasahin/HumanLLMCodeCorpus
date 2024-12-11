
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
b1 = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv')
print("First few rows of the dataset:")
print(b1.head())
b2 = (2, 6.5, 8)
b3 = ["bad", "good"]
b1["quality"] = pd.cut(b1["quality"], b2 = b2, labels=b3)
b4 = LabelEncoder()
b1["quality"] = b4.fit_transform(b1["quality"])
print("\nCounts of each quality category:")
print(b1["quality"].value_counts())
plt.figure(b5 = (6, 4))
sns.countplot(b1["quality"])
plt.title("Count of Wine Quality Categories")
plt.xlabel("Quality")
plt.ylabel("Count")
plt.show()
b6 = b1.drop("quality", axis=1)
b7 = b1["quality"]
X_train, X_test, y_train, b8 = train_test_split(b6, b7, test_size=0.2, random_state=42)
b9 = StandardScaler()
b10 = b9.fit_transform(X_train)
b11 = b9.transform(X_test)
b12 = RandomForestClassifier(n_estimators=200)
b12.fit(b10, y_train)
b13 = b12.predict(b11)
print("\nClassification Report:")
print(classification_report(b8, b13))