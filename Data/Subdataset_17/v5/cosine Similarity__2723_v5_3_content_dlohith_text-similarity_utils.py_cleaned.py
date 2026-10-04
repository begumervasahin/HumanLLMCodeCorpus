import math
from scipy import spatial
def inverse_document_frequency(term, all_documents):
    num_documents_with_term = sum(1 for doc in all_documents if term.lower() in doc.lower().split())
    if num_documents_with_term > 0:
        return 1.0 + math.log(float(len(all_documents)) / num_documents_with_term)
    else:
        return 1.0
def term_frequency(term, document):
    normalized_document = document.lower().split()
    return normalized_document.count(term.lower()) / float(len(normalized_document))
def get_tfidf(document, all_documents):
    terms = document.lower().split()
    tfidf_vector = []
    for term in terms:
        tf = term_frequency(term, document)
        idf = inverse_document_frequency(term, all_documents)
        tfidf = tf * idf
        tfidf_vector.append(tfidf)
    return tfidf_vector
def cosine_similarity(vector1, vector2):
    padding_length = abs(len(vector1) - len(vector2))
    padding = [0] * padding_length
    if len(vector1) > len(vector2):
        vector2.extend(padding)
    elif len(vector2) > len(vector1):
        vector1.extend(padding)
    return 1 - spatial.distance.cosine(vector1, vector2)