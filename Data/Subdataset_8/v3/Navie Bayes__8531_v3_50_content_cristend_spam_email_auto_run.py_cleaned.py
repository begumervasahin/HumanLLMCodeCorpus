import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from app.src.spam_classify import HAM_DATA, SPAM_DATA, load_email, TEST_DATA
from app.src.import_data import crawl_data
def load_data(limit=None, test=False):
    if test:
        data = [email for email in load_email(TEST_DATA, limit=limit)]
    else:
        ham_emails = [email for email in load_email(HAM_DATA, limit=limit)]
        spam_emails = [email for email in load_email(SPAM_DATA, limit=limit)]
        data = ham_emails + spam_emails
    return data
def main():
    crawl_data()
    crawl_data(test=True)
    LIMIT = 2000
    vectorizer = TfidfVectorizer(stop_words='english')
    emails = load_data(limit=LIMIT)
    labels = np.array([0] * len(ham_emails) + [1] * len(spam_emails))
    X_prepared = vectorizer.fit_transform(emails)
    X_train, X_test, Y_train, Y_test = train_test_split(
        X_prepared, labels, test_size=0.2, random_state=42)
    mnb = MultinomialNB(alpha=0.2)
    mnb.fit(X_train, Y_train)
    predictions = mnb.predict(X_test)
    accuracy = accuracy_score(Y_test, predictions)
    print("Accuracy Score:", accuracy)
if __name__ == "__main__":
    main()