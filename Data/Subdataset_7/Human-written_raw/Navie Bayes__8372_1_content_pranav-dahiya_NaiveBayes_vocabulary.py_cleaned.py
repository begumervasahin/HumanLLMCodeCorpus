import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
def fonk1(folder):
    b1 = glob.glob(folder+"*.txt")
    b2 = {}
    for filename in b1:
        with open(filename) as f:
            b3 = f.readlines()
            for line in b3:
                b4 = word_tokenize(line)
                for b5 in b4:
                    b5 = b5.lower()
                    if b5 in b2.keys():
                        b2[b5] += 1
                    else:
                        b2[b5] = 1
    b2.pop("", None)
    return b2
def fonk2(old_vocab, new_vocab):
    for b5 in new_vocab.keys():
        if b5 in list(old_vocab.keys()):
            old_vocab[b5] += new_vocab[b5]
        else:
            old_vocab[b5] = new_vocab[b5]
    return old_vocab
def fonk3(b2):
    b6 = set(stopwords.b4('english'))
    for b5 in b6:
        b2.pop(b5, None)
    return b2
def fonk4(b2):
    b7 = WordNetLemmatizer()
    for b5 in list(b2.keys()):
        b8 = b7.fonk4(b5)
        if b8 != b5:
            try:
                b2[b8] += b2[b5]
            except KeyError:
                pass
            b2.pop(b5)
    return b2
def fonk5(b2, percentile):
    b9 = np.percentile(np.fromiter(b2.values(), dtype=float), percentile)
    b10 = np.percentile(np.fromiter(b2.values(), dtype=float), 100-percentile)
    print(b9, b10)
    b2 = {key:value for key, value in b2.items() if value > b9 and value < b10}
    return b2
if b11 = = '__main__':
    b2 = {}
    for i in range(1, 11):
        b2 = fonk2(b2, fonk1("lingspam/part"+str(i)+"/"))
    with open("vocabulary1.pickle", "wb") as f:
        pickle.dump(b2, f)
    b2 = fonk3(b2)
    with open("vocabulary2.pickle", "wb") as f:
        pickle.dump(b2, f)
    b2 = fonk4(b2)
    with open("vocabulary3.pickle", "wb") as f:
        pickle.dump(b2, f)
    b2 = fonk5(b2, 2)
    with open("vocabulary4.pickle", "wb") as f:
        pickle.dump(b2, f)