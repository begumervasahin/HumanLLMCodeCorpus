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
doc1 = "This is a sample document for testing TF-IDF and cosine similarity."
doc2 = "TF-IDF stands for Term Frequency-Inverse Document Frequency."
documents = [doc1, doc2]
query = "TF-IDF and cosine similarity are techniques used in information retrieval."
query_tfidf = get_tfidf(query, documents)
document_tfidfs = [get_tfidf(doc, documents) for doc in documents]
similarities = [cosine_similarity(query_tfidf, doc_tfidf) for doc_tfidf in document_tfidfs]
print(f"Query TF-IDF: {query_tfidf}")
for i, doc in enumerate(documents):
    print(f"Similarity with Document {i+1}: {similarities[i]}")