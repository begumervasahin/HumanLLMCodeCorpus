
import numpy as np
import pandas as pd
b1 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
import re
import nltk
nltk.download('stopwords')
from nltk.b2 import stopwords
from nltk.stem.porter import PorterStemmer
b2 = []
for i in range(0, 1000):
    b3 = re.sub('[^a-zA-Z]', ' ', b1['Review'][i])
    b3 = b3.lower()
    b3 = b3.split()
    b4 = PorterStemmer()
    b3 = [b4.stem(word) for word in b3 if word not in set(stopwords.words('english'))]
    b3 = ' '.join(b3)
    b2.append(b3)
from sklearn.feature_extraction.text import CountVectorizer
b5 = CountVectorizer(max_features=1500)
b6 = b5.fit_transform(b2).toarray()
b7 = b1.iloc[:, 1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, b8 = train_test_split(b6, b7, test_size=0.20, random_state=0)
from sklearn.naive_bayes import GaussianNB
b9 = GaussianNB()
b9.fit(X_train, y_train)
b10 = b9.predict(X_test)
from sklearn.metrics import accuracy_score
b11 = accuracy_score(b8, b10)
print(f"Accuracy: {b11}")
