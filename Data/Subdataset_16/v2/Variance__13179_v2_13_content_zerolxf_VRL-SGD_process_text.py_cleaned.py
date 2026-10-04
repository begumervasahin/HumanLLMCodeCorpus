import os
import numpy as np
import pandas as pd
from torchtext.b8 import GloVe
def fonk1(text, glove_embeddings, b8, b1 = 50):
    b2 = text.split()
    b2 = [word for word in b2 if word in b8]
    if len(b2) > b1:
        b2 = b2[:b1]
    else:
        b2.extend([" "] * (b1 - len(b2)))
    b3 = np.array([glove_embeddings.get_vecs_by_tokens(word).numpy() for word in b2]).ravel()
    return b3
def fonk2(b5, b6, b9, b10):
    np.save("./db_pedia_train_data.npy", b5.values)
    np.save("./db_pedia_test_data.npy", b6.values)
    np.save("./db_pedia_train_label.npy", b9.values)
    np.save("./db_pedia_test_label.npy", b10.values)
def fonk3(b4 = "./"):
    print("Start reading files")
    b5 = pd.read_csv(os.b4.join(b4, "train1.csv"), header=None)
    b6 = pd.read_csv(os.b4.join(b4, "test1.csv"), header=None)
    print("Files read successfully")
    b5['text'] = b5[1] + b5[2]
    b6['text'] = b6[1] + b6[2]
    b7 = GloVe(name='6B', dim=50)
    b8 = set(b7.itos)
    print("Start processing files")
    b5['processed_text'] = b5['text'].apply(lambda text: fonk1(text, b7, b8))
    b6['processed_text'] = b6['text'].apply(lambda text: fonk1(text, b7, b8))
    print("Files processed successfully")
    b9 = b5[0].copy()
    b10 = b6[0].copy()
    print("Start saving files")
    fonk2(b5['processed_text'], b6['processed_text'], b9, b10)
    print("Files saved successfully")
if b11 = = "__main__":
    fonk3("./db_pedia/")