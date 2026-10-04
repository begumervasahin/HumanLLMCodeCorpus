
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
nltk.download('stopwords')
def preprocess_reviews(dataset):
    corpus = []
    ps = PorterStemmer()
    for i in range(len(dataset)):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower().split()
        review = [ps.stem(word) for word in review if word not in stopwords.words('english')]
        corpus.append(' '.join(review))
    return corpus
def main():
    dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
    corpus = preprocess_reviews(dataset)
    cv = CountVectorizer(max_features=1500)
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, 1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = clf.score(X_test, y_test)
    print(f'Accuracy: {accuracy:.2f}')
if __name__ == "__main__":
    main()