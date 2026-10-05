import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy as np
import sys
ham_train, spam_train, ham_test, spam_test = sys.argv[1:5]
Lamda, iteration, learning_rate = map(float, sys.argv[5:8])
ham_train_files = glob.glob(f"{ham_train}/*.txt")
spam_train_files = glob.glob(f"{spam_train}/*.txt")
ham_test_files = glob.glob(f"{ham_test}/*.txt")
spam_test_files = glob.glob(f"{spam_test}/*.txt")
def preprocess_text(filename, remove_stopwords=True):
    text = ""
    for file_name in filename:
        with open(file_name, 'r') as file:
            text += file.read()
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    translator = str.maketrans('', '', string.digits)
    text = text.translate(translator)
    word_count = Counter(text.split())
    if remove_stopwords:
        word_count = Counter([word for word in word_count if word not in stopwords.words('english')])
    return word_count
def filter_words(word_counts, min_count=2):
    return Counter({word: count for word, count in word_counts.items() if count >= min_count})
def create_feature_matrix(remove_stopwords):
    spam_word_counts = preprocess_text(spam_train_files, remove_stopwords)
    bag_of_words = filter_words(spam_word_counts, min_count=2)
    feature_matrix = []
    for file_name in ham_train_files + spam_train_files:
        feature = {}
        with open(file_name, 'r') as file:
            file_text = file.read().split(" ")
            file_word_counts = Counter(file_text)
            for word in bag_of_words:
                feature[word] = file_word_counts[word]
            feature["Probability_of_class"] = 0.0 if "ham" in file_name else 1.0
            feature_matrix.append(feature)
    return feature_matrix, bag_of_words
def calculate_class_probability(w0, weights, feature_matrix):
    for feature in feature_matrix:
        sum_p = sum(weights[word] * feature[word] for word in weights)
        prob = np.exp(w0 + sum_p) / (1 + np.exp(w0 + sum_p)) if sum_p < 700 else 1.0
        feature["Probability_of_class"] = prob
    return feature_matrix
def update_weights(weights, learning_rate, Lamda, feature_matrix):
    for word in weights:
        weight_sum = sum(feature[word] * (feature["Probability_of_class"] - feature["Class_of_file"]) for feature in feature_matrix)
        weights[word] += learning_rate * weight_sum - learning_rate * Lamda * weights[word]
    return weights
def calculate_accuracy(weights):
    correct_count = 0
    total_count = 0
    for file_name in spam_test_files:
        with open(file_name, 'r') as file:
            file_text = file.read().split(" ")
            file_word_counts = Counter(file_text)
            sum_p = sum(weights[word] * file_word_counts[word] for word in weights)
            prob = np.exp(1 + sum_p) / (1 + np.exp(1 + sum_p)) if sum_p < 700 else 1.0
            if prob > 0.9:
                correct_count += 1
            total_count += 1
    for file_name in ham_test_files:
        with open(file_name, 'r') as file:
            file_text = file.read().split(" ")
            file_word_counts = Counter(file_text)
            sum_p = sum(weights[word] * file_word_counts[word] for word in weights)
            prob = np.exp(1 + sum_p) / (1 + np.exp(1 + sum_p)) if sum_p < 700 else 1.0
            if prob < 0.9:
                correct_count += 1
            total_count += 1
    return correct_count / total_count
def logistic_regression(iterations, learning_rate, Lamda, remove_stopwords):
    feature_matrix, bag_of_words = create_feature_matrix(remove_stopwords)
    w0 = 1.0
    weights = {word: 1.0 for word in bag_of_words}
    feature_matrix = calculate_class_probability(w0, weights, feature_matrix)
    for _ in range(iterations):
        weights = update_weights(weights, learning_rate, Lamda, feature_matrix)
        feature_matrix = calculate_class_probability(w0, weights, feature_matrix)
    final_accuracy = calculate_accuracy(weights)
    print(f"Logistic Regression - {'filtered' if remove_stopwords else 'unfiltered'} - Total Accuracy - {final_accuracy * 100:.2f}")
logistic_regression(iteration, learning_rate, Lamda, remove_stopwords=False)
logistic_regression(iteration, learning_rate, Lamda, remove_stopwords=True)