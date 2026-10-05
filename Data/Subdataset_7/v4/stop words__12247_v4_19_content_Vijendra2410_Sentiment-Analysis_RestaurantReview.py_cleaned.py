
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
nltk.download('stopwords')
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
b2 = set(stopwords.words('english'))
b3 = PorterStemmer()
b4 = []
for i in range(0, 1000):
    b5 = re.sub('[^a-zA-z]', ' ', b1.values[i, 0])
    b5 = b5.lower()
    b5 = b5.split()
    b5 = [b3.stem(word) for word in b5 if word not in b2]
    b5 = ' '.join(b5)
    b4.append(b5)
b6 = CountVectorizer(max_features=1500)
b7 = b6.fit_transform(b4).toarray()
b8 = b1.iloc[:, 1].values
X_train, X_test, y_train, b9 = train_test_split(b7, b8, test_size=0.15, random_state=0)
b10 = GaussianNB()
b10.fit(X_train, y_train)
b11 = b10.predict(X_test)
b12 = b10.score(X_test, b9)