import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.b8 import PorterStemmer
from sklearn.feature_extraction.b3 import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
b1 = [
    "Sample b3 from CNN.",
    "Another sample b3 from CNN for testing.",
    "More CNN b3 to process."
]
b2 = [
    "Sample b3 from Fox News.",
    "Another sample b3 from Fox News.",
    "More Fox News b3 for processing."
]
def fonk1(b3):
    b3 = ' '.join(b3)
    b4 = word_tokenize(b3)
    b4 = re.split(r'\W+', ' '.join(b4))
    b5 = str.maketrans('', '', string.punctuation)
    b6 = [w.translate(b5) for w in b4]
    b4 = [word.lower() for word in b6]
    b7 = set(stopwords.b4('english'))
    b4 = [w for w in b4 if w.isalpha() and not w in b7]
    b8 = PorterStemmer()
    b4 = [b8.stem(word) for word in b4]
    return b4
b9 = fonk1(b1)
b10 = fonk1(b2)
b11 = CountVectorizer()
b12 = b11.fit_transform([' '.join(b9)])
b13 = b11.transform([' '.join(b10)])
b14 = cosine_similarity(b13, b12)
b15 = b14.mean()
print(f"Mean Cosine Similarity Score: {b15}")