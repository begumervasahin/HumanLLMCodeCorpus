import nltk
import os
import math
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
corpus_root = './presidential_debates'
document_vectors = {}
document_frequency = Counter()
term_frequencies = {}
document_lengths = Counter()
postings_list = {}
def calculate_weight(filename, token):
    idf = get_inverse_document_frequency(token)
    return (1 + math.log10(term_frequencies[filename][token])) * idf
def get_inverse_document_frequency(token):
    if document_frequency[token] == 0:
        return -1
    return math.log10(len(term_frequencies) / document_frequency[token])
for filename in os.listdir(corpus_root):
    with open(os.path.join(corpus_root, filename), "r", encoding='UTF-8') as file:
        doc = file.read().lower()
        tokens = tokenizer.tokenize(doc)
        stopwords_set = set(stopwords.words('english'))
        tokens = [stemmer.stem(token) for token in tokens if token not in stopwords_set]
        tf = Counter(tokens)
        document_frequency += Counter(list(set(tokens)))
        term_frequencies[filename] = tf.copy()
        tf.clear()
for filename in term_frequencies:
    document_vectors[filename] = Counter()
    length = 0
    for token in term_frequencies[filename]:
        weight = calculate_weight(filename, token)
        document_vectors[filename][token] = weight
        length += weight ** 2
    document_lengths[filename] = math.sqrt(length)
for filename in document_vectors:
    for token in document_vectors[filename]:
        document_vectors[filename][token] = document_vectors[filename][token] / document_lengths[filename]
        if token not in postings_list:
            postings_list[token] = Counter()
        postings_list[token][filename] = document_vectors[filename][token]
def get_weight(filename, token):
    return document_vectors[filename][token]
def query(qstring):
    qstring = qstring.lower()
    query_term_frequencies = {}
    query_length = 0
    flag = 0
    common_docs = set()
    tenth_weights = {}
    cosine_similarities = Counter()
    for token in qstring.split():
        token = stemmer.stem(token)
        if token not in postings_list:
            continue
        if get_inverse_document_frequency(token) == 0:
            common_docs = common_docs & set(postings_list[token].keys()) if flag else set(postings_list[token].keys())
        else:
            common_docs = common_docs | set(postings_list[token].keys())
            _, weights = zip(*postings_list[token].most_common(10))
            tenth_weights[token] = weights[9]
        query_term_frequencies[token] = 1 + math.log10(qstring.count(token))
        query_length += query_term_frequencies[token] ** 2
        flag = 1
    query_length = math.sqrt(query_length)
    for doc in document_vectors:
        cosine_similarity = 0
        for token in query_term_frequencies:
            if doc in postings_list[token]:
                cosine_similarity += (query_term_frequencies[token] / query_length) * postings_list[token][doc]
            else:
                cosine_similarity += (query_term_frequencies[token] / query_length) * tenth_weights[token]
        cosine_similarities[doc] = cosine_similarity
    most_similar_doc = cosine_similarities.most_common(1)
    document, similarity_score = zip(*most_similar_doc)
    try:
        return document[0], similarity_score[0] if document[0] in common_docs else "fetch more"
    except UnboundLocalError:
        return "None", 0
print("(%s, %.12f)" % query("health insurance wall street"))
print("(%s, %.12f)" % query("security conference ambassador"))
print("(%s, %.12f)" % query("particular constitutional amendment"))
print("(%s, %.12f)" % query("terror attack"))
print("(%s, %.12f)" % query("vector entropy"))