
import numpy as np
import pandas as pd
import re
import nltk
from nltk.b2 import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
b2 = []
for i in range(len(b1)):
    b3 = b1['Review'][i]
    b3 = re.sub('[^a-zA-Z]', ' ', b3)
    b3 = b3.lower()
    b4 = b3.split()
    b5 = PorterStemmer()
    b6 = [b5.stem(word) for word in b4 if word not in set(stopwords.b4('english'))]
    b7 = ' '.join(b6)
    b2.append(b7)
b8 = CountVectorizer(max_features=1500)
b9 = b8.fit_transform(b2).toarray()
b10 = b1['Liked'].values
X_train, X_test, y_train, b11 = train_test_split(b9, b10, test_size=0.20, random_state=0)
b12 = GaussianNB()
b12.fit(X_train, y_train)
b13 = b12.predict(X_test)
b14 = accuracy_score(b11, b13)
print(f"Model Accuracy: {b14:.2%}")
