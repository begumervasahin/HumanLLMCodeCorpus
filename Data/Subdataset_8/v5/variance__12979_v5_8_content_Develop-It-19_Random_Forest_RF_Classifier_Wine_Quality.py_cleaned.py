import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
%matplotlib inline
from google.colab import drive
drive.mount('/content/gdrive')
dataset_path = '/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv'
wine = pd.read_csv(dataset_path)
print(wine.head())
quality_bins = (2, 6.5, 8)
quality_labels = ["bad", "good"]
wine["quality"] = pd.cut(wine["quality"], bins=quality_bins, labels=quality_labels)
label_quality = LabelEncoder()
wine["quality"] = label_quality.fit_transform(wine["quality"])
print(wine["quality"].value_counts())
sns.countplot(wine["quality"])
X = wine.drop("quality", axis=1)
y = wine["quality"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
predictions = rfc.predict(X_test)
print(classification_report(y_test, predictions))