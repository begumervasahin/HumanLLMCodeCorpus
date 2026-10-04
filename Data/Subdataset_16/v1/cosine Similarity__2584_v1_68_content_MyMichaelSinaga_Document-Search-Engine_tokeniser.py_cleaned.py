import math
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
def fonk1(raw_string):
    b1 = RegexpTokenizer(r'\w+')
    b2 = b1.tokenize(str(raw_string))
    b3 = [w.lower() for w in b2]
    return b3
def fonk2(token_normalised_text):
    b4 = PorterStemmer()
    b5 = [b4.fonk2(w) for w in token_normalised_text]
    return b5
def fonk3(b5, doc_id, b13):
    for root in b5:
        if root not in b13:
            b13[root] = {}
        if doc_id not in b13[root]:
            b13[root][doc_id] = 0
        b13[root][doc_id] += 1
    return b13
def fonk4(processed_query):
    b6 = {}
    for root in processed_query:
        if root not in b6:
            b6[root] = 0
        b6[root] += 1
    return b6
def fonk5(b13, b12):
    b7 = {word: len(b13[word]) for word in b13}
    for word in b13:
        for doc in b13[word]:
            b8 = 1 + math.log(b13[word][doc])
            b9 = math.log(b12 / b7[word])
            b13[word][doc] = b8 * b9
    return b13, b7
def fonk6(b6, b7, b12):
    for word in b6:
        b8 = 1 + math.log(b6[word])
        b9 = math.log(b12 / b7.get(word, b12))
        b6[word] = b8 * b9
    return b6
if b10 = = "__main__":
    b11 = ["The quick brown fox jumps over the lazy dog.", "The dog barks at the fox."]
    b12 = len(b11)
    b13 = {}
    for i, doc in enumerate(b11):
        b14 = fonk1(doc)
        b15 = fonk2(b14)
        b13 = fonk3(b15, f"doc_{i}", b13)
    b13, b7 = fonk5(b13, b12)
    b16 = "quick fox"
    b17 = fonk1(b16)
    b18 = fonk2(b17)
    b6 = fonk4(b18)
    b19 = fonk6(b6, b7, b12)
    print("TF-IDF for Documents:", b13)
    print("TF-IDF for Query:", b19)