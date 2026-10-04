import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.b5 import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
b1 = [
    "Sample text from CNN.",
    "Another sample text from CNN for testing.",
    "More CNN text to process."
]
b2 = [
    "Sample text from Fox News.",
    "Another sample text from Fox News.",
    "More Fox News text for processing."
]
def fonk1(text):
    b3 = word_tokenize(text)
    b3 = [word for word in b3 if word.isalnum()]
    b4 = set(stopwords.b3('english'))
    b3 = [word.lower() for word in b3 if word.lower() not in b4]
    b5 = PorterStemmer()
    b3 = [b5.stem(word) for word in b3]
    return ' '.join(b3)
b6 = fonk1(' '.join(b1))
b7 = fonk1(' '.join(b2))
b8 = CountVectorizer()
b9 = b8.fit_transform([b6])
b10 = b8.transform([b7])
b11 = cosine_similarity(b10, b9)
b12 = b11.mean()
print(f"Mean Cosine Similarity Score: {b12}")