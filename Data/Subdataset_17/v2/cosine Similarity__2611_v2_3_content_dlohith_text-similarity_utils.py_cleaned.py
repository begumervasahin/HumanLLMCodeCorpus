import math
from scipy import spatial
def inverseDocumentFrequency(term, allDocuments):
    numDocumentsWithThisTerm = sum(1 for doc in allDocuments if term.lower() in doc.lower().split())
    if numDocumentsWithThisTerm > 0:
        return 1.0 + math.log(float(len(allDocuments)) / numDocumentsWithThisTerm)
    else:
        return 1.0
def termFrequency(term, document):
    normalizedDocument = document.lower().split()
    return normalizedDocument.count(term.lower()) / float(len(normalizedDocument))
def getTFIDF(document, allDocuments):
    terms = document.lower().split()
    tfidfs = []
    for term in terms:
        tf = termFrequency(term, document)
        idf = inverseDocumentFrequency(term, allDocuments)
        tfidf = tf * idf
        tfidfs.append(tfidf)
    return tfidfs
def cosineSimilarity(query, document):
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
query_tfidf = getTFIDF(query, documents)
document_tfidfs = [getTFIDF(doc, documents) for doc in documents]
similarities = [cosineSimilarity(query_tfidf, doc_tfidf) for doc_tfidf in document_tfidfs]
print(f"Query TF-IDF: {query_tfidf}")
for i, doc in enumerate(documents):
    print(f"Similarity with Document {i+1}: {similarities[i]}")