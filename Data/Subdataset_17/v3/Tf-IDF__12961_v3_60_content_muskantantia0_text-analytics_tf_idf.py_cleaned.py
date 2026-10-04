import re
import string
import pandas as pd
from math import log
def load_data(file_path):
    return pd.read_csv(file_path)
def preprocess_document(doc):
    doc = doc.lower()
    doc = re.sub(f'[{re.escape(string.punctuation)}]', '', doc)
    return doc.split()
def preprocess_documents(documents):
    return [preprocess_document(doc) for doc in documents]
def flatten_term_vectors(term_vectors):
    return [word for term_vector in term_vectors for word in term_vector]
def calculate_word_frequencies(word_list):
    word_freq = {word: word_list.count(word) for word in set(word_list)}
    total_words = len(word_list)
    freq_list = [
        (word, freq, round(log(total_words / freq, 10), 4), freq * round(log(total_words / freq, 10), 4))
        for word, freq in word_freq.items()
    ]
    return sorted(freq_list, key=lambda x: x[1], reverse=True)
def main():
    data = load_data('tf_idf.csv')
    documents = data['title'].tolist()
    term_vectors = preprocess_documents(documents)
    word_list = flatten_term_vectors(term_vectors)
    finals = calculate_word_frequencies(word_list)
    print(f"Number of documents: {len(documents)}")
    print(f"Number of words: {len(word_list)}")
    print("Word frequencies and metrics:")
    for item in finals:
        print(item)
if __name__ == "__main__":
    main()