import os
import numpy as np
import pandas as pd
from torchtext.vocab import GloVe
def process_text(text, glove_embeddings, vocab, max_length=50):
    words = text.split()
    words = [word for word in words if word in vocab]
    if len(words) > max_length:
        words = words[:max_length]
    else:
        words.extend([" "] * (max_length - len(words)))
    word_vectors = np.array([glove_embeddings.get_vecs_by_tokens(word).numpy() for word in words]).ravel()
    return word_vectors
def save_processed_data(train_data, test_data, train_labels, test_labels):
    np.save("./db_pedia_train_data.npy", train_data.values)
    np.save("./db_pedia_test_data.npy", test_data.values)
    np.save("./db_pedia_train_label.npy", train_labels.values)
    np.save("./db_pedia_test_label.npy", test_labels.values)
def generate_db_pedia_dataset(path="./"):
    print("Start reading files")
    train_data = pd.read_csv(os.path.join(path, "train1.csv"), header=None)
    test_data = pd.read_csv(os.path.join(path, "test1.csv"), header=None)
    print("Files read successfully")
    train_data['text'] = train_data[1] + train_data[2]
    test_data['text'] = test_data[1] + test_data[2]
    glove = GloVe(name='6B', dim=50)
    vocab = set(glove.itos)
    print("Start processing files")
    train_data['processed_text'] = train_data['text'].apply(lambda text: process_text(text, glove, vocab))
    test_data['processed_text'] = test_data['text'].apply(lambda text: process_text(text, glove, vocab))
    print("Files processed successfully")
    train_labels = train_data[0].copy()
    test_labels = test_data[0].copy()
    print("Start saving files")
    save_processed_data(train_data['processed_text'], test_data['processed_text'], train_labels, test_labels)
    print("Files saved successfully")
if __name__ == "__main__":
    generate_db_pedia_dataset("./db_pedia/")