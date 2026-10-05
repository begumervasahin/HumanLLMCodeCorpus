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
N = 30
index = 0
document_map = []
for filename in os.listdir(corpus_root):
    with open(os.path.join(corpus_root, filename), "r", encoding='UTF-8') as file:
        document_map.append(filename)
        doc = file.read().lower()
        tokens = tokenizer.tokenize(doc)
        cleaned_tokens = [word for word in tokens if word not in stop_words]
        stemmed_tokens = [stemmer.stem(word) for word in cleaned_tokens]
        term_frequencies = nltk.FreqDist(stemmed_tokens)
        log_frequencies = {term: 1 + math.log(freq, 10) for term, freq in term_frequencies.items()}
        document_log_frequencies.append(log_frequencies)
        for term in term_frequencies.keys():
            document_frequencies[term] = document_frequencies.get(term, 0) + 1
        index += 1
for term, freq in document_frequencies.items():
    inverse_document_frequencies[term] = math.log(N / freq, 10)
list_weights = []
document_lengths = []
for log_freqs in document_log_frequencies:
    weights = {term: freq * inverse_document_frequencies[term] for term, freq in log_freqs.items()}
    list_weights.append(weights)
    length = sum(weight ** 2 for weight in weights.values()) ** 0.5
    document_lengths.append(length)
list_final_weight = []
for weights in list_weights:
    final_weight = {term: weight / length for term, weight in weights.items()}
    list_final_weight.append(final_weight)
posting_list = {}
for doc_index, weights in enumerate(list_final_weight):
    for term, weight in weights.items():
        posting_list.setdefault(term, []).extend([doc_index, weight])
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
    query_terms = [stemmer.stem(word) for word in tokens if word not in stop_words]
    query_frequencies = nltk.FreqDist(query_terms)
    query_log_frequencies = {term: 1 + math.log(freq, 10) for term, freq in query_frequencies.items()}
    query_length = sum(freq ** 2 for freq in query_log_frequencies.values()) ** 0.5
    normalized_query_weights = {term: freq / query_length for term, freq in query_log_frequencies.items()}
    query_tokens = [sorted_posting_list(term) for term in query_log_frequencies.keys()]
    intersection = set(query_tokens[0])
    for token in query_tokens:
        intersection.intersection_update(token)
    if not intersection:
        return 'None', 0
    scores = []
    for doc_index in intersection:
        score = sum(normalized_query_weights[term] * list_final_weight[doc_index].get(term, 0) for term in query_log_frequencies.keys())
        scores.append(score)
    max_score = max(scores)
    max_index = scores.index(max_score)
    position = intersection.pop()
    return document_map[position], max_score
def main():
    while True:
        query_string = input("Enter your query (or 'exit' to quit): ")
        if query_string.lower() == 'exit':
            break
        else:
            result = execute_query(query_string)
            print(f"Document: {result[0]}, Score: {result[1]}")
if __name__ == "__main__":
    main()