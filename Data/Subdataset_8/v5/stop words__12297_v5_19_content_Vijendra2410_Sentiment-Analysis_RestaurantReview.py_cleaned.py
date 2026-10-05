import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
nltk.download('stopwords')
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
stop_words = set(nltk.corpus.stopwords.words('english'))
ps = nltk.stem.porter.PorterStemmer()
corpus = []
for review in dataset.iloc[:, 0]:
    review = re.sub('[^a-zA-Z]', ' ', review).lower().split()
    review = ' '.join([ps.stem(word) for word in review if word not in stop_words])
    corpus.append(review)
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = classifier.score(X_test, y_test)