import math
import string
def preprocess_document(document):
    document = document.lower()
    exclude = set(string.punctuation)
    document = ''.join(ch for ch in document if ch not in exclude)
    return document
def calculate_tf(doc_term_list, term):
    doc_term_count = len(doc_term_list)
    term_count_in_document = doc_term_list.count(term)
    tf = term_count_in_document / doc_term_count
    return tf
def calculate_idf(corpus, term):
    doc_count = len(corpus)
    num_docs_with_term = sum(1 for doc in corpus if term in doc)
    if num_docs_with_term != 0:
        idf = math.log(doc_count / num_docs_with_term)
    else:
        idf = 0
    return idf
def tf_idf(corpus, document, term):
    document = preprocess_document(document)
    doc_term_list = document.split()
    tf = calculate_tf(doc_term_list, term)
    idf = calculate_idf(corpus, term)
    return tf * idf