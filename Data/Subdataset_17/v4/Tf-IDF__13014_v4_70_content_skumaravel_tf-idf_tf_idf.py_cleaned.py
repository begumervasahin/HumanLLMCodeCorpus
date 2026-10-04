import math
import string
def tf_idf(corpus, document, term):
    document = document.lower()
    exclude = set(string.punctuation)
    document = ''.join(ch for ch in document if ch not in exclude)
    doc_terms = document.split()
    total_terms_in_doc = len(doc_terms)
    term_frequency = doc_terms.count(term) / total_terms_in_doc
    total_documents = len(corpus)
    docs_with_term = sum(1 for doc in corpus if term in ''.join(ch for ch in doc.lower() if ch not in exclude).split())
    if docs_with_term != 0:
        idf = math.log(total_documents / docs_with_term)
    else:
        idf = 0
    return term_frequency * idf
corpus = [
    "This is a sample document.",
    "This document is another sample document.",
    "And this is a different document."
]
document = "This is a sample document."
term = "sample"
tf_idf_score = tf_idf(corpus, document, term)
print(f"TF-IDF score for term '{term}' in the document: {tf_idf_score}")