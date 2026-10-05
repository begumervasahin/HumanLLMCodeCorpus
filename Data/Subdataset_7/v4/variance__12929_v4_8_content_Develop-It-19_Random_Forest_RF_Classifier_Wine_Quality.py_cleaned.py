import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
%matplotlib inline
import os
from google.colab import drive
drive.mount('/content/gdrive')
b1 = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv')
!cat /content/gdrive/My Drive/Colab Notebooks/RedWine/winequality-red.csv
!pip install fastai
b2 = (2, 6.5, 8)
b3 = ["bad", "good"]
b1["quality"] = pd.cut(b1["quality"], b2 = b2, labels=b3)
b4 = LabelEncoder()
b1["quality"] = b4.fit_transform(b1["quality"])
b1["quality"].value_counts()
sns.countplot(b1["quality"])
b5 = b1.drop("quality", axis=1)
b6 = b1["quality"]
b9, b10, y_train, b7 = train_test_split(b5, b6, test_size=0.2, random_state=42)
b8 = StandardScaler()
b9 = b8.fit_transform(b9)
b10 = b8.transform(b10)
b11 = RandomForestClassifier(n_estimators=200)
b11.fit(b9, y_train)
b12 = b11.predict(b10)
print(classification_report(b7, b12))