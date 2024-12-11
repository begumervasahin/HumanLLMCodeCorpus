import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
nltk.download('punkt')
nltk.download('wordnet')
b1 = [
    "This is a sample document for testing the TF-IDF vectorization process.",
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is commonly used in natural language processing and information retrieval.",
]
def fonk1(text):
    b2 = nltk.word_tokenize(text.translate(str.maketrans('', '', string.punctuation)).lower())
    b3 = nltk.stem.WordNetLemmatizer()
    return [b3.lemmatize(token) for token in b2]
b4 = CountVectorizer(tokenizer=normalize_text, stop_words='english')
b5 = b4.fit_transform(b1).toarray()
print("Vocabulary:")
print(b4.vocabulary_)
print("\nTerm Frequency (TF) Matrix:")
print(b5)
b6 = TfidfTransformer(norm="l2")
b7 = b6.fit_transform(b5).toarray()
print("\nIDF Values:")
print(b6.idf_)
print("\nTF-IDF Matrix:")
print(b7)
def fonk2(text_list):
    b4 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    b7 = b4.fit_transform(text_list)
    return (b7 * b7.T).toarray()
print("\nCosine Similarity Matrix:")
print(fonk2(b1))