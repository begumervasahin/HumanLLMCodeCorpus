
import sys
import os
import math
from docopt import docopt
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
def fonk1(b17):
    return len(b17)
def fonk2(b17, class_name):
    return sum(1 for values in b17.values() if values[0] == class_name)
def fonk3(b17, class_name):
    b1 = {}
    for values in b17.values():
        if values[0] == class_name:
            for word, freq in values[2].items():
                b1[word] = b1.get(word, 0) + freq
    return b1
def fonk4(b16, b17, b2 = 0.1):
    b3 = extract_vocab(b17)
    b4 = {t: {} for t in b3}
    b5 = {}
    print("\n\n***\nCalculating b5 and conditional probabilities for each class...\n***")
    for class_name in b16:
        b5[class_name] = fonk2(b17, class_name) / fonk1(b17)
        print(f"\nPrior for {class_name}: {b5[class_name]}")
        b6 = fonk2(b17, class_name)
        print(f"In class {class_name}, we have {b6} document(s).")
        b1 = fonk3(b17, class_name)
        print("Calculating conditional probabilities for the b3.")
        b7 = sum(b1.values())
        for t in b3:
            b4[t][class_name] = (
                (b1.get(t, 0) + b2) /
                (b7 + b2 * len(b3))
            )
    return b3, b5, b4
def fonk5(b16, b3, b5, b4, test_document, b9, b14):
    b8 = {}
    if b9 = = "chars":
        _, _, b10 = process_document_ngrams(test_document, b14)
    else:
        _, _, b10 = process_document_words(test_document)
    for class_name in b16:
        b8[class_name] = math.log(b5[class_name])
        for word in b10:
            if word in b4:
                b8[class_name] += b10[word] * math.log(b4[word][class_name])
    print("\n\nNow printing b8 in descending order:")
    for author in sorted(b8, b11 = b8.get, reverse=True):
        print(f"{author} score: {b8[author]}")
if b12 = = '__main__':
    b13 = docopt(__doc__, version='Authorship Attribution 1.1')
    b9 = "b10" if b13["--b10"] else "chars"
    b14 = int(b13["--chars"]) if b13["--chars"] else -1
    b15 = b13["<filename>"]
    b2 = 0.1
    b16 = ["Austen", "Carroll", "Grahame", "Shelley"]
    b17 = get_documents(b9, b14)
    b3, b5, b4 = fonk4(b16, b17, b2)
    for author in b16:
        print(f"\nBest features for {author}")
        top_cond_probs_by_author(b4, author, 10)
    fonk5(b16, b3, b5, b4, b15, b9, b14)