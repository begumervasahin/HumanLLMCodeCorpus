import math
from scipy import spatial
def fonk1(term, allDocuments):
    a1 = 0
    for doc in allDocuments:
        if term.lower() in doc.lower().split():
            a1 += 1
    if a1 > 0:
        return 1.0 + math.log(float(len(allDocuments)) / a1)
    else:
        return 1.0
def fonk2(term, document):
    b1 = document.lower().split()
    return b1.count(term.lower()) / float(len(b1))
def fonk3(document, allDocuments):
    b2 = document.lower().split()
    b3 = []
    for term in b2:
        b4 = fonk2(term, document)
        b5 = fonk1(term, allDocuments)
        b6 = b4 * b5
        b3.append(b6)
    return b3
def fonk4(b12, document):
    b7 = abs(len(b12) - len(document))
    b8 = [0] * b7
    if len(b12) > len(document):
        document.extend(b8)
    elif len(document) > len(b12):
        b12.extend(b8)
    return 1 - spatial.distance.cosine(b12, document)
b9 = "This is a sample document for testing TF-IDF and cosine similarity."
b10 = "TF-IDF stands for Term Frequency-Inverse Document Frequency."
b11 = [b9, b10]
b12 = "TF-IDF and cosine similarity are techniques used in information retrieval."
b13 = fonk3(b12, b11)
b14 = [fonk3(doc, b11) for doc in b11]
b15 = [fonk4(b13, doc_tfidf) for doc_tfidf in b14]
print(f"Query TF-IDF: {b13}")
for i, doc in enumerate(b11):
    print(f"Similarity with Document {i+1}: {b15[i]}")