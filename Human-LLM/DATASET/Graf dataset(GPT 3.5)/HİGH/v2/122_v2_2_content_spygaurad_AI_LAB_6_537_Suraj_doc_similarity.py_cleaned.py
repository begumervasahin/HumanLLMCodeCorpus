import nltk
import re
import math
b1 = "I am Sam."
b2 = "Sam I am."
b3 = "I do not like green eggs and ham."
b4 = "I do not like them, Sam I am."
def fonk1(document):
    return set(nltk.word_tokenize((re.sub(r"\W", " ", document)).lower()))
b5 = fonk1(b1)
b6 = fonk1(b2)
b7 = fonk1(b3)
b8 = fonk1(b4)
def fonk2(set1, set2):
    b9 = set1.b9(set2)
    b10 = set1.b10(set2)
    return len(b9) / len(b10)
b11 = [b5, b6, b7, b8]
def fonk3(term, document):
    return document.count(term)
def fonk4(term):
    b12 = sum(1 for lst in b11 if term in lst)
    b13 = b12 if b12 > 0 else 1
    return math.log2(len(b11) / b13)
def fonk5(term, document):
    b14 = fonk3(term, document)
    b15 = fonk4(term)
    return b14 * b15
def fonk6(b5, b6):
    b16 = sum(fonk5(term, b5) * fonk5(term, b6) for term in b5 if term in b6)
    b17 = sum(pow(fonk5(term, b5), 2) for term in b5)
    b18 = sum(pow(fonk5(term, b6), 2) for term in b6)
    return b16 / (math.sqrt(b17 * b18))
print("Jaccard Similarity between d1 and d2:", fonk2(b5, b6))
print("Jaccard Similarity between d1 and d3:", fonk2(b5, b7))
print("Jaccard Similarity between d1 and d4:", fonk2(b5, b8))
print("Jaccard Similarity between d2 and d3:", fonk2(b6, b7))
print("Jaccard Similarity between d2 and d4:", fonk2(b6, b8))
print("Jaccard Similarity between d3 and d4:", fonk2(b7, b8))
print("Cosine Similarity between d1 and d2:", fonk6(b5, b6))
print("Cosine Similarity between d1 and d3:", fonk6(b5, b7))
print("Cosine Similarity between d1 and d4:", fonk6(b5, b8))
print("Cosine Similarity between d2 and d3:", fonk6(b6, b7))
print("Cosine Similarity between d2 and d4:", fonk6(b6, b8))
print("Cosine Similarity between d3 and d4:", fonk6(b7, b8))