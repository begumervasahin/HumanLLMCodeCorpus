import math
from scipy import spatial
def fonk1(term, all_documents):
    b1 = sum(1 for doc in all_documents if term.lower() in doc.lower().split())
    if b1 > 0:
        return 1.0 + math.log(len(all_documents) / b1)
    else:
        return 1.0
def fonk2(term, document):
    b2 = document.lower().split()
    return b2.count(term.lower()) / len(b2)
def fonk3(document, all_documents):
    b3 = document.lower().split()
    b4 = []
    for term in b3:
        b5 = fonk2(term, document)
        b6 = fonk1(term, all_documents)
        b7 = b5 * b6
        b4.append(b7)
    return b4
def fonk4(query, document):
    b8 = abs(len(query) - len(document))
    b9 = [0] * b8
    if len(query) > len(document):
        document.extend(b9)
    elif len(document) > len(query):
        query.extend(b9)
    return 1 - spatial.distance.cosine(query, document)
b10 = "This is a sample document."
b11 = "Another document with some more text."
b12 = [b10, b11]
b13 = fonk3(b10, b12)
b14 = fonk3(b11, b12)
b15 = fonk4(b13, b14)
print("Cosine Similarity:", b15)