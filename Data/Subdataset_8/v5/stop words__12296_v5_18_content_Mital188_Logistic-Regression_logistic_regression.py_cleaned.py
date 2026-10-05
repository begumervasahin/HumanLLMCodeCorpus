import glob
import numpy as np
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
def read_files(filenames, stop_words):
    all_text = ""
    for file_name in filenames:
        with open(file_name) as file:
            all_text += file.read()
    translator = str.maketrans('', '', string.punctuation)
    all_text = all_text.translate(translator)
    translator = str.maketrans('', '', string.digits)
    all_text = all_text.translate(translator)
    word_counts = Counter(all_text.split())
    if stop_words:
        stop_words_set = set(stopwords.words('english'))
        word_counts = Counter({word: count for word, count in word_counts.items() if word not in stop_words_set})
    return word_counts
def slice_bag(bag_of_words, min_count):
    return Counter({word: count for word, count in bag_of_words.items() if count >= min_count})
def create_feature_matrix(ham_files, spam_files, bag_of_words):
    feature_matrix = []
    for file_name in ham_files:
        with open(file_name) as file:
            file_text = file.read().split()
            file_word_counts = Counter(file_text)
            feature = {word: file_word_counts[word] for word in bag_of_words}
            feature["Probability_of_class"] = 0.0
            feature["Class_of_file"] = 0
            feature_matrix.append(feature)
    for file_name in spam_files:
        with open(file_name) as file:
            file_text = file.read().split()
            file_word_counts = Counter(file_text)
            feature = {word: file_word_counts[word] for word in bag_of_words}
            feature["Probability_of_class"] = 0.0
            feature["Class_of_file"] = 1
            feature_matrix.append(feature)
    return feature_matrix
def calculate_class_probability(w0, weights, feature_matrix):
    for feature in feature_matrix:
        sum_product = sum(weights[word] * feature[word] for word in weights)
        prob = np.exp(w0 + sum_product) / (1 + np.exp(w0 + sum_product)) if sum_product < 700 else 1.0
        feature["Probability_of_class"] = prob
    return feature_matrix
def update_weights(weights, n, lam, feature_matrix):
    for word in weights:
        weight_update = sum(feature[word] * (feature["Class_of_file"] - feature["Probability_of_class"]) for feature in feature_matrix)
        weights[word] += n * weight_update - n * lam * weights[word]
    return weights
def calculate_accuracy(weights, spam_test_files, ham_test_files):
    count_right, count_total = 0, 0
    for file_name in spam_test_files + ham_test_files:
        with open(file_name) as file:
            file_text = file.read().split()
            file_word_counts = Counter(file_text)
            sum_product = sum(weights[word] * file_word_counts[word] for word in weights)
            prob = np.exp(1 + sum_product) / (1 + np.exp(1 + sum_product)) if sum_product < 700 else 1.0
            if (prob > 0.9 and "spam" in file_name) or (prob < 0.9 and "ham" in file_name):
                count_right += 1
            count_total += 1
    return count_right / count_total
def logistic_regression(iterations, n, lam, ham_train_path, spam_train_path, ham_test_files, spam_test_files, stop_words):
    ham_files = glob.glob(ham_train_path + "/*.txt")
    spam_files = glob.glob(spam_train_path + "/*.txt")
    all_files = ham_files + spam_files
    word_counts = read_files(all_files, stop_words)
    bag_of_words = slice_bag(word_counts, min_count=2)
    feature_matrix = create_feature_matrix(ham_files, spam_files, bag_of_words)
    w0 = 1.0
    initial_weights = {word: 1.0 for word in bag_of_words}
    feature_matrix = calculate_class_probability(w0, initial_weights, feature_matrix)
    weights = initial_weights
    for _ in range(iterations):
        weights = update_weights(weights, n, lam, feature_matrix)
        feature_matrix = calculate_class_probability(w0, weights, feature_matrix)
    final_accuracy = calculate_accuracy(weights, spam_test_files, ham_test_files)
    if stop_words:
        print("Logistic Regression - filtered - Total Accuracy - {:.2f}%".format(final_accuracy * 100))
    else:
        print("Logistic Regression - unfiltered - Total Accuracy - {:.2f}%".format(final_accuracy * 100))
ham_train_path = sys.argv[1]
spam_train_path = sys.argv[2]
ham_test_files = glob.glob(sys.argv[3] + "/*.txt")
spam_test_files = glob.glob(sys.argv[4] + "/*.txt")
Lamda = float(sys.argv[5])
iteration = int(sys.argv[6])
learning_rate = float(sys.argv[7])
logistic_regression(iteration, learning_rate, Lamda, ham_train_path, spam_train_path, ham_test_files, spam_test_files, stop_words=False)
logistic_regression(iteration, learning_rate, Lamda, ham_train_path, spam_train_path, ham_test_files, spam_test_files, stop_words=True)