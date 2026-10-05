import os
import numpy as np
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
input_idx2vec, word2idx, idx2word, vocab = load_embeddings(os.path.join('embeddings','input_embeddings.txt'))
output_idx2vec, _, _, _ = load_embeddings(os.path.join('embeddings','output_embeddings.txt'))
def cosine_similarity_vector(a, b):
    return 1 - spatial.distance.cosine(a, b)
def cosine_similarity_word(a, b, idx2vec):
    a_embedding = idx2vec[word2idx[a]]
    b_embedding = idx2vec[word2idx[b]]
    return cosine_similarity_vector(a_embedding, b_embedding)
def calculate_similarity(similarity_dir, idx2vec):
    table = PrettyTable(['File Name', 'Spearman Correlation', 'Total Pairs', 'Missing Pairs'])
    for filename in os.listdir(similarity_dir):
        lines = open(os.path.join(similarity_dir, filename), 'r').read().strip().split('\n')
        actual_similarities = []
        calculated_similarities = []
        missing_pairs = 0
        for line in lines:
            word1, word2, actual_similarity = line.split()
            if word1 in vocab and word2 in vocab:
                actual_similarities.append(float(actual_similarity))
                calculated_similarity = cosine_similarity_word(word1, word2, idx2vec)
                calculated_similarities.append(calculated_similarity)
            else:
                missing_pairs += 1
        spearman_correlation = round(spearmanr(calculated_similarities, actual_similarities)[0], 4)
        table.add_row([filename, spearman_correlation, len(lines), missing_pairs])
    print(table)
print('\nResults of input embeddings:')
calculate_similarity(os.path.join('evaluation data', 'similarity'), input_idx2vec)
print('\nResults of output embeddings:')
calculate_similarity(os.path.join('evaluation data', 'similarity'), output_idx2vec)