import math
from scipy import spatial
def fonk1(term, all_documents):
    b1 = sum(1 for doc in all_documents if term.lower() in doc.lower().split())
    if b1 > 0:
        return 1.0 + math.log(float(len(all_documents)) / b1)
    else:
        return 1.0
def fonk2(term, document):
    b2 = document.lower().split()
    return b2.count(term.lower()) / float(len(b2))
def fonk3(document, all_documents):
    b3 = document.lower().split()
    b4 = []
    for term in b3:
        b5 = fonk2(term, document)
        b6 = fonk1(term, all_documents)
        b7 = b5 * b6
        b4.append(b7)
    return b4
def fonk4(b13, document):
    b8 = abs(len(b13) - len(document))
    b9 = [0] * b8
    if len(b13) > len(document):
        document.extend(b9)
    elif len(document) > len(b13):
        b13.extend(b9)
    return 1 - spatial.distance.cosine(b13, document)
b10 = "This is a sample document for testing TF-IDF and cosine similarity."
b11 = "TF-IDF stands for Term Frequency-Inverse Document Frequency."
b12 = [b10, b11]
b13 = "TF-IDF and cosine similarity are techniques used in information retrieval."
b14 = fonk3(b13, b12)
b15 = [fonk3(doc, b12) for doc in b12]
b16 = [fonk4(b14, doc_tfidf) for doc_tfidf in b15]
print(f"Query TF-IDF: {b14}")
for i, doc in enumerate(b12):
    print(f"Similarity with Document {i+1}: {b16[i]}")