import nltk
import re
import math
d1 = "I am Sam."
d2 = "Sam I am."
d3 = "I do not like green eggs and ham."
d4 = "I do not like them, Sam I am."
d1 = nltk.word_tokenize((re.sub(r"\W", " ", d1)).lower())
d2 = nltk.word_tokenize((re.sub(r"\W", " ", d2)).lower())
d3 = nltk.word_tokenize((re.sub(r"\W", " ", d3)).lower())
d4 = nltk.word_tokenize((re.sub(r"\W", " ", d4)).lower())
def jaccard(seta, setb):
    common = seta.intersection(setb)
    return len(common) / (len(seta) + len(setb) - len(common))
corpus = [d1, d2, d3, d4]
def freq(term, document):
    return document.count(term)
def docfreq(term):
    doc_count = 0
    term_doc = 0
    for lst in corpus:
        doc_count += 1
        if term in lst:
            term_doc += 1
    idf = math.log2(doc_count / term_doc)
    return idf
def weight(term, document):
    tf = freq(term, document)
    idf = docfreq(term)
    return tf * idf
def cos_similarity(doc, query):
    numerator = 0
    wtd = 0
    wtq = 0
    for term in doc:
        if term in query:
            numerator += weight(term, doc) * weight(term, query)
    for term in doc:
        wtd += pow(weight(term, doc), 2)
    for term in query:
        wtq += pow(weight(term, query), 2)
    return numerator / (math.sqrt(wtd * wtq))
print("The Jaccard similarity of d1 and d2 is", jaccard(set(d1), set(d2)))
print("The Jaccard similarity of d1 and d3 is", jaccard(set(d1), set(d3)))
print("The Jaccard similarity of d1 and d4 is", jaccard(set(d1), set(d4)))
print("The Jaccard similarity of d2 and d3 is", jaccard(set(d2), set(d3)))
print("The Jaccard similarity of d2 and d4 is", jaccard(set(d2), set(d4)))
print("The Jaccard similarity of d3 and d4 is", jaccard(set(d3), set(d4)))
print("The cosine similarity of d1 and d2 is", cos_similarity(d1, d2))
print("The cosine similarity of d1 and d3 is", cos_similarity(d1, d3))
print("The cosine similarity of d1 and d4 is", cos_similarity(d1, d4))
print("The cosine similarity of d2 and d3 is", cos_similarity(d2, d3))
print("The cosine similarity of d2 and d4 is", cos_similarity(d2, d4))
print("The cosine similarity of d3 and d4 is", cos_similarity(d3, d4))