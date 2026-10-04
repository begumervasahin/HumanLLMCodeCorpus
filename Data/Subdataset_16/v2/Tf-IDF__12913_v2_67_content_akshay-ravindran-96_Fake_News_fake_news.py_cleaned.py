import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
b1 = 'C:\\Users\\Akshay\\Desktop\\machine_Learning\\Fake_News\\news.csv'
b2 = pd.read_csv(b1)
print("First 10 rows of the dataset:")
print(b2.head(10))
b3 = b2['label']
x_train, x_test, y_train, b4 = train_test_split(b2['text'], b3, test_size=0.2, random_state=7)
b5 = TfidfVectorizer(stop_words='english', max_df=0.7)
b6 = b5.fit_transform(x_train)
b7 = b5.transform(x_test)
b8 = PassiveAggressiveClassifier(max_iter=50)
b8.fit(b6, y_train)
b9 = b8.predict(b7)
b10 = accuracy_score(b4, b9)
print(f'Accuracy: {round(b10 * 100, 2)}%')
b11 = confusion_matrix(b4, b9, b3=['FAKE', 'REAL'])
print("Confusion Matrix:")
print(b11)