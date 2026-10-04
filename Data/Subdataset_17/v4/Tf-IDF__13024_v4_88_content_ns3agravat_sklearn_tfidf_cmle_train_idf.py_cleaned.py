import pickle
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
train_data = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_vectorizer = TfidfVectorizer(
    stop_words='english',
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'\w{2,}',
    ngram_range=(1, 1),
    max_features=30000
)
X_train_tfidf = tfidf_vectorizer.fit_transform(train_data.data)
text_classifier = MultinomialNB().fit(X_train_tfidf, train_data.target)
with open('text_classifier.pkl', 'wb') as clf_file:
    pickle.dump(text_classifier, clf_file)
with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(tfidf_vectorizer, vec_file)