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
b1 = '/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv'
b2 = pd.read_csv(b1)
print(b2.head())
b3 = (2, 6.5, 8)
b4 = ["bad", "good"]
b2["quality"] = pd.cut(b2["quality"], b5 = b3, labels=b4)
b6 = LabelEncoder()
b2["quality"] = b6.fit_transform(b2["quality"])
print(b2["quality"].value_counts())
sns.countplot(b2["quality"])
b7 = b2.drop("quality", axis=1)
b8 = b2["quality"]
b11, b12, y_train, b9 = train_test_split(b7, b8, test_size=0.2, random_state=42)
b10 = StandardScaler()
b11 = b10.fit_transform(b11)
b12 = b10.transform(b12)
b13 = RandomForestClassifier(n_estimators=200)
b13.fit(b11, y_train)
b14 = b13.predict(b12)
print(classification_report(b9, b14))