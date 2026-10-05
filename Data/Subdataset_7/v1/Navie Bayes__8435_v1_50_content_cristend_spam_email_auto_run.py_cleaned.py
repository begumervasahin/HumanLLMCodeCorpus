import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from app.src.spam_classify import HAM_DATA, SPAM_DATA, load_email, TEST_DATA
from app.src.import_data import crawl_data
def fonk1(b1 = None, b5=False):
    if b5:
        b2 = [email for email in load_email(TEST_DATA, b1=b1)]
    else:
        b3 = [email for email in load_email(HAM_DATA, b1=b1)]
        b4 = [email for email in load_email(SPAM_DATA, b1=b1)]
        b2 = b3 + b4
    return b2
crawl_data()
crawl_data(b5 = True)
a1 = 2000
b6 = TfidfVectorizer(stop_words='english')
b7 = fonk1(b1=a1)
b8 = np.array([0] * len(b3) + [1] * len(b4))
b9 = b6.fit_transform(b7)
X_train, X_test, Y_train, b10 = train_test_split(
    b9, b8, b11 = 0.2, random_state=42)
b12 = MultinomialNB(alpha=0.2)
b12.fit(X_train, Y_train)
b13 = b12.predict(X_test)
b14 = accuracy_score(b10, b13)
print("Accuracy Score:", b14)