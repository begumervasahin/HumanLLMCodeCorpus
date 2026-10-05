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
b2 = nltk.stem.porter.PorterStemmer()
b3 = nltk.stem.WordNetLemmatizer()
def fonk1(b4):
    return [b2.stem(token) for token in b4]
def fonk2(b4):
    return [b3.lemmatize(token) for token in b4]
def fonk3(text):
    b4 = nltk.word_tokenize(text.translate(str.maketrans('', '', string.punctuation)).lower())
    return fonk2(b4)
b5 = CountVectorizer(tokenizer=normalize_text, stop_words='english')
b6 = b5.fit_transform(b1).toarray()
print("Vocabulary:")
print(b5.vocabulary_)
print("\nTerm Frequency (TF) Matrix:")
print(b6)
b7 = TfidfTransformer(norm="l2")
b8 = b7.fit_transform(b6).toarray()
print("\nIDF Values:")
print(b7.idf_)
print("\nTF-IDF Matrix:")
print(b8)
def fonk4(text_list):
    b9 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    b8 = b9.fit_transform(text_list)
    return (b8 * b8.T).toarray()
print("\nCosine Similarity Matrix:")
print(fonk4(b1))