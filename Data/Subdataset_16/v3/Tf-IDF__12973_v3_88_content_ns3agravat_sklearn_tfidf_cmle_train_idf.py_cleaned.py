
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
def fonk1():
    return fetch_20newsgroups(b1 = 'train', shuffle=True)
def fonk2():
    return TfidfVectorizer(
        b2 = 'english',
        b3 = True,
        b4 = 'unicode',
        b5 = 'word',
        b6 = r'\w{2,}',
        b7 = (1, 1),
        a1 = 30000
    )
def fonk3(X_train, y_train):
    b8 = MultinomialNB()
    b8.fit(X_train, y_train)
    return b8
def fonk4(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)
def fonk5():
    b9 = fonk1()
    b10 = fonk2()
    b10.fit(b9.data)
    b11 = b10.transform(b9.data)
    b12 = fonk3(b11, b9.target)
    fonk4(b12, 'b12.pkl')
    fonk4(b10, 'vectorizer.pkl')
    print("Model and vectorizer have been saved to disk.")
if b13 = = "__main__":
    fonk5()