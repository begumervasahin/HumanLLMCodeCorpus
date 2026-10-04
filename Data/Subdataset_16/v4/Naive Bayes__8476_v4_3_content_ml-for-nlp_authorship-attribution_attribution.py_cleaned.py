
import sys
import math
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab, top_cond_probs_by_author
from docopt import docopt
def fonk1(b16):
    return len(b16)
def fonk2(b16, c):
    return sum(1 for values in b16.values() if values[0] == c)
def fonk3(b16, c):
    b1 = {}
    for _, values in b16.items():
        if values[0] == c:
            for word, count in values[2].items():
                b1[word] = b1.get(word, 0) + count
    return b1
def fonk4(b15, b16, a1):
    b2 = extract_vocab(b16)
    b3 = {t: {} for t in b2}
    b4 = {}
    print("\n\n***\nCalculating b4 and conditional probabilities for each class...\n***")
    for c in b15:
        b4[c] = fonk2(b16, c) / fonk1(b16)
        print(f"\nPrior for {c}: {b4[c]}")
        b5 = fonk2(b16, c)
        print(f"In class {c}, we have {b5} document(s).")
        b1 = fonk3(b16, c)
        print("Calculating conditional probabilities for the b2.")
        b6 = sum(b1.values())
        for t in b2:
            b3[t][c] = (b1.get(t, 0) + a1) / (b6 + a1 * len(b2))
    return b2, b4, b3
def fonk5(b15, b2, b4, b3, test_document, b8, b13):
    b7 = {}
    if b8 = = "chars":
        _, _, b9 = process_document_ngrams(test_document, b13)
    elif b8 = = "b9":
        _, _, b9 = process_document_words(test_document)
    for c in b15:
        b7[c] = math.log(b4[c])
        for t in b9:
            if t in b3:
                b7[c] += b9[t] * math.log(b3[t][c])
    print("\n\nNow printing b7 in descending order:")
    for author in sorted(b7, b10 = b7.get, reverse=True):
        print(f"{author} score: {b7[author]}")
if b11 = = '__main__':
    b12 = docopt(__doc__, version='Authorship Attribution 1.1')
    b8 = "b9" if b12["--b9"] else "chars"
    b13 = -1 if b12["--b9"] else int(b12["--chars"])
    b14 = b12["<filename>"]
    a1 = 0.1
    b15 = ["Austen", "Carroll", "Grahame", "Shelley"]
    b16 = get_documents(b8, b13)
    b2, b4, b3 = fonk4(b15, b16, a1)
    for author in b15:
        print(f"\nBest features for {author}")
        top_cond_probs_by_author(b3, author, 10)
    fonk5(b15, b2, b4, b3, b14, b8, b13)