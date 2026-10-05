import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import string
nltk.download('punkt')
nltk.download('wordnet')
dataAll = [
    "This is a sample document for testing the TF-IDF vectorization process.",
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is commonly used in natural language processing and information retrieval.",
]
def normalize_text(text):
    tokens = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    stemmer = nltk.stem.porter.PorterStemmer()
    lemmatizer = nltk.stem.WordNetLemmatizer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens
count_vectorizer = CountVectorizer(tokenizer=normalize_text, stop_words='english')
tf_matrix = count_vectorizer.fit_transform(dataAll).toarray()
print("Vocabulary:")
print(count_vectorizer.vocabulary_)
tfidf_transformer = TfidfTransformer(norm="l2")
tfidf_matrix = tfidf_transformer.fit_transform(tf_matrix)
print("\nIDF Values:")
print(tfidf_transformer.idf_)
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
tfidf_vectorizer = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(dataAll)
cos_similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()
print("\nCosine Similarity Matrix:")
print(cos_similarity_matrix)