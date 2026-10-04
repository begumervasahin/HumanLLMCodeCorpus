import os
import sys
import numpy as np
import pandas as pd
from torchtext.b8 import GloVe
sys.b4.append('../')
def fonk1(text, glove_vectors, b8, b1 = 50):
    b2 = text.split()
    b2 = [word for word in b2 if word in b8]
    if len(b2) > b1:
        b2 = b2[:b1]
    else:
        b2.extend([" "] * (b1 - len(b2)))
    b3 = np.array([glove_vectors.get_vecs_by_tokens(word).numpy() for word in b2]).ravel()
    return b3
def fonk2(b5, b6, b11, b12):
    np.save("./db_pedia_train_data.npy", b5.values)
    np.save("./db_pedia_test_data.npy", b6.values)
    np.save("./db_pedia_train_labels.npy", b11.values)
    np.save("./db_pedia_test_labels.npy", b12.values)
def fonk3(b4 = "./"):
    print("Start reading files...")
    b5 = pd.read_csv(os.b4.join(b4, "train1.csv"), header=None)
    b6 = pd.read_csv(os.b4.join(b4, "test1.csv"), header=None)
    print("File reading complete.")
    b5['combined_text'] = b5[1] + " " + b5[2]
    b6['combined_text'] = b6[1] + " " + b6[2]
    b7 = GloVe(name='6B', dim=50)
    b8 = set(b7.itos)
    print("Start processing files...")
    b9 = b5['combined_text'].apply(lambda text: fonk1(text, b7, b8))
    b10 = b6['combined_text'].apply(lambda text: fonk1(text, b7, b8))
    print("File processing complete.")
    b11 = b5[0].copy()
    b12 = b6[0].copy()
    print("Start saving files...")
    fonk2(b9, b10, b11, b12)
    print("File saving complete.")
fonk3("./db_pedia/")