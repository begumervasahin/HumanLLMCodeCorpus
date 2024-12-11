import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
nltk.download('stopwords')
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
b2 = []
for index in range(0, 1000):
    b3 = re.sub('[^a-zA-Z]', ' ', b1['Review'][index])
    b3 = b3.lower()
    b4 = b3.split()
    b5 = nltk.PorterStemmer()
    b6 = [b5.stem(word) for word in b4 if word not in set(nltk.b2.stopwords.b4('english'))]
    b7 = ' '.join(b6)
    b2.append(b7)
b8 = CountVectorizer(max_features=1500)
b9 = b8.fit_transform(b2).toarray()
b10 = b1.iloc[:, 1].values
X_train, X_test, y_train, b11 = train_test_split(b9, b10, test_size=0.20, random_state=0)
b12 = GaussianNB()
b12.fit(X_train, y_train)
b13 = b12.predict(X_test)
b14 = confusion_matrix(b11, b13)
print("Confusion Matrix:")
print(b14)