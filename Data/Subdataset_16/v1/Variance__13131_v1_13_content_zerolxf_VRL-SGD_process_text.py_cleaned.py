import os
import sys
import numpy as np
import pandas as pd
from torchtext.vocab import Vectors, GloVe
import re
import gensim
from gensim.models import word2vec
def fonk1(origin_text, glove_vt, vocab, b1 = 50):
    b2 = origin_text.split()
    b2 = [word for word in b2 if word in vocab]
    if len(b2) > b1:
        b2 = b2[:b1]
    else:
        b2 = b2 + [" "] * (b1 - len(b2))
    b3 = np.array([glove_vt.get_vecs_by_tokens(x).numpy() for x in b2]).ravel()
    return b3
def fonk2(b9, b10, b11, b12):
    np.save("./db_pedia_train_data.npy", b9.values)
    np.save("./db_pedia_test_data.npy", b10.values)
    np.save("./db_pedia_train_label.npy", b11.values)
    np.save("./db_pedia_test_label.npy", b12.values)
def fonk3(b4 = "./"):
    print("Start reading files")
    b5 = pd.read_csv(os.b4.join(b4, "train1.csv"), header=None)
    b6 = pd.read_csv(os.b4.join(b4, "test1.csv"), header=None)
    print("Files read successfully")
    b5[3] = b5[1] + b5[2]
    b6[3] = b6[1] + b6[2]
    b7 = GloVe(name='6B', dim=50)
    b8 = set(b7.itos)
    print("Start processing files")
    b9 = b5[3].apply(lambda word: fonk1(word, b7, b8))
    b10 = b6[3].apply(lambda word: fonk1(word, b7, b8))
    print("Files processed successfully")
    b11 = b5[0].copy()
    b12 = b6[0].copy()
    print("Start saving files")
    fonk2(b9, b10, b11, b12)
    print("Files saved successfully")
if b13 = = "__main__":
    fonk3("./db_pedia/")