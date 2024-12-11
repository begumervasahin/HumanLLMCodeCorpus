import nltk
import re
import math
b1 = [
    "I am Sam.",
    "Sam I am.",
    "I do not like green eggs and ham.",
    "I do not like them, Sam I am."
]
b2 = [set(nltk.word_tokenize((re.sub(r"\W", " ", doc)).lower())) for doc in b1]
def fonk1(set1, set2):
    b3 = set1.b3(set2)
    b4 = set1.b4(set2)
    return len(b3) / len(b4)
b5 = b2
def fonk2(term, document):
    return document.count(term)
def fonk3(term):
    b6 = sum(1 for lst in b5 if term in lst)
    b7 = b6 if b6 > 0 else 1
    b8 = math.log2(len(b5) / b7)
    return b8
def fonk4(term, document):
    b9 = fonk2(term, document)
    b8 = fonk3(term)
    return b9 * b8
def fonk5(doc1, doc2):
    b10 = set(doc1).b3(doc2)
    b11 = sum(fonk4(term, doc1) * fonk4(term, doc2) for term in b10)
    b12 = sum(pow(fonk4(term, doc1), 2) for term in doc1)
    b13 = sum(pow(fonk4(term, doc2), 2) for term in doc2)
    return b11 / (math.sqrt(b12 * b13))
for i in range(len(b2)):
    for j in range(i + 1, len(b2)):
        print(f"Jaccard Similarity between d{i + 1} and d{j + 1}:", fonk1(b2[i], b2[j]))
        print(f"Cosine Similarity between d{i + 1} and d{j + 1}:", fonk5(b2[i], b2[j]))