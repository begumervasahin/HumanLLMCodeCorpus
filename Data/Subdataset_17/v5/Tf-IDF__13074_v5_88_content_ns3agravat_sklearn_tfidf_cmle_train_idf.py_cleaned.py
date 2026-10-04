import pickle
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
def fetch_training_data():
    return fetch_20newsgroups(subset='train', shuffle=True)
def initialize_tfidf_vectorizer():
    return TfidfVectorizer(
        stop_words='english',
        sublinear_tf=True,
        strip_accents='unicode',
        analyzer='word',
        token_pattern=r'\w{2,}',
        ngram_range=(1, 1),
        max_features=30000
    )
def train_text_classifier(X_train, y_train):
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)
    return classifier
def save_model_and_vectorizer(classifier, vectorizer):
    with open('text_classifier.pkl', 'wb') as clf_file:
        pickle.dump(classifier, clf_file)
    with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
def main():
    train_data = fetch_training_data()
    tfidf_vectorizer = initialize_tfidf_vectorizer()
    X_train_tfidf = tfidf_vectorizer.fit_transform(train_data.data)
    text_classifier = train_text_classifier(X_train_tfidf, train_data.target)
    save_model_and_vectorizer(text_classifier, tfidf_vectorizer)
if __name__ == "__main__":
    main()