import pickle
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
b1 = fetch_20newsgroups(subset='train', shuffle=True)
b2 = TfidfVectorizer(
    b3 = 'english',
    b4 = True,
    b5 = 'unicode',
    b6 = 'word',
    b7 = r'\w{2,}',
    b8 = (1, 1),
    a1 = 30000
)
b9 = b2.fit_transform(b1.data)
b10 = MultinomialNB().fit(b9, b1.target)
with open('b10.pkl', 'wb') as clf_file:
    pickle.dump(b10, clf_file)
with open('b2.pkl', 'wb') as vec_file:
    pickle.dump(b2, vec_file)