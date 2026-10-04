import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
b1 = pd.read_csv('C:\\Users\\Akshay\\Desktop\\machine_Learning\\Fake_News\\news.csv')
b1.shape
print(b1.head(10))
b2 = b1.label
b2.head()
x_train,x_test,y_train,b3 = train_test_split(b1['text'], b2, test_size=0.2, random_state=7)
b4 = TfidfVectorizer(stop_words='english', max_df=0.7)
b5 = b4.fit_transform(x_train)
b6 = b4.transform(x_test)
b7 = PassiveAggressiveClassifier(max_iter=50)
b7.fit(b5,y_train)
b8 = b7.predict(b6)
b9 = accuracy_score(b3,b8)
print(f'Accuracy: {round(b9*100,2)}%')
confusion_matrix(b3,b8, b2 = ['FAKE','REAL'])