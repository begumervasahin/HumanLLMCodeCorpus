
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
reviews_dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
corpus = []
for i in range(len(reviews_dataset)):
    review_text = reviews_dataset['Review'][i]
    review_text = re.sub('[^a-zA-Z]', ' ', review_text)
    review_text = review_text.lower()
    words = review_text.split()
    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in words if word not in set(stopwords.words('english'))]
    preprocessed_review = ' '.join(stemmed_words)
    corpus.append(preprocessed_review)
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = reviews_dataset['Liked'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")
