import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from app.src.spam_classify import HAM_DATA, SPAM_DATA, load_email, TEST_DATA
from app.src.import_data import crawl_data
crawl_data()
crawl_data(test=True)
LIMIT = 2000
TEST_SIZE = 0.2
RANDOM_STATE = 42
ham_emails = [email for email in load_email(HAM_DATA, limit=LIMIT)]
spam_emails = [email for email in load_email(SPAM_DATA, limit=LIMIT)]
test_emails = [email for email in load_email(TEST_DATA)]
X = np.array(ham_emails + spam_emails)
y = np.array([0] * len(ham_emails) + [1] * len(spam_emails))
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
classifier = MultinomialNB(alpha=0.2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
X_test_emails = np.array(test_emails)
y_test_emails = np.array([1] * len(test_emails))
X_test_emails_vectorized = vectorizer.transform(X_test_emails)
test_result = classifier.predict(X_test_emails_vectorized)
test_accuracy = accuracy_score(y_test_emails, test_result)
print(f"Test Accuracy: {test_accuracy:.4f}")