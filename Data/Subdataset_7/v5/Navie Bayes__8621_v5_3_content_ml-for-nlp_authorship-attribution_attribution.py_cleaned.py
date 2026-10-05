import sys
import os
import math
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
from docopt import docopt
def fonk1(b17):
    return len(b17)
def fonk2(b17, c):
    b1 = sum(1 for values in b17.values() if values[0] == c)
    return b1
def fonk3(b17, c):
    b2 = {}
    for d, values in b17.items():
        if values[0] == c:
            b2.update(values[2])
    return b2
def fonk4(b16, b17, a1):
    b3 = extract_vocab(b17)
    b4 = {t: {} for t in b3}
    b5 = {}
    print("\n\n***\nCalculating b5 and conditional probabilities for each class...\n***")
    for c in b16:
        b5[c] = fonk2(b17, c) / fonk1(b17)
        print("\nPrior for", c, b5[c])
        b6 = fonk2(b17, c)
        print("In class", c, "we have", b6, "document(s).")
        b2 = fonk3(b17, c)
        print("Calculating conditional probabilities for the b3.")
        b7 = sum(b2.values())
        for t in b3:
            b4[t][c] = (b2.get(t, 0) + a1) / (b7 * (1 + a1))
    return b3, b5, b4
def fonk5(b16, b3, b5, b4, test_document, b9, b14):
    b8 = {}
    if b9 = = "chars":
        author, doc_length, b10 = process_document_ngrams(test_document, b14)
    elif b9 = = "b10":
        author, doc_length, b10 = process_document_words(test_document)
    for c in b16:
        b8[c] = math.log(b5[c])
        for t in b10:
            if t in b4:
                b8[c] += b10[t] * math.log(b4[t][c])
    print("\n\nNow printing b8 in descending order:")
    for author in sorted(b8, b11 = b8.get, reverse=True):
        print(author, "score:", b8[author])
if b12 = = '__main__':
    b13 = docopt(__doc__, version='Authorship Attribution 1.1')
    b9 = "b10" if b13["--b10"] else "chars"
    b14 = -1 if b13["--b10"] else int(b13["--chars"])
    b15 = b13["<filename>"]
    a1 = 0.1
    b16 = ["Austen", "Carroll", "Grahame", "Shelley"]
    b17 = get_documents(b9, b14)
    b3, b5, b4 = fonk4(b16, b17, a1)
    for author in b16:
        print("\nBest features for", author)
        top_cond_probs_by_author(b4, author, 10)
    fonk5(b16, b3, b5, b4, b15, b9, b14)