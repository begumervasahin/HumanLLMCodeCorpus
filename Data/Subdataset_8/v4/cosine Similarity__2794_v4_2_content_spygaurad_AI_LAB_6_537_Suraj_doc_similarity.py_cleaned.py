import nltk
import re
import math
documents = [
    "I am Sam.",
    "Sam I am.",
    "I do not like green eggs and ham.",
    "I do not like them, Sam I am."
]
tokenized_docs = [set(nltk.word_tokenize((re.sub(r"\W", " ", doc)).lower())) for doc in documents]
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)
corpus = tokenized_docs
def term_frequency(term, document):
    return document.count(term)
def doc_frequency(term):
    doc_count = sum(1 for lst in corpus if term in lst)
    term_doc = doc_count if doc_count > 0 else 1
    idf = math.log2(len(corpus) / term_doc)
    return idf
def weighted_term_frequency(term, document):
    tf = term_frequency(term, document)
    idf = doc_frequency(term)
    return tf * idf
def cosine_similarity(doc1, doc2):
    common_terms = set(doc1).intersection(doc2)
    numerator = sum(weighted_term_frequency(term, doc1) * weighted_term_frequency(term, doc2) for term in common_terms)
    wtd = sum(pow(weighted_term_frequency(term, doc1), 2) for term in doc1)
    wtq = sum(pow(weighted_term_frequency(term, doc2), 2) for term in doc2)
    return numerator / (math.sqrt(wtd * wtq))
for i in range(len(tokenized_docs)):
    for j in range(i + 1, len(tokenized_docs)):
        print(f"Jaccard Similarity between d{i + 1} and d{j + 1}:", jaccard_similarity(tokenized_docs[i], tokenized_docs[j]))
        print(f"Cosine Similarity between d{i + 1} and d{j + 1}:", cosine_similarity(tokenized_docs[i], tokenized_docs[j]))