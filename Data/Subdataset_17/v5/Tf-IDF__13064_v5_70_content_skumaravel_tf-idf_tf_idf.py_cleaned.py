import math
import string
def preprocess_text(text):
    text = text.lower()
    exclude = set(string.punctuation)
    return ''.join(ch for ch in text if ch not in exclude)
def calculate_term_frequency(document, term):
    term_count = document.count(term)
    total_terms = len(document)
    return term_count / total_terms
def calculate_inverse_document_frequency(corpus, term):
    num_docs_with_term = sum(1 for doc in corpus if term in doc)
    total_documents = len(corpus)
    if num_docs_with_term > 0:
        return math.log(total_documents / num_docs_with_term)
    else:
        return 0
def tf_idf(corpus, document, term):
    preprocessed_corpus = [preprocess_text(doc).split() for doc in corpus]
    preprocessed_document = preprocess_text(document).split()
    tf = calculate_term_frequency(preprocessed_document, term)
    idf = calculate_inverse_document_frequency(preprocessed_corpus, term)
    return tf * idf
corpus = [
    "This is a sample document.",
    "This document is another sample document.",
    "And this is a different document."
]
document = "This is a sample document."
term = "sample"
tf_idf_score = tf_idf(corpus, document, term)
print(f"TF-IDF score for term '{term}' in the document: {tf_idf_score}")