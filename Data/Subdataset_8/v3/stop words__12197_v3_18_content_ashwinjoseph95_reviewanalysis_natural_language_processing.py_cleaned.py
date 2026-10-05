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
reviews_dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
def clean_and_stem_text(text):
    cleaned_text = re.sub('[^a-zA-Z]', ' ', text)
    cleaned_text = cleaned_text.lower()
    words = cleaned_text.split()
    stemmer = nltk.PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words if word not in set(nltk.corpus.stopwords.words('english'))]
    cleaned_review = ' '.join(stemmed_words)
    return cleaned_review
corpus = [clean_and_stem_text(review) for review in reviews_dataset['Review']]
vectorizer = CountVectorizer(max_features=1500)
X_features = vectorizer.fit_transform(corpus).toarray()
y_labels = reviews_dataset['Liked'].values
X_train, X_test, y_train, y_test = train_test_split(X_features, y_labels, test_size=0.20, random_state=0)
naive_bayes_classifier = GaussianNB()
naive_bayes_classifier.fit(X_train, y_train)
predicted_labels = naive_bayes_classifier.predict(X_test)
confusion_matrix_result = confusion_matrix(y_test, predicted_labels)
print("Confusion Matrix:")
print(confusion_matrix_result)