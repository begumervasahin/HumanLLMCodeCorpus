import os
from scipy import spatial
from scipy.stats import spearmanr
from prettytable import PrettyTable
from DataHandler import load_embeddings
input_embeddings, input_word2idx, _, input_vocab = load_embeddings(os.path.join('embeddings', 'input_embeddings.txt'))
output_embeddings, _, _, output_vocab = load_embeddings(os.path.join('embeddings', 'output_embeddings.txt'))
def calculate_cosine_similarity(a, b):
    return 1 - spatial.distance.cosine(a, b)
def calculate_word_similarity(word1, word2, embeddings, word2idx):
    if word1 in word2idx and word2 in word2idx:
        embedding1 = embeddings[word2idx[word1]]
        embedding2 = embeddings[word2idx[word2]]
        return calculate_cosine_similarity(embedding1, embedding2)
    else:
        return None
def calculate_similarity_scores(similarity_dir, embeddings, vocab, word2idx):
    table = PrettyTable(['File Name', 'Spearman Correlation', 'Total Pairs', 'Missing Pairs'])
    for filename in os.listdir(similarity_dir):
        lines = open(os.path.join(similarity_dir, filename), 'r').read().strip().split('\n')
        actual_similarities = []
        calculated_similarities = []
        missing_pairs = 0
        for line in lines:
            word1, word2, actual_similarity = line.split()
            actual_similarity = float(actual_similarity)
            similarity = calculate_word_similarity(word1, word2, embeddings, word2idx)
            if similarity is not None:
                actual_similarities.append(actual_similarity)
                calculated_similarities.append(similarity)
            else:
                missing_pairs += 1
        spearman_correlation = round(spearmanr(calculated_similarities, actual_similarities)[0], 4)
        table.add_row([filename, spearman_correlation, len(lines), missing_pairs])
    print(table)
print('\nResults of input embeddings:')
calculate_similarity_scores(os.path.join('evaluation data', 'similarity'), input_embeddings, input_vocab, input_word2idx)
print('\nResults of output embeddings:')
calculate_similarity_scores(os.path.join('evaluation data', 'similarity'), output_embeddings, output_vocab, input_word2idx)