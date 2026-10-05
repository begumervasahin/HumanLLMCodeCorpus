import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
nltk.download('punkt')
nltk.download('wordnet')
dataAll = [
    "This is a sample document for testing the TF-IDF vectorization process.",
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is commonly used in natural language processing and information retrieval.",
]
stemmer = nltk.stem.porter.PorterStemmer()
lemmatizer = nltk.stem.WordNetLemmatizer()
def stem_tokens(tokens):
    return [stemmer.stem(token) for token in tokens]
def lemmatize_tokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]
def normalize_text(text):
    tokens = nltk.word_tokenize(text.translate(str.maketrans('', '', string.punctuation)).lower())
    return lemmatize_tokens(tokens)
lem_vectorizer = CountVectorizer(tokenizer=normalize_text, stop_words='english')
tf_matrix = lem_vectorizer.fit_transform(dataAll).toarray()
print("Vocabulary:")
print(lem_vectorizer.vocabulary_)
print("\nTerm Frequency (TF) Matrix:")
print(tf_matrix)
tfidf_transformer = TfidfTransformer(norm="l2")
tfidf_matrix = tfidf_transformer.fit_transform(tf_matrix).toarray()
print("\nIDF Values:")
print(tfidf_transformer.idf_)
print("\nTF-IDF Matrix:")
print(tfidf_matrix)
def cos_similarity(text_list):
    tfidf_vectorizer = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(text_list)
    return (tfidf_matrix * tfidf_matrix.T).toarray()
print("\nCosine Similarity Matrix:")
print(cos_similarity(dataAll))