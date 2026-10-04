import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
def fonk1(b15):
    b1 = glob.glob(b15 + "*.txt")
    b2 = {}
    for filename in b1:
        with open(filename, 'r') as file:
            b3 = file.readlines()
            for line in b3:
                b4 = word_tokenize(line)
                for b5 in b4:
                    b5 = b5.lower()
                    if b5 in b2:
                        b2[b5] += 1
                    else:
                        b2[b5] = 1
    b2.pop("", None)
    return b2
def fonk2(old_vocab, new_vocab):
    for b5, count in new_vocab.items():
        if b5 in old_vocab:
            old_vocab[b5] += count
        else:
            old_vocab[b5] = count
    return old_vocab
def fonk3(b2):
    b6 = set(stopwords.b4('english'))
    for b5 in b6:
        b2.pop(b5, None)
    return b2
def fonk4(b2):
    b7 = WordNetLemmatizer()
    b8 = {}
    for b5 in list(b2.keys()):
        b9 = b7.lemmatize(b5)
        if b9 != b5:
            if b9 in b8:
                b8[b9] += b2[b5]
            else:
                b8[b9] = b2[b5]
        else:
            b8[b5] = b2[b5]
    return b8
def fonk5(b2, percentile):
    b10 = np.fromiter(b2.b10(), dtype=float)
    b11 = np.percentile(b10, percentile)
    b12 = np.percentile(b10, 100 - percentile)
    print(f"Lower bound: {b11}, Upper bound: {b12}")
    b13 = {key: value for key, value in b2.items() if b11 < value < b12}
    return b13
if b14 = = '__main__':
    b2 = {}
    for i in range(1, 11):
        b15 = f"lingspam/part{i}/"
        b2 = fonk2(b2, fonk1(b15))
    with open("vocabulary1.pickle", "wb") as file:
        pickle.dump(b2, file)
    b2 = fonk3(b2)
    with open("vocabulary2.pickle", "wb") as file:
        pickle.dump(b2, file)
    b2 = fonk4(b2)
    with open("vocabulary3.pickle", "wb") as file:
        pickle.dump(b2, file)
    b2 = fonk5(b2, 2)
    with open("vocabulary4.pickle", "wb") as file:
        pickle.dump(b2, file)