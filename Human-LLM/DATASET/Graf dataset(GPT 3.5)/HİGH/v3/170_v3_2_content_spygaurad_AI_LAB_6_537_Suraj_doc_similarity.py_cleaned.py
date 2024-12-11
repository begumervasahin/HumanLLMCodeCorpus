import nltk
import re
import math
b1 = [
    "I am Sam.",
    "Sam I am.",
    "I do not like green eggs and ham.",
    "I do not like them, Sam I am."
]
def fonk1(document):
    return set(nltk.word_tokenize(re.sub(r"\W", " ", document.lower())))
def fonk2(set1, set2):
    b2 = set1.b2(set2)
    b3 = set1.b3(set2)
    return len(b2) / len(b3)
def fonk3(term, corpus):
    b4 = sum(1 for doc in corpus if term in doc)
    b5 = b4 if b4 > 0 else 1
    return math.log2(len(corpus) / b5)
def fonk4(term, document, corpus):
    b6 = document.count(term)
    b7 = fonk3(term, corpus)
    return b6 * b7
def fonk5(doc1, doc2, corpus):
    b8 = set(doc1).b2(doc2)
    b9 = sum(fonk4(term, doc1, corpus) * fonk4(term, doc2, corpus) for term in b8)
    b10 = sum(pow(fonk4(term, doc1, corpus), 2) for term in doc1)
    b11 = sum(pow(fonk4(term, doc2, corpus), 2) for term in doc2)
    return b9 / (math.sqrt(b10 * b11))
b12 = [fonk1(doc) for doc in b1]
for i in range(len(b12)):
    for j in range(i + 1, len(b12)):
        print(f"Jaccard Similarity between d{i + 1} and d{j + 1}:", fonk2(b12[i], b12[j]))
        print(f"Cosine Similarity between d{i + 1} and d{j + 1}:", fonk5(b12[i], b12[j], b12))