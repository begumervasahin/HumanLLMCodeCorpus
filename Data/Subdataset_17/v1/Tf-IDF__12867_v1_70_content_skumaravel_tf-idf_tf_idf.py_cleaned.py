import math
import string
def preprocess_document(document):
    document = document.lower()
    exclude = set(string.punctuation)
    document = ''.join(ch for ch in document if ch not in exclude)
    return document
def calculate_tf(document, term):
    doc_term_list = document.split()
    doc_term_count = len(doc_term_list)
    term_count_in_document = doc_term_list.count(term)
    tf = term_count_in_document / doc_term_count
    return tf
def calculate_idf(corpus, term):
    doc_count = len(corpus)
    num_docs_with_term = sum(1 for doc in corpus if term in preprocess_document(doc).split())
    if num_docs_with_term > 0:
        idf = math.log(doc_count / num_docs_with_term)
    else:
        idf = 0
    return idf
def tf_idf(corpus, document, term):
    document = preprocess_document(document)
    term = term.lower()
    tf = calculate_tf(document, term)
    idf = calculate_idf(corpus, term)
    return tf * idf
corpus = [
    "This is a sample document.",
    "This document is another example document.",
    "And this is a different document."
]
document = "This document is a sample document."
term = "document"
tfidf_score = tf_idf(corpus, document, term)
print(f"The TF-IDF score for the term '{term}' is: {tfidf_score}")