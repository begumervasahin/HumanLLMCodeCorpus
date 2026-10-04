import os
import numpy as np
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
input_idx2vec, word2idx, idx2word, vocab = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
output_idx2vec, _, _, _ = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
def cosine_similarity(vector_a, vector_b):
    return 1 - cosine(vector_a, vector_b)
def word_cosine_similarity(word_a, word_b, embeddings):
    vector_a = embeddings[word2idx[word_a]]
    vector_b = embeddings[word2idx[word_b]]
    return cosine_similarity(vector_a, vector_b)
def calculate_similarity(similarity_directory, embeddings):
    table = PrettyTable(['File Name', 'Rho', 'Total', 'Missing'])
    for filename in os.listdir(similarity_directory):
        file_path = os.path.join(similarity_directory, filename)
        with open(file_path, 'r') as file:
            lines = file.read().strip().split('\n')
        actual_similarities = []
        calculated_similarities = []
        missing_count = 0
        for line in lines:
            word1, word2, actual_similarity = line.split()
            if word1 in vocab and word2 in vocab:
                actual_similarities.append(float(actual_similarity))
                calculated_similarity = word_cosine_similarity(word1, word2, embeddings)
                calculated_similarities.append(calculated_similarity)
            else:
                missing_count += 1
        rho, _ = spearmanr(calculated_similarities, actual_similarities)
        table.add_row([filename, round(rho, 4), len(lines), missing_count])
    print(table)
print('\nResults of input embeddings:')
calculate_similarity(os.path.join('evaluation data', 'similarity'), input_idx2vec)
print('\nResults of output embeddings:')
calculate_similarity(os.path.join('evaluation data', 'similarity'), output_idx2vec)