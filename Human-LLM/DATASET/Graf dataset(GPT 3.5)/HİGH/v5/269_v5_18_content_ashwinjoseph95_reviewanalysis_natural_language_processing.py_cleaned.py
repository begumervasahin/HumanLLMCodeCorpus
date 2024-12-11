
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
nltk.download('stopwords')
def fonk1(b1):
    b1 = re.sub('[^a-zA-Z]', ' ', b1).lower()
    b1 = b1.split()
    b2 = PorterStemmer()
    b1 = [b2.stem(word) for word in b1 if word not in set(stopwords.words('english'))]
    return ' '.join(b1)
b3 = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
b3['Review'] = b3['Review'].apply(preprocess_review)
b4 = CountVectorizer(max_features=1500).fit_transform(b3['Review']).toarray()
b5 = b3['Liked'].values
X_train, X_test, y_train, b6 = train_test_split(b4, b5, test_size=0.20, random_state=0)
b7 = GaussianNB()
b7.fit(X_train, y_train)
b8 = b7.predict(X_test)
b9 = confusion_matrix(b6, b8)