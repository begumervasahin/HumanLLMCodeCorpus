import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cnn_scroll = [
    "Sample text from CNN.",
    "Another sample text from CNN for testing.",
    "More CNN text to process."
]
fox_scroll = [
    "Sample text from Fox News.",
    "Another sample text from Fox News.",
    "More Fox News text for processing."
]
def preprocess_text(text):
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.lower() not in stop_words]
    porter = PorterStemmer()
    words = [porter.stem(word) for word in words]
    return ' '.join(words)
cnn_preprocessed = preprocess_text(' '.join(cnn_scroll))
fox_preprocessed = preprocess_text(' '.join(fox_scroll))
vectorizer = CountVectorizer()
cnn_vectorized = vectorizer.fit_transform([cnn_preprocessed])
fox_vectorized = vectorizer.transform([fox_preprocessed])
cosine_sim_score = cosine_similarity(fox_vectorized, cnn_vectorized)
mean_cosine_similarity = cosine_sim_score.mean()
print(f"Mean Cosine Similarity Score: {mean_cosine_similarity}")