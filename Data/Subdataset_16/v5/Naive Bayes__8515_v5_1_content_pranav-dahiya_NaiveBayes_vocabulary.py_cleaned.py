import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
def fonk1(b14):
    b1 = glob.glob(b14 + "*.txt")
    b2 = {}
    for filename in b1:
        with open(filename, 'r') as file:
            b3 = file.readlines()
            for line in b3:
                b4 = word_tokenize(line)
                for b5 in b4:
                    b5 = b5.lower()
                    if b5:
                        b2[b5] = b2.get(b5, 0) + 1
    return b2
def fonk2(old_vocab, new_vocab):
    for b5, count in new_vocab.items():
        old_vocab[b5] = old_vocab.get(b5, 0) + count
    return old_vocab
def fonk3(b2):
    b6 = set(stopwords.b4('english'))
    for b5 in b6:
        b2.pop(b5, None)
    return b2
def fonk4(b2):
    b7 = WordNetLemmatizer()
    b8 = {}
    for b5, count in b2.items():
        b9 = b7.lemmatize(b5)
        if b9 in b8:
            b8[b9] += count
        else:
            b8[b9] = count
    return b8
def fonk5(b2, percentile):
    b10 = np.array(list(b2.b10()))
    b11 = np.percentile(b10, percentile)
    b12 = np.percentile(b10, 100 - percentile)
    print(f"Lower bound: {b11}, Upper bound: {b12}")
    b13 = {b5: count for b5, count in b2.items() if b11 < count < b12}
    return b13
def fonk6(b2, filename):
    with open(filename, "wb") as file:
        pickle.dump(b2, file)
def fonk7():
    b2 = {}
    for i in range(1, 11):
        b14 = f"lingspam/part{i}/"
        b2 = fonk2(b2, fonk1(b14))
    fonk6(b2, "vocabulary1.pickle")
    b2 = fonk3(b2)
    fonk6(b2, "vocabulary2.pickle")
    b2 = fonk4(b2)
    fonk6(b2, "vocabulary3.pickle")
    b2 = fonk5(b2, 2)
    fonk6(b2, "vocabulary4.pickle")
if b15 = = '__main__':
    fonk7()