from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
b1 = fetch_20newsgroups(subset='train', shuffle=True)
b2 = CountVectorizer()
b3 = TfidfTransformer()
b4 = TfidfVectorizer(
    b5 = 'english',
    b6 = True,
    b7 = 'unicode',
    b8 = 'word',
    b9 = r'\w{2,}',
    b10 = (1, 1),
    b11 = 30000)
b4.fit(b1.data)
b12 = b4.transform(b1.data)
b13 = MultinomialNB().fit(b12, b1.target)
b14 = 'b13.pkl'
pickle.dump(b13, open(b14, 'wb'))
pickle.dump(b4, open('vectorizer.pkl', 'wb'))