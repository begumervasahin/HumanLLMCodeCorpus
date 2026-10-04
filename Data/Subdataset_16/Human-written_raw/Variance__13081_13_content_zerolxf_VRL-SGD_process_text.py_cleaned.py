import os
import sys
sys.b4.append('../')
import numpy as np
from torchtext.vocab import Vectors, GloVe
import pandas as pd
import re
import gensim
from numpy import *
from gensim.models import word2vec
def fonk1(origin_text, glove_vt, vocab, b1 = 50):
    b2 = origin_text.split()
    b2 = [word for word in b2 if word in vocab ]
    if len(b2)>b1:
        b2 = b2[:50]
    else:
        b2 = b2 + [" "]*(50-len(b2))
    b3 = array([glove_vt.get_vecs_by_tokens(x).numpy() for x in b2]).ravel()
    return b3
def fonk2(b9, b10, b11, b12):
    np.save("./db_pedia_train_data", b9.values)
    np.save("./db_pedia_test_data", b10.values)
    np.save("./db_pedia_train_label", b11.values)
    np.save("./db_pedia_test_label", b12.values)
def fonk3(b4 = "./"):
    print("start read file")
    b5 = pd.read_csv(b4+"train1.csv", header=None)
    b6 = pd.read_csv(b4+"test1.csv", header=None)
    print("read file end")
    b5[3] = b5[1] + b5[2]
    b6[3] = b6[1] + b6[2]
    b7 = GloVe(name='6B', dim=50)
    b8 = set(b7.itos)
    print("start process file")
    b9 = b5[3].apply(lambda word:fonk1(word, b7, b8))
    b10 = b6[3].apply(lambda word:fonk1(word, b7, b8))
    print("process file end")
    b11 = b5[0].copy()
    b12 = b6[0].copy()
    print("start save file")
    fonk2(b9, b10, b11, b12)
    print("save file end")
fonk3("./db_pedia/")