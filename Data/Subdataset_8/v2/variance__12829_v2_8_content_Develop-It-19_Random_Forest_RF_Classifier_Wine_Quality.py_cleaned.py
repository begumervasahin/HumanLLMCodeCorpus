
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
wine = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv')
print("First few rows of the dataset:")
print(wine.head())
bins = (2, 6.5, 8)
group_names = ["bad", "good"]
wine["quality"] = pd.cut(wine["quality"], bins=bins, labels=group_names)
label_quality = LabelEncoder()
wine["quality"] = label_quality.fit_transform(wine["quality"])
print("\nCounts of each quality category:")
print(wine["quality"].value_counts())
plt.figure(figsize=(6, 4))
sns.countplot(wine["quality"])
plt.title("Count of Wine Quality Categories")
plt.xlabel("Quality")
plt.ylabel("Count")
plt.show()
X = wine.drop("quality", axis=1)
y = wine["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
rf_classifier = RandomForestClassifier(n_estimators=200)
rf_classifier.fit(X_train_scaled, y_train)
y_pred = rf_classifier.predict(X_test_scaled)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))