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
def fonk1(text):
    b2 = re.sub('[^a-zA-Z]', ' ', text)
    b2 = b2.lower()
    b3 = b2.split()
    b4 = nltk.PorterStemmer()
    b5 = [b4.stem(word) for word in b3 if word not in set(nltk.b7.stopwords.b3('english'))]
    b6 = ' '.join(b5)
    return b6
b7 = [fonk1(review) for review in b1['Review']]
b8 = CountVectorizer(max_features=1500)
b9 = b8.fit_transform(b7).toarray()
b10 = b1['Liked'].values
X_train, X_test, y_train, b11 = train_test_split(b9, b10, test_size=0.20, random_state=0)
b12 = GaussianNB()
b12.fit(X_train, y_train)
b13 = b12.predict(X_test)
b14 = confusion_matrix(b11, b13)
print("Confusion Matrix:")
print(b14)