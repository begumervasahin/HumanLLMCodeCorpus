import math
import string
def tf_idf(corpus, document, term):
    document = document.lower()
    exclude = set(string.punctuation)
    document = ''.join(ch for ch in document if ch not in exclude)
    doc_term_list = document.split()
    doc_term_count = len(doc_term_list)
    term_count_in_document = doc_term_list.count(term)
    tf = term_count_in_document / doc_term_count
    doc_count = len(corpus)
    num_docs_with_term = sum(1 for doc in corpus if term in doc.lower().split())
    if num_docs_with_term != 0:
        temp_idf = doc_count / num_docs_with_term
        idf = math.log(temp_idf)
    else:
        idf = 0
    tfidf_score = tf * idf
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