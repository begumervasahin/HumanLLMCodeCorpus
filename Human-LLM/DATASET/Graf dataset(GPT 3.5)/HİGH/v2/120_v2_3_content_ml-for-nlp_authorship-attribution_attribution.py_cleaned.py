import sys
import math
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
from docopt import docopt
def fonk1(b19):
    return len(b19)
def fonk2(b19, class_label):
    b1 = sum(1 for _, (b3, _) in b19.items() if b3 == class_label)
    return b1
def fonk3(b19, class_label):
    b2 = {}
    for doc_id, (b3, word_freq) in b19.items():
        if b3 = = class_label:
            for word, freq in word_freq.items():
                b2[word] = b2.get(word, 0) + freq
    return b2
def fonk4(b18, b19, b4 = 0.1):
    b5 = extract_vocab(b19)
    b6 = {word: {c: 0 for c in b18} for word in b5}
    b7 = {}
    print("\n\n***\nCalculating b7 and conditional probabilities for each class...\n***")
    b8 = fonk1(b19)
    for c in b18:
        b7[c] = fonk2(b19, c) / b8
        print("\nPrior for", c, b7[c])
        b9 = fonk2(b19, c)
        print("In class", c, "we have", b9, "document(s).")
        b2 = fonk3(b19, c)
        print("Calculating conditional probabilities for the b5.")
        b10 = sum(b2.values())
        for t in b5:
            if t in b2:
                b6[t][c] = (b2[t] + b4) / (b10 + b4 * len(b5))
            else:
                b6[t][c] = b4 / (b10 + b4 * len(b5))
    return b5, b7, b6
def fonk5(b18, b5, b7, b6, test_document, b11 = "b13", a1=-1):
    b12 = {}
    if b11 = = "chars":
        author, doc_length, b13 = process_document_ngrams(test_document, a1)
    elif b11 = = "b13":
        author, doc_length, b13 = process_document_words(test_document)
    for c in b18:
        b12[c] = math.log(b7[c])
        for t in b13:
            if t in b6:
                b12[c] += b13[t] * math.log(b6[t][c])
    print("\n\nNow printing b12 in descending order:")
    for author in sorted(b12, b14 = b12.get, reverse=True):
        print(author, "score:", b12[author])
if b15 = = '__main__':
    b16 = docopt(__doc__, version='Authorship Attribution 1.1')
    if b16["--b13"]:
        b11 = "b13"
        a1 = -1
    if b16["--chars"]:
        b11 = "chars"
        a1 = int(b16["--chars"])
    b17 = b16["<filename>"]
    b18 = ["Austen", "Carroll", "Grahame", "Shelley"]
    b19 = get_documents(b11, a1)
    b5, b7, b6 = fonk4(b18, b19)
    for author in b18:
        print("\nBest features for", author)
        top_cond_probs_by_author(b6, author, 10)
    fonk5(b18, b5, b7, b6, b17, b11, a1)