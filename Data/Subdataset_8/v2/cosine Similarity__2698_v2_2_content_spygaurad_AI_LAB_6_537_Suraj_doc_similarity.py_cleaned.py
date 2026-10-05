import nltk
import re
import math
document1 = "I am Sam."
document2 = "Sam I am."
document3 = "I do not like green eggs and ham."
document4 = "I do not like them, Sam I am."
def preprocess(document):
    return set(nltk.word_tokenize((re.sub(r"\W", " ", document)).lower()))
doc1 = preprocess(document1)
doc2 = preprocess(document2)
doc3 = preprocess(document3)
doc4 = preprocess(document4)
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
corpus = [doc1, doc2, doc3, doc4]
def term_frequency(term, document):
    return document.count(term)
def inverse_document_frequency(term):
    doc_count = sum(1 for lst in corpus if term in lst)
    term_doc = doc_count if doc_count > 0 else 1
    return math.log2(len(corpus) / term_doc)
def weighted_term_frequency(term, document):
    tf = term_frequency(term, document)
    idf = inverse_document_frequency(term)
    return tf * idf
def cosine_similarity(doc1, doc2):
    numerator = sum(weighted_term_frequency(term, doc1) * weighted_term_frequency(term, doc2) for term in doc1 if term in doc2)
    wtd = sum(pow(weighted_term_frequency(term, doc1), 2) for term in doc1)
    wtq = sum(pow(weighted_term_frequency(term, doc2), 2) for term in doc2)
    return numerator / (math.sqrt(wtd * wtq))
print("Jaccard Similarity between d1 and d2:", jaccard_similarity(doc1, doc2))
print("Jaccard Similarity between d1 and d3:", jaccard_similarity(doc1, doc3))
print("Jaccard Similarity between d1 and d4:", jaccard_similarity(doc1, doc4))
print("Jaccard Similarity between d2 and d3:", jaccard_similarity(doc2, doc3))
print("Jaccard Similarity between d2 and d4:", jaccard_similarity(doc2, doc4))
print("Jaccard Similarity between d3 and d4:", jaccard_similarity(doc3, doc4))
print("Cosine Similarity between d1 and d2:", cosine_similarity(doc1, doc2))
print("Cosine Similarity between d1 and d3:", cosine_similarity(doc1, doc3))
print("Cosine Similarity between d1 and d4:", cosine_similarity(doc1, doc4))
print("Cosine Similarity between d2 and d3:", cosine_similarity(doc2, doc3))
print("Cosine Similarity between d2 and d4:", cosine_similarity(doc2, doc4))
print("Cosine Similarity between d3 and d4:", cosine_similarity(doc3, doc4))