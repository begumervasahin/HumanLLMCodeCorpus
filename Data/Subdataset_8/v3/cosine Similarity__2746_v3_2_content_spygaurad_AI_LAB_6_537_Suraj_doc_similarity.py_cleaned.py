import nltk
import re
import math
documents = [
    "I am Sam.",
    "Sam I am.",
    "I do not like green eggs and ham.",
    "I do not like them, Sam I am."
]
def preprocess(document):
    return set(nltk.word_tokenize(re.sub(r"\W", " ", document.lower())))
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
def inverse_document_frequency(term, corpus):
    doc_count = sum(1 for doc in corpus if term in doc)
    term_doc = doc_count if doc_count > 0 else 1
    return math.log2(len(corpus) / term_doc)
def weighted_term_frequency(term, document, corpus):
    tf = document.count(term)
    idf = inverse_document_frequency(term, corpus)
    return tf * idf
def cosine_similarity(doc1, doc2, corpus):
    common_terms = set(doc1).intersection(doc2)
    numerator = sum(weighted_term_frequency(term, doc1, corpus) * weighted_term_frequency(term, doc2, corpus) for term in common_terms)
    wtd = sum(pow(weighted_term_frequency(term, doc1, corpus), 2) for term in doc1)
    wtq = sum(pow(weighted_term_frequency(term, doc2, corpus), 2) for term in doc2)
    return numerator / (math.sqrt(wtd * wtq))
tokenized_docs = [preprocess(doc) for doc in documents]
for i in range(len(tokenized_docs)):
    for j in range(i + 1, len(tokenized_docs)):
        print(f"Jaccard Similarity between d{i + 1} and d{j + 1}:", jaccard_similarity(tokenized_docs[i], tokenized_docs[j]))
        print(f"Cosine Similarity between d{i + 1} and d{j + 1}:", cosine_similarity(tokenized_docs[i], tokenized_docs[j], tokenized_docs))