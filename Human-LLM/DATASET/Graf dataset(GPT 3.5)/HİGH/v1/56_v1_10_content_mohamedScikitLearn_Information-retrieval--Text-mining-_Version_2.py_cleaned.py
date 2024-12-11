import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import numpy as np
nltk.download('punkt')
nltk.download('wordnet')
b1 = [
    "This is a sample document for testing the TF-IDF vectorization process.",
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is commonly used in natural language processing and information retrieval.",
]
b2 = nltk.stem.porter.PorterStemmer()
b3 = nltk.stem.WordNetLemmatizer()
def fonk1(b5):
    return [b2.stem(token) for token in b5]
def fonk2(b5):
    return [b3.lemmatize(token) for token in b5]
b4 = dict((ord(punct), None) for punct in string.punctuation)
def fonk3(text):
    b5 = nltk.word_tokenize(text.lower().translate(b4))
    return fonk2(b5)
b6 = CountVectorizer(tokenizer=normalize_text, stop_words='english')
b7 = b6.fit_transform(b1).toarray()
print("Vocabulary:")
print(b6.vocabulary_)
print("\nTerm Frequency (TF) Matrix:")
print(b7)
b8 = TfidfTransformer(norm="l2")
b9 = b8.fit_transform(b7).toarray()
print("\nIDF Values:")
print(b8.idf_)
print("\nTF-IDF Matrix:")
print(b9)
def fonk4(text_list):
    b10 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    b9 = b10.fit_transform(text_list)
    return (b9 * b9.T).toarray()
print("\nCosine Similarity Matrix:")
print(fonk4(b1))