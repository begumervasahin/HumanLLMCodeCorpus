import nltk
import re
import math
b1 = "I am Sam."
b2 = "Sam I am."
b3 = "I do not like green eggs and ham."
b4 = "I do not like them, Sam I am."
b1 = nltk.word_tokenize((re.sub(r"\W", " ", b1)).lower())
b2 = nltk.word_tokenize((re.sub(r"\W", " ", b2)).lower())
b3 = nltk.word_tokenize((re.sub(r"\W", " ", b3)).lower())
b4 = nltk.word_tokenize((re.sub(r"\W", " ", b4)).lower())
def fonk1(seta, setb):
    b5 = seta.intersection(setb)
    return len(b5) / (len(seta) + len(setb) - len(b5))
b6 = [b1, b2, b3, b4]
def fonk2(term, document):
    return document.count(term)
def fonk3(term):
    a1 = 0
    a2 = 0
    for lst in b6:
        a1 += 1
        if term in lst:
            a2 += 1
    b7 = math.log2(a1 / a2)
    return b7
def fonk4(term, document):
    b8 = fonk2(term, document)
    b7 = fonk3(term)
    return b8 * b7
def fonk5(doc, query):
    a3 = 0
    a4 = 0
    a5 = 0
    for term in doc:
        if term in query:
            a3 += fonk4(term, doc) * fonk4(term, query)
    for term in doc:
        a4 += pow(fonk4(term, doc), 2)
    for term in query:
        a5 += pow(fonk4(term, query), 2)
    return a3 / (math.sqrt(a4 * a5))
print("The Jaccard similarity of b1 and b2 is", fonk1(set(b1), set(b2)))
print("The Jaccard similarity of b1 and b3 is", fonk1(set(b1), set(b3)))
print("The Jaccard similarity of b1 and b4 is", fonk1(set(b1), set(b4)))
print("The Jaccard similarity of b2 and b3 is", fonk1(set(b2), set(b3)))
print("The Jaccard similarity of b2 and b4 is", fonk1(set(b2), set(b4)))
print("The Jaccard similarity of b3 and b4 is", fonk1(set(b3), set(b4)))
print("The cosine similarity of b1 and b2 is", fonk5(b1, b2))
print("The cosine similarity of b1 and b3 is", fonk5(b1, b3))
print("The cosine similarity of b1 and b4 is", fonk5(b1, b4))
print("The cosine similarity of b2 and b3 is", fonk5(b2, b3))
print("The cosine similarity of b2 and b4 is", fonk5(b2, b4))
print("The cosine similarity of b3 and b4 is", fonk5(b3, b4))