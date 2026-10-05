import os
import numpy as np
from scipy.spatial.distance import cdist
from prettytable import PrettyTable
from DataHandler import load_embeddings
INPUT_EMBEDDINGS_PATH = os.path.join('embeddings', 'input_embeddings.txt')
OUTPUT_EMBEDDINGS_PATH = os.path.join('embeddings', 'output_embeddings.txt')
ANALOGY_FILE_PATH = os.path.join('evaluation data', 'analogy', 'EN-GOOGLE.txt')
input_idx2vec, word2idx, idx2word, vocab = load_embeddings(INPUT_EMBEDDINGS_PATH)
output_idx2vec, _, _, _ = load_embeddings(OUTPUT_EMBEDDINGS_PATH)
input_idx2vec = input_idx2vec / np.linalg.norm(input_idx2vec, axis=1, keepdims=True)
output_idx2vec = output_idx2vec / np.linalg.norm(output_idx2vec, axis=1, keepdims=True)
def words_to_idxs(words_list):
    return [word2idx[word] for word in words_list]
def split_into_batches(questions, batch_size):
    if batch_size >= len(questions):
        return [questions]
    batches = []
    for i in range(0, len(questions), batch_size):
        batches.append(questions[i:i + batch_size])
    return batches
def load_analogy_questions(file_path):
    lines = open(file_path, "r").read().strip().split('\n')
    analogy_questions = []
    category = None
    for line in lines:
        if line.startswith(":"):
            category = line.lower().split()[1]
        else:
            words = line.split()
            analogy_questions.append((category, words[0], words[1], words[2], words[3]))
    all_categories = set(question[0] for question in analogy_questions)
    syn_categories = {category for category in all_categories if category.startswith('gram')}
    sem_categories = all_categories - syn_categories
    syn_questions = [question[1:] for question in analogy_questions if question[0] in syn_categories]
    sem_questions = [question[1:] for question in analogy_questions if question[0] in sem_categories]
    return syn_questions, sem_questions
syn_questions, sem_questions = load_analogy_questions(ANALOGY_FILE_PATH)
questions = {'Syntactic': syn_questions, 'Semantic': sem_questions}
def calculate_analogy_accuracy(questions, embeddings, batch_size=1000):
    table = PrettyTable(['Category', 'Accuracy', 'Total Questions', 'Missing Words'])
    for category, cat_questions in questions.items():
        missing = 0
        filtered_questions = []
        for question in cat_questions:
            if all(word in vocab for word in question):
                filtered_questions.append(question)
            else:
                missing += 1
        predicted_labels = []
        ground_truth_labels = []
        for batch in split_into_batches(filtered_questions, batch_size):
            batch = np.array(batch)
            word1, word2, word3, word4 = batch[:, 0], batch[:, 1], batch[:, 2], batch[:, 3]
            word1_idxs = words_to_idxs(word1)
            word2_idxs = words_to_idxs(word2)
            word3_idxs = words_to_idxs(word3)
            word4_idxs = words_to_idxs(word4)
            word1_vecs = embeddings[word1_idxs]
            word2_vecs = embeddings[word2_idxs]
            word3_vecs = embeddings[word3_idxs]
            d_vecs = word2_vecs - word1_vecs + word3_vecs
            similarities = 1 - cdist(d_vecs, embeddings, 'cosine')
            similarities[:, 0] = -1
            predicted_labels.extend(np.argmax(similarities, axis=1))
            ground_truth_labels.extend(word4_idxs)
        ground_truth_labels = np.array(ground_truth_labels)
        predicted_labels = np.array(predicted_labels)
        correct_predictions = (predicted_labels == ground_truth_labels)
        accuracy = round(np.sum(correct_predictions) / len(correct_predictions) * 100, 2)
        table.add_row([category, accuracy, len(cat_questions), missing])
    print(table)
print('\nResults of input embeddings:')
calculate_analogy_accuracy(questions, input_idx2vec, batch_size=1000)
print('\nResults of output embeddings:')
calculate_analogy_accuracy(questions, output_idx2vec, batch_size=1000)