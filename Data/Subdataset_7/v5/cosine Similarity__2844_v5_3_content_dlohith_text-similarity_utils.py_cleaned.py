import math
from scipy import spatial
def fonk1(term, all_documents):
    b1 = sum(1 for doc in all_documents if term.lower() in doc.lower().split())
    if b1 > 0:
        b2 = 1.0 + math.log(len(all_documents) / b1)
    else:
        b2 = 1.0
    return b2
def fonk2(term, document):
    b3 = document.lower().split()
    return b3.count(term.lower()) / float(len(b3))
def fonk3(document, all_documents):
    b4 = document.lower().split()
    b5 = []
    for term in b4:
        b6 = fonk2(term, document)
        b2 = fonk1(term, all_documents)
        b7 = b6 * b2
        b5.append(b7)
    return b5
def fonk4(query, document):
    b8 = abs(len(query) - len(document))
    b9 = [0] * b8
    if len(query) > len(document):
        document.extend(b9)
    elif len(document) > len(query):
        query.extend(b9)
    return 1 - spatial.distance.cosine(query, document)