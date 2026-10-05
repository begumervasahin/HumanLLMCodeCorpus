import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import string
nltk.download('punkt')
nltk.download('wordnet')
b1 = [
    "This is a sample document for testing the TF-IDF vectorization process.",
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is commonly used in natural language processing and information retrieval.",
]
def fonk1(text):
    b2 = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    b3 = nltk.stem.porter.PorterStemmer()
    b4 = nltk.stem.WordNetLemmatizer()
    b5 = [b3.stem(token) for token in b2]
    b6 = [b4.lemmatize(token) for token in b2]
    return b6
b7 = CountVectorizer(tokenizer=normalize_text, stop_words='english')
b8 = b7.fit_transform(b1).toarray()
print("Vocabulary:")
print(b7.vocabulary_)
b9 = TfidfTransformer(norm="l2")
b10 = b9.fit_transform(b8)
print("\nIDF Values:")
print(b9.idf_)
print("\nTF-IDF Matrix:")
print(b10.toarray())
b11 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
b10 = b11.fit_transform(b1)
b12 = (b10 * b10.T).toarray()
print("\nCosine Similarity Matrix:")
print(b12)