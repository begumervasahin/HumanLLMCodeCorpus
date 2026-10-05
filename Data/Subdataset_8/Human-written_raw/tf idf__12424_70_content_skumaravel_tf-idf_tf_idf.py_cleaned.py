
import math
import string
def tf_idf(corpus, document, term):
    document = document.lower()
    exclude = set(string.punctuation)
    document = ''.join(ch for ch in document if ch not in exclude)
    doc_term_list = document.split()
    doc_term_count = len(doc_term_list)
    term_count_in_document = 0
    for t in doc_term_list:
        if t == term:
            term_count_in_document += 1
    tf = term_count_in_document/doc_term_count
    doc_count = len(corpus)
    num_docs_with_term = 0
    for doc in corpus:
        doc = doc.lower()
        doc = ''.join(ch for ch in doc if ch not in exclude)
        d_words = doc.lower().split()
        if term in d_words:
            num_docs_with_term += 1
    if num_docs_with_term != 0:
        temp_idf = doc_count/num_docs_with_term
        idf = math.log(temp_idf)
    else:
        idf = 0
    return tf*idf