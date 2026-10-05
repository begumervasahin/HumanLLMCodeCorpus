import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
corpus_root = './presidential_debates'
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
document_frequencies = {}
document_log_frequencies = []
inverse_document_frequencies = {}
total_documents = 30
document_map = []
def calculate_idf():
    for term, frequency in document_frequencies.items():
        inverse_document_frequencies[term] = math.log(total_documents / frequency, 10)
def calculate_document_weight(doc_index):
    weight = {}
    for term, frequency in document_log_frequencies[doc_index].items():
        weight[term] = frequency * inverse_document_frequencies[term]
    return weight
def calculate_document_length(doc_weight):
    return sum(weight ** 2 for weight in doc_weight.values()) ** 0.5
def calculate_normalized_document_weight(doc_index):
    normalized_weight = {}
    for term, weight in list_weights[doc_index].items():
        normalized_weight[term] = weight / document_lengths[doc_index]
    return normalized_weight
def get_idf(token):
    return inverse_document_frequencies.get(token, -1)
def get_weight(filename, token):
    doc_index = document_map.index(filename)
    idf = get_idf(token)
    doc_weight = document_log_frequencies[doc_index]
    if token in doc_weight:
        tf = doc_weight[token]
        weight = (tf * idf) / document_lengths[doc_index]
        return weight
    else:
        return 0
def sorted_posting_list(term):
    try:
        doc_weights = {doc_index: weight for doc_index, weight in zip(posting_list[term][::2], posting_list[term][1::2])}
        sorted_docs = sorted(doc_weights, key=doc_weights.get, reverse=True)
        return sorted_docs[:10]
    except KeyError:
        return []
def execute_query(query_string):
    query_string = query_string.lower()
    tokens = tokenizer.tokenize(query_string)
    query_terms = [word for word in tokens if word not in stop_words]
    stemmed_query_terms = [stemmer.stem(term) for term in query_terms]
    query_log_frequencies = {term: 1 + math.log(frequency, 10) for term, frequency in nltk.FreqDist(stemmed_query_terms).items()}
    query_length = (sum(log_frequency ** 2 for log_frequency in query_log_frequencies.values())) ** 0.5
    normalized_query_weight = {term: frequency / query_length for term, frequency in query_log_frequencies.items()}
    query_tokens = [sorted_posting_list(term) for term in query_log_frequencies.keys()]
    intersection = query_tokens[0]
    for token in query_tokens:
        intersection = [doc_index for doc_index in token if doc_index in set(intersection)]
    if not intersection:
        return 'None', 0
    score_list = []
    for doc_index in intersection:
        score = sum(normalized_query_weight[term] * normalized_document_weights[doc_index].get(term, 0) for term in query_log_frequencies.keys())
        score_list.append(score)
    max_score = max(score_list)
    max_index = score_list.index(max_score)
    position = intersection[max_index]
    return document_map[position], max_score
for filename in os.listdir(corpus_root):
    with open(os.path.join(corpus_root, filename), "r", encoding='UTF-8') as file:
        document_map.append(filename)
        document = file.read().lower()
        tokens = tokenizer.tokenize(document)
        cleaned_tokens = [word for word in tokens if word not in stop_words]
        stemmed_tokens = [stemmer.stem(word) for word in cleaned_tokens]
        term_frequencies = nltk.FreqDist(stemmed_tokens)
        log_frequencies = {term: 1 + math.log(frequency, 10) for term, frequency in term_frequencies.items()}
        document_log_frequencies.append(log_frequencies)
        for term in term_frequencies.keys():
            document_frequencies[term] = document_frequencies.get(term, 0) + 1
calculate_idf()
list_weights = [calculate_document_weight(i) for i in range(len(document_map))]
document_lengths = [calculate_document_length(weights) for weights in list_weights]
normalized_document_weights = [calculate_normalized_document_weight(i) for i in range(len(document_map))]
posting_list = {}
for doc_index in range(len(document_map)):
    for term, weight in normalized_document_weights[doc_index].items():
        posting_list.setdefault(term, []).extend([doc_index, weight])
def main():
    while True:
        query_string = input("Enter your query (or 'exit' to quit): ")
        if query_string.lower() == 'exit':
            break
        else:
            result = execute