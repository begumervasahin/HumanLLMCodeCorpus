import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
class class1:
    def fonk1(self):
        pass
    def fonk2(self, folder):
        b1 = glob.glob(folder + "*.txt")
        b2 = {}
        for filename in b1:
            with open(filename) as f:
                b3 = f.readlines()
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
    def fonk3(self, old_vocab, new_vocab):
        for b5, count in new_vocab.items():
            if b5 in old_vocab:
                old_vocab[b5] += count
            else:
                old_vocab[b5] = count
        return old_vocab
    def fonk4(self, b2):
        b6 = set(stopwords.b4('english'))
        for b5 in b6:
            b2.pop(b5, None)
        return b2
    def fonk5(self, b2):
        b7 = WordNetLemmatizer()
        for b5 in list(b2.keys()):
            b8 = b7.fonk5(b5)
            if b8 != b5:
                try:
                    b2[b8] += b2[b5]
                except KeyError:
                    pass
                b2.pop(b5)
        return b2
    def fonk6(self, b2, percentile):
        b9 = np.percentile(list(b2.values()), percentile)
        b10 = np.percentile(list(b2.values()), 100 - percentile)
        b2 = {key: value for key, value in b2.items() if b9 < value < b10}
        return b2
if b11 = = '__main__':
    b12 = class1()
    b2 = {}
    for i in range(1, 11):
        b2 = b12.fonk3(b2, b12.fonk2("lingspam/part" + str(i) + "/"))
    with open("vocabulary1.pickle", "wb") as f:
        pickle.dump(b2, f)
    b2 = b12.fonk4(b2)
    with open("vocabulary2.pickle", "wb") as f:
        pickle.dump(b2, f)
    b2 = b12.fonk5(b2)
    with open("vocabulary3.pickle", "wb") as f:
        pickle.dump(b2, f)
    b2 = b12.fonk6(b2, 2)
    with open("vocabulary4.pickle", "wb") as f:
        pickle.dump(b2, f)