import math
from scipy import spatial
def inverse_document_frequency(term, all_documents):
    num_documents_with_this_term = sum(1 for doc in all_documents if term.lower() in doc.lower().split())
    if num_documents_with_this_term > 0:
        return 1.0 + math.log(float(len(all_documents)) / num_documents_with_this_term)
    else:
        return 1.0
def term_frequency(term, document):
    normalized_document = document.lower().split()
    return normalized_document.count(term.lower()) / float(len(normalized_document))
def get_tfidf(document, all_documents):
    terms = document.lower().split()
    tfidfs = []
    for term in terms:
        tf = term_frequency(term, document)
        idf = inverse_document_frequency(term, all_documents)
        tfidf = tf * idf
        tfidfs.append(tfidf)
    return tfidfs
def cosine_similarity(query, document):
    padding_len = abs(len(query) - len(document))
    padding = [0] * padding_len
    if len(query) > len(document):
        document.extend(padding)
    elif len(document) > len(query):
        query.extend(padding)
    return 1 - spatial.distance.cosine(query, document)