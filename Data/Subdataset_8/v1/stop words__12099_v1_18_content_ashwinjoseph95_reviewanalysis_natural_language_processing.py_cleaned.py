import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
nltk.download('stopwords')
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = nltk.PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(nltk.corpus.stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)