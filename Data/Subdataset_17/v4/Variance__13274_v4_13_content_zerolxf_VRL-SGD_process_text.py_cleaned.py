import os
import sys
import numpy as np
import pandas as pd
from torchtext.vocab import Vectors, GloVe
import re
from gensim.models import word2vec
sys.path.append('../')
def process_text(origin_text, glove_vectors, vocab, fix_length=50):
    words = origin_text.split()
    words = [word for word in words if word in vocab]
    if len(words) > fix_length:
        words = words[:fix_length]
    else:
        words += [" "] * (fix_length - len(words))
    word_vectors = np.array([glove_vectors.get_vecs_by_tokens(word).numpy() for word in words]).ravel()
    return word_vectors
def save_to_files(train_data, test_data, train_labels, test_labels):
    np.save("./db_pedia_train_data.npy", train_data.values)
    np.save("./db_pedia_test_data.npy", test_data.values)
    np.save("./db_pedia_train_labels.npy", train_labels.values)
    np.save("./db_pedia_test_labels.npy", test_labels.values)
def generate_db_pedia_data(path="./"):
    print("Start reading files...")
    train_data = pd.read_csv(os.path.join(path, "train1.csv"), header=None)
    test_data = pd.read_csv(os.path.join(path, "test1.csv"), header=None)
    print("File reading complete.")
    train_data['combined_text'] = train_data[1] + " " + train_data[2]
    test_data['combined_text'] = test_data[1] + " " + test_data[2]
    glove = GloVe(name='6B', dim=50)
    vocab = set(glove.itos)
    print("Start processing files...")
    train_vectors = train_data['combined_text'].apply(lambda text: process_text(text, glove, vocab))
    test_vectors = test_data['combined_text'].apply(lambda text: process_text(text, glove, vocab))
    print("File processing complete.")
    train_labels = train_data[0].copy()
    test_labels = test_data[0].copy()
    print("Start saving files...")
    save_to_files(train_vectors, test_vectors, train_labels, test_labels)
    print("File saving complete.")
generate_db_pedia_data("./db_pedia/")