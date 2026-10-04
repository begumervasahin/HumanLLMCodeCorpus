import os
import sys
import numpy as np
import pandas as pd
from torchtext.vocab import Vectors, GloVe
import re
import gensim
from gensim.models import word2vec
def process(origin_text, glove_vt, vocab, fix_length=50):
    words = origin_text.split()
    words = [word for word in words if word in vocab]
    if len(words) > fix_length:
        words = words[:fix_length]
    else:
        words = words + [" "] * (fix_length - len(words))
    word_vect = np.array([glove_vt.get_vecs_by_tokens(x).numpy() for x in words]).ravel()
    return word_vect
def save_file(train_data, test_data, train_label, test_label):
    np.save("./db_pedia_train_data.npy", train_data.values)
    np.save("./db_pedia_test_data.npy", test_data.values)
    np.save("./db_pedia_train_label.npy", train_label.values)
    np.save("./db_pedia_test_label.npy", test_label.values)
def generate_db_pedia(path="./"):
    print("Start reading files")
    db_train_data = pd.read_csv(os.path.join(path, "train1.csv"), header=None)
    db_test_data = pd.read_csv(os.path.join(path, "test1.csv"), header=None)
    print("Files read successfully")
    db_train_data[3] = db_train_data[1] + db_train_data[2]
    db_test_data[3] = db_test_data[1] + db_test_data[2]
    glove = GloVe(name='6B', dim=50)
    words_set = set(glove.itos)
    print("Start processing files")
    train_data = db_train_data[3].apply(lambda word: process(word, glove, words_set))
    test_data = db_test_data[3].apply(lambda word: process(word, glove, words_set))
    print("Files processed successfully")
    train_label = db_train_data[0].copy()
    test_label = db_test_data[0].copy()
    print("Start saving files")
    save_file(train_data, test_data, train_label, test_label)
    print("Files saved successfully")
if __name__ == "__main__":
    generate_db_pedia("./db_pedia/")