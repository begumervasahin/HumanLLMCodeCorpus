import nltk
import re
import math
def preprocess_text(text):
    tokens = nltk.word_tokenize(re.sub(r"\W", " ", text.lower()))
    return set(tokens)
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
def calculate_term_frequency(term, document):
    return document.count(term)
def calculate_document_frequency(term, corpus):
    doc_count = sum(1 for doc in corpus if term in doc)
    term_doc = doc_count if doc_count > 0 else 1
    return math.log2(len(corpus) / term_doc)
def calculate_weighted_term_frequency(term, document, corpus):
    tf = calculate_term_frequency(term, document)
    idf = calculate_document_frequency(term, corpus)
    return tf * idf
def calculate_cosine_similarity(doc1, doc2, corpus):
    common_terms = set(doc1).intersection(doc2)
    numerator = sum(calculate_weighted_term_frequency(term, doc1, corpus) * calculate_weighted_term_frequency(term, doc2, corpus) for term in common_terms)
    wtd = sum(pow(calculate_weighted_term_frequency(term, doc1, corpus), 2) for term in doc1)
    wtq = sum(pow(calculate_weighted_term_frequency(term, doc2, corpus), 2) for term in doc2)
    return numerator / (math.sqrt(wtd * wtq))
documents = [
    "I am Sam.",
    "Sam I am.",
    "I do not like green eggs and ham.",
    "I do not like them, Sam I am."
]
tokenized_docs = [preprocess_text(doc) for doc in documents]
for i in range(len(tokenized_docs)):
    for j in range(i + 1, len(tokenized_docs)):
        print(f"Jaccard Similarity between d{i + 1} and d{j + 1}:", jaccard_similarity(tokenized_docs[i], tokenized_docs[j]))
        print(f"Cosine Similarity between d{i + 1} and d{j + 1}:", calculate_cosine_similarity(tokenized_docs[i], tokenized_docs[j], tokenized_docs))