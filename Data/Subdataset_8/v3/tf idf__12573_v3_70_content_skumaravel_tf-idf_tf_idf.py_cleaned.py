import math
import string
def preprocess_document(document):
    document = document.lower()
    exclude = set(string.punctuation)
    document = ''.join(ch for ch in document if ch not in exclude)
    return document
def calculate_tf(term_count, total_terms):
    return term_count / total_terms
def calculate_idf(num_docs_with_term, total_docs):
    if num_docs_with_term != 0:
        return math.log(total_docs / num_docs_with_term)
    else:
        return 0
def calculate_tfidf(tf, idf):
    return tf * idf
def tf_idf(corpus, document, term):
    document = preprocess_document(document)
    doc_term_list = document.split()
    doc_term_count = len(doc_term_list)
    term_count_in_document = doc_term_list.count(term)
    tf = calculate_tf(term_count_in_document, doc_term_count)
    doc_count = len(corpus)
    num_docs_with_term = sum(1 for doc in corpus if term in preprocess_document(doc).split())
    idf = calculate_idf(num_docs_with_term, doc_count)
    tfidf_score = calculate_tfidf(tf, idf)
    return tfidf_score
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]
document = "This is the first document."
term = "document"
print("TF-IDF Score:", tf_idf(corpus, document, term))