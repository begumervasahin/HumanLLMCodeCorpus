import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
def cosine_similarity(a, b):
    return 1 - spatial.distance.cosine(a, b)
def cosine_similarity_words(word1, word2, idx2vec):
    vec1 = idx2vec[word2idx[word1]]
    vec2 = idx2vec[word2idx[word2]]
    return cosine_similarity(vec1, vec2)
def calculate_similarity(similarity_directory, idx2vec):
    result_table = PrettyTable(['File Name', 'Spearman Rho', 'Total Pairs', 'Missing Pairs'])
    for filename in os.listdir(similarity_directory):
        lines = open(os.path.join(similarity_directory, filename), 'r').read().strip().split('\n')
        actual_scores = []
        calculated_scores = []
        missing_pairs = 0
        for line in lines:
            word1, word2, actual_similarity = line.split()
            if word1 in vocab and word2 in vocab:
                actual_scores.append(float(actual_similarity))
                calculated_similarity = cosine_similarity_words(word1, word2, idx2vec)
                calculated_scores.append(calculated_similarity)
            else:
                missing_pairs += 1
        spearman_rho = round(spearmanr(calculated_scores, actual_scores)[0], 4)
        result_table.add_row([filename, spearman_rho, len(lines), missing_pairs])
    print(result_table)
if __name__ == "__main__":
    input_idx2vec, word2idx, idx2word, vocab = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
    output_idx2vec, _, _, _ = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
    print('\nResults of input embeddings:')
    calculate_similarity(os.path.join('evaluation data', 'similarity'), input_idx2vec)
    print('\nResults of output embeddings:')
    calculate_similarity(os.path.join('evaluation data', 'similarity'), output_idx2vec)