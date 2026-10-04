import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.b4 import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
nltk.download('stopwords')
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
def fonk1(b2):
    b2 = re.sub('[^a-zA-Z]', ' ', b2)
    b2 = b2.lower().split()
    b3 = PorterStemmer()
    b2 = [b3.stem(word) for word in b2 if word not in set(stopwords.words('english'))]
    return ' '.join(b2)
b4 = [fonk1(b1['Review'][i]) for i in range(0, 1000)]
b5 = CountVectorizer(max_features=1500)
b6 = b5.fit_transform(b4).toarray()
b7 = b1.iloc[:, 1].values
X_train, X_test, y_train, b8 = train_test_split(b6, b7, test_size=0.20, random_state=0)
b9 = GaussianNB()
b9.fit(X_train, y_train)
b10 = b9.predict(X_test)
b11 = confusion_matrix(b8, b10)
print("Confusion Matrix:")
print(b11)