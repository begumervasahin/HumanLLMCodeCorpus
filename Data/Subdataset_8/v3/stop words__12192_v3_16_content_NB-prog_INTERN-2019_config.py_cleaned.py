import os
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
class SkipGram:
    def __init__(self, corpus_file, max_vocab_size, max_corpus_size, fw_subsampling_th,
                 embedding_dims, neg_samples, epochs, mini_batch_size, window_size,
                 cont_training, words_to_plot):
        self.corpus_file = corpus_file
        self.max_vocab_size = max_vocab_size
        self.max_corpus_size = max_corpus_size
        self.fw_subsampling_th = fw_subsampling_th
        self.embedding_dims = embedding_dims
        self.neg_samples = neg_samples
        self.epochs = epochs
        self.mini_batch_size = mini_batch_size
        self.window_size = window_size
        self.cont_training = cont_training
        self.words_to_plot = words_to_plot
        self.vocab = {}
        self.word_freq = None
    def preprocess_corpus(self):
        with open(self.corpus_file, 'r', encoding='utf-8') as file:
            corpus = file.read().split()
        if len(corpus) > self.max_corpus_size:
            corpus = corpus[:int(self.max_corpus_size)]
        self.word_freq = Counter(corpus)
        if self.fw_subsampling_th:
            corpus = [word for word in corpus if np.random.rand() < self.discard_probability(word)]
        vocab_count = Counter(corpus).most_common(self.max_vocab_size)
        self.vocab = {word: idx for idx, (word, _) in enumerate(vocab_count)}
        self.word_freq = {word: freq for word, freq in self.word_freq.items() if word in self.vocab}
    def discard_probability(self, word):
        if self.fw_subsampling_th:
            return 1 - (self.fw_subsampling_th / self.word_freq[word]) ** 0.5
        else:
            return 0
    def train_skipgram(self):
        pass
    def plot_word_embeddings(self):
        pass
    def train_and_plot(self):
        self.preprocess_corpus()
        self.train_skipgram()
        self.plot_word_embeddings()
if __name__ == "__main__":
    config = {
        "corpus_file": 'corpus.txt',
        "max_vocab_size": 50000,
        "max_corpus_size": 1e12,
        "fw_subsampling_th": None,
        "embedding_dims": 50,
        "neg_samples": 20,
        "epochs": 3,
        "mini_batch_size": 256,
        "window_size": 5,
        "cont_training": False,
        "words_to_plot": 1000
    }
    skipgram_model = SkipGram(**config)
    skipgram_model.train_and_plot()