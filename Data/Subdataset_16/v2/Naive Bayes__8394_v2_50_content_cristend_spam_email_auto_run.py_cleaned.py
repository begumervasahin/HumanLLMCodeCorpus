import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from app.src.spam_classify import HAM_DATA, SPAM_DATA, load_email, TEST_DATA
from app.src.import_data import crawl_data
crawl_data()
crawl_data(b1 = True)
a1 = 2000
b2 = [email for email in load_email(HAM_DATA, limit=a1)]
b3 = [email for email in load_email(SPAM_DATA, limit=a1)]
b4 = [email for email in load_email(TEST_DATA)]
b5 = np.array(b2 + b3)
b6 = np.array([0] * len(b2) + [1] * len(b3))
b7 = TfidfVectorizer(stop_words='english')
b8 = b7.fit_transform(b5)
X_train, X_test, Y_train, b9 = train_test_split(b8, b6, test_size=0.2, random_state=42)
b10 = MultinomialNB(alpha=0.2)
b10.fit(X_train, Y_train)
b11 = b10.predict(X_train)
b12 = b10.predict(X_test)
b13 = accuracy_score(Y_train, b11)
b14 = accuracy_score(b9, b12)
print(f"Training Accuracy: {b13:.4f}")
print(f"Test Accuracy: {b14:.4f}")
b15 = np.array(b4)
b16 = b7.transform(b15)
b17 = b10.predict(b16)
b18 = np.array([1] * len(b4))
b19 = accuracy_score(b18, b17)
print(f"Test Emails Accuracy: {b19:.4f}")