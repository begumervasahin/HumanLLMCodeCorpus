import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from app.src.spam_classify import (
    HAM_DATA, SPAM_DATA, load_email, TEST_DATA)
from app.src.import_data import crawl_data
crawl_data()
crawl_data(b1 = True)
a1 = 2000
b2 = TfidfVectorizer('english')
b3 = [email for email in load_email(HAM_DATA, limit=a1)]
b4 = [email for email in load_email(SPAM_DATA, limit=a1)]
b5 = [email for email in load_email(TEST_DATA)]
b6 = np.array(b3+b4)
b7 = np.array([0]*len(b3)+[1]*len(b4))
b8 = b2.fit_transform(b6)
X_train, X_test, Y_train, b9 = train_test_split(
    b8, b7, b10 = 0.2, random_state=42)
b11 = MultinomialNB(alpha=.2)
b11.fit(X_train, Y_train)
b12 = np.array(b5)
b13 = np.array([1]*len(b5))
b14 = b2.transform(b6)
b15 = b11.predict(b8)
b16 = accuracy_score(b7, b15)
print(b16)