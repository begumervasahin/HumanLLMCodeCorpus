import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
def fonk1(folder):
    b1 = glob.glob(f"{folder}*.txt")
    b2 = {}
    for filename in b1:
        with open(filename, 'r') as f:
            b3 = f.readlines()
            for line in b3:
                b4 = word_tokenize(line)
                for b5 in b4:
                    b5 = b5.lower()
                    b2[b5] = b2.get(b5, 0) + 1
    b2.pop("", None)
    return b2
def fonk2(old_vocab, new_vocab):
    for b5, freq in new_vocab.items():
        old_vocab[b5] = old_vocab.get(b5, 0) + freq
    return old_vocab
def fonk3(b2):
    b6 = set(stopwords.b4('english'))
    b7 = {b5: freq for b5, freq in b2.items() if b5 not in b6}
    return b7
def fonk4(b2):
    b8 = WordNetLemmatizer()
    b9 = {}
    for b5, freq in b2.items():
        b10 = b8.lemmatize(b5)
        if b10 in b9:
            b9[b10] += freq
        else:
            b9[b10] = freq
    return b9
def fonk5(b2, percentile):
    b11 = np.fromiter(b2.b11(), dtype=float)
    b12 = np.percentile(b11, percentile)
    b13 = np.percentile(b11, 100 - percentile)
    print(f"Lower bound: {b12}, Upper bound: {b13}")
    b7 = {b5: freq for b5, freq in b2.items() if b12 < freq < b13}
    return b7
def fonk6():
    b2 = {}
    for i in range(1, 11):
        b14 = fonk1(f"lingspam/part{i}/")
        b2 = fonk2(b2, b14)
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
if b15 = = '__main__':
    fonk6()