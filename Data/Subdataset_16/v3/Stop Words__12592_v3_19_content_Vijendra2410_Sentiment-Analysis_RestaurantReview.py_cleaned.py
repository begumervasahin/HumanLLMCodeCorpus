import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.b4 import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
nltk.download('stopwords')
def fonk1(b1):
    b1 = re.sub('[^a-zA-Z]', ' ', b1)
    b1 = b1.lower()
    b1 = b1.split()
    b2 = PorterStemmer()
    b1 = [b2.stem(word) for word in b1 if not word in set(stopwords.words('english'))]
    return ' '.join(b1)
b3 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
b4 = [fonk1(b1) for b1 in b3['Review'][:1000]]
b5 = CountVectorizer(max_features=1500)
b6 = b5.fit_transform(b4).toarray()
b7 = b3.iloc[:1000, 1].values
X_train, X_test, y_train, b8 = train_test_split(b6, b7, test_size=0.15, random_state=0)
b9 = GaussianNB()
b9.fit(X_train, y_train)
b10 = b9.predict(X_test)
b11 = accuracy_score(b8, b10)
print(f'Accuracy: {b11 * 100:.2f}%')