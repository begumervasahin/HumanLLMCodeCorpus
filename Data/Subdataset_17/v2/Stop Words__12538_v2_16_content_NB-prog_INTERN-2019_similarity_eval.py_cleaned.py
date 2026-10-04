import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
def load_all_embeddings():
    input_idx2vec, word2idx, idx2word, vocab = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
    output_idx2vec, _, _, _ = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
    return input_idx2vec, output_idx2vec, word2idx, idx2word, vocab
def cosine_similarity(vec1, vec2):
    return 1 - spatial.distance.cosine(vec1, vec2)
def cosine_similarity_words(word1, word2, idx2vec, word2idx):
    vec1 = idx2vec[word2idx[word1]]
    vec2 = idx2vec[word2idx[word2]]
    return cosine_similarity(vec1, vec2)
def calculate_similarity(sim_dir, idx2vec, word2idx, vocab):
    table = PrettyTable(['File Name', 'Rho', 'Total', 'Missing'])
    for filename in os.listdir(sim_dir):
        with open(os.path.join(sim_dir, filename), 'r') as file:
            lines = file.read().strip().split('\n')
        actual_similarities = []
        calculated_similarities = []
        missing_count = 0
        for line in lines:
            word1, word2, actual_similarity = line.split()
            if word1 in vocab and word2 in vocab:
                actual_similarities.append(float(actual_similarity))
                calculated_similarities.append(cosine_similarity_words(word1, word2, idx2vec, word2idx))
            else:
                missing_count += 1
        rho, _ = spearmanr(calculated_similarities, actual_similarities)
        table.add_row([filename, round(rho, 4), len(lines), missing_count])
    print(table)
def main():
    input_idx2vec, output_idx2vec, word2idx, idx2word, vocab = load_all_embeddings()
    print('\nResults of input embeddings:')
    calculate_similarity(os.path.join('evaluation data', 'similarity'), input_idx2vec, word2idx, vocab)
    print('\nResults of output embeddings:')
    calculate_similarity(os.path.join('evaluation data', 'similarity'), output_idx2vec, word2idx, vocab)
if __name__ == "__main__":
    main()