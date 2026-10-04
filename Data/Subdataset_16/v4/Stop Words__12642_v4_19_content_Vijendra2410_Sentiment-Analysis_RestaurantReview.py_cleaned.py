
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.b2 import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
nltk.download('stopwords')
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
b2 = []
for i in range(0, 1000):
    b3 = re.sub('[^a-zA-Z]', ' ', b1.values[i, 0])
    b3 = b3.lower()
    b3 = b3.split()
    b4 = PorterStemmer()
    b3 = [b4.stem(word) for word in b3 if not word in set(stopwords.words('english'))]
    b3 = ' '.join(b3)
    b2.append(b3)
b5 = CountVectorizer(max_features=1500)
b6 = b5.fit_transform(b2).toarray()
b7 = b1.iloc[:, 1].values
X_train, X_test, y_train, b8 = train_test_split(b6, b7, test_size=0.15, random_state=0)
b9 = GaussianNB()
b9.fit(X_train, y_train)
b10 = b9.predict(X_test)
b11 = b9.score(X_test, b8)
print(f'Accuracy: {b11}')