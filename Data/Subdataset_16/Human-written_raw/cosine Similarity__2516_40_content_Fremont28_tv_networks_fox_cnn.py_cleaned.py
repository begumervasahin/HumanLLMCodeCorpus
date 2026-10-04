import re
import string
b1 = cnn_scroll
b1 = ' '.join(b1)
b1 = b1.split()
b1 = re.split(r'\W+',b1)
b2 = str.maketrans('','',string.punctuation)
b3 = [w.translate(b2) for w in b1]
b1 = [word.lower() for word in b1]
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.b5 import PorterStemmer
b1 = word_tokenize(b1)
b1 = [w for w in b1 if w.isalpha()]
b1
b4 = set(stopwords.words('english'))
b1 = [w for w in b1 if not w in b4]
b5 = PorterStemmer()
b1 = [b5.stem(w) for w in b1]
b6 = fox_scroll
b6 = ' '.join(b6)
b6 = word_tokenize(b6)
b6 = [w for w in b6 if w.isalpha() ]
b6 = [w for w in b6 if not w in b4]
b5 = PorterStemmer()
b6 = [b5.stem(w) for w in b6]
b7 = CountVectorizer(analyzer='word',min_df=1,
b4 = 'english',lowercase=True,token_pattern='[a-zA-Z0-9]{3,}')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
b8 = b7.fit_transform(b1)
b9 = b7.fit_transform(b6)
b10 = cosine_similarity(fox_vectorized1,fox_vectorized1)
b10.mean()