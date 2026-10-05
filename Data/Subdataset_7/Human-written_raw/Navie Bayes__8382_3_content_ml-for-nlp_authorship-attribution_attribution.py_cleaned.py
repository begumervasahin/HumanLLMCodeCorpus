
import sys
import os
import math
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
from docopt import docopt
def fonk1(b15):
    return len(b15)
def fonk2(b15, c):
    a1 = 0
    for values in b15.values():
        if values[0] == c:
            a1+=1
    return a1
def fonk3(b15,c):
    b1 = {}
    for d,values in b15.items():
        if values[0] == c:
            b1.update(values[2])
    return b1
def fonk4(b14, b15):
    b2 = extract_vocab(b15)
    b3 = {}
    for t in b2:
        b3[t] = {}
    b4 = {}
    print("\n\n***\nCalculating b4 and conditional probabilities for each class...\n***")
    for c in b14:
         b4[c] = fonk2(b15,c) / fonk1(b15)
         print("\nPrior for",c,b4[c])
         b5 = fonk2(b15, c)
         print("In class",c,"we have",b5,"document(s).")
         b1 = fonk3(b15,c)
         print("Calculating conditional probabilities for the b2.")
         b6 = sum(b1.values())
         for t in b2:
             if t in b1:
                 b3[t][c] = (b1[t] + a3) / (b6 * (1 + a3))
             else:
                 b3[t][c] = (0 + a3) / (b6 * (1 + a3))
    return b2, b4, b3
def fonk5(b14, b2, b4, b3, test_document):
    b7 = {}
    if b8 = = "chars":
        author, doc_length, b9 = process_document_ngrams(test_document,a2)
    elif b8 = = "b9":
        author, doc_length, b9 = process_document_words(test_document)
    for c in b14:
        b7[c] = math.log(b4[c])
        for t in b9:
            if t in b3:
                for i in range(b9[t]):
                    b7[c] += math.log(b3[t][c])
    print("\n\nNow printing b7 in descending order:")
    for author in sorted(b7, b10 = b7.get, reverse=True):
        print(author,"score:",b7[author])
if b11 = = '__main__':
    b12 = docopt(__doc__, version='Authorship Attribution 1.1')
    if b12["--b9"]:
        b8 = "b9"
        a2 = -1
    if b12["--chars"]:
        b8 = "chars"
        a2 = int(b12["--chars"])
    b13 = b12["<filename>"]
    a3 = 0.1
    b14 = ["Austen", "Carroll", "Grahame", "Shelley"]
    b15 = get_documents(b8, a2)
    b2, b4, b3 = fonk4(b14, b15)
    for author in b14:
        print("\nBest features for",author)
        top_cond_probs_by_author(b3, author, 10)
    fonk5(b14, b2, b4, b3, b13)