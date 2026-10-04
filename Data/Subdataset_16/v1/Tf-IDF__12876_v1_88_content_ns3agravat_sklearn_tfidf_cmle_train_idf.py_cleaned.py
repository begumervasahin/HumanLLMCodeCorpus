
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
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
b2.fit(b1.data)
b9 = b2.transform(b1.data)
b10 = MultinomialNB().fit(b9, b1.target)
with open('b10.pkl', 'wb') as model_file:
    pickle.dump(b10, model_file)
with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(b2, vectorizer_file)
print("Model and vectorizer have been saved to disk.")