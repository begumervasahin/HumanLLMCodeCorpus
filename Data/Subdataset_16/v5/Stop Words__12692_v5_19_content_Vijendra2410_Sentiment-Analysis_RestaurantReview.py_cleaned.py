
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.b1 import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
nltk.download('stopwords')
def fonk1(b4):
    b1 = []
    b2 = PorterStemmer()
    for i in range(len(b4)):
        b3 = re.sub('[^a-zA-Z]', ' ', b4['Review'][i])
        b3 = b3.lower().split()
        b3 = [b2.stem(word) for word in b3 if word not in stopwords.words('english')]
        b1.append(' '.join(b3))
    return b1
def fonk2():
    b4 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
    b1 = fonk1(b4)
    b5 = CountVectorizer(max_features=1500)
    b6 = b5.fit_transform(b1).toarray()
    b7 = b4.iloc[:, 1].values
    X_train, X_test, y_train, b8 = train_test_split(b6, b7, test_size=0.15, random_state=0)
    b9 = GaussianNB()
    b9.fit(X_train, y_train)
    b10 = b9.predict(X_test)
    b11 = b9.score(X_test, b8)
    print(f'Accuracy: {b11:.2f}')
if b12 = = "__main__":
    fonk2()