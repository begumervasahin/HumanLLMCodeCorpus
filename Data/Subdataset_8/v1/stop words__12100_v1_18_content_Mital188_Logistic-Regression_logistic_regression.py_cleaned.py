import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy as np
import sys
ham_train = sys.argv[1]
spam_train = sys.argv[2]
ham_test = sys.argv[3]
spam_test = sys.argv[4]
Lamda = float(sys.argv[5])
iteration = int(sys.argv[6])
learning_rate = float(sys.argv[7])
ham_train_files = glob.glob(ham_train + "/*.txt")
spam_train_files = glob.glob(spam_train + "/*.txt")
ham_test_files = glob.glob(ham_test + "/*.txt")
spam_test_files = glob.glob(spam_test + "/*.txt")
def read_file(filename, stop_words):
    train_file = ""
    for file_name in filename:
        with open(file_name, 'r') as file:
            train_file += file.read()
    translator = str.maketrans('', '', string.punctuation)
    train_file = train_file.translate(translator)
    translator = str.maketrans('', '', string.digits)
    train_file = train_file.translate(translator)
    train_file = Counter(train_file.split())
    if stop_words:
        train_file = Counter([word for word in train_file if word not in stopwords.words('english')])
    return train_file
def slice_bag(bag_of_words, count):
    c = 0
    for word in list(bag_of_words):
        if bag_of_words[word] < 2 and c < count:
            c += 1
            del bag_of_words[word]
    return bag_of_words
def feature_matrix(stop_word):
    unique_train_spam = read_file(spam_train_files, stop_word)
    bag_of_words = unique_train_spam
    bag_of_words = slice_bag(bag_of_words, count=4000)
    feature_matrix = []
    for file_name in ham_train_files:
        feature = {}
        with open(file_name, 'r') as file:
            test_file = file.read().split(" ")
            test_file = Counter(test_file)
            for words in bag_of_words:
                feature[words] = (test_file[words])
            feature["Probability_of_class"] = 0.0
            feature["Class_of_file"] = 0
            feature_matrix.append(feature)
    for file_name in spam_train_files:
        feature = {}
        with open(file_name, 'r') as file:
            test_file = file.read().split(" ")
            test_file = Counter(test_file)
            for words in bag_of_words:
                feature[words] = (test_file[words])
            feature["Probability_of_class"] = 0.0
            feature["Class_of_file"] = 1
            feature_matrix.append(feature)
    return feature_matrix, bag_of_words
def probability_of_class(w0, weights, feature_mat):
    for feature in feature_mat:
        sum_p = 0
        for words in weights:
            sum_p += weights[words] * feature[words]
        if sum_p < 700:
            prob = np.exp(np.array(w0 + sum_p, dtype=np.float)) / (1 + np.exp(np.array(w0 + sum_p, dtype=np.float)))
        else:
            prob = 1.0
        feature["Probability_of_class"] = prob
    return feature_mat
def update_weights(weights, n, lam, feature_matrix):
    for w in weights:
        sum = 0.0
        for feature in feature_matrix:
            sum += feature[w] * (feature["Class_of_file"] - feature["Probability_of_class"])
        weights[w] = weights[w] + n * sum - n * lam * weights[w]
    return weights
def accuracy(weights):
    count_right = 0
    count_total = 0
    for file_name in spam_test_files:
        with open(file_name, 'r') as file:
            test_file = file.read().split(" ")
            test_file = Counter(test_file)
            sum_p = 0
            count_total += 1
            for words in weights:
                sum_p += weights[words] * test_file[words]
            if sum_p < 700:
                prob = np.exp(np.array(1 + sum_p, dtype=np.float)) / (1 + np.exp(np.array(1 + sum_p, dtype=np.float)))
            else:
                prob = 1.0
            if prob > 0.9:
                count_right += 1
    for file_name in ham_test_files:
        with open(file_name, 'r') as file:
            test_file = file.read().split(" ")
            test_file = Counter(test_file)
            sum_p = 0
            count_total += 1
            for words in weights:
                sum_p += weights[words] * test_file[words]
            if sum_p < 700:
                prob = np.exp(np.array(1 + sum_p, dtype=np.float)) / (1 + np.exp(np.array(1 + sum_p, dtype=np.float)))
            else:
                prob = 1.0
            if prob < 0.9:
                count_right += 1
    return count_right / count_total
def logistic_regression(iterations, n, lam, stop_word):
    feature_matrix, bag_of_words = feature_matrix(stop_word)
    w0 = 1.0
    initial_w = {word: 1.0 for word in bag_of_words}
    feature_matrix = probability_of_class(w0, initial_w, feature_matrix)
    w = initial_w
    for i in range(iterations):
        w = update_weights(w, n, lam, feature_matrix)
        feature_matrix = probability_of_class(w0, w, feature_matrix)
    final_accuracy = accuracy(w)
    if stop_word == 1:
        print("Logistic Regression - filtered - Total Accuracy - {:.2f}".format(final_accuracy * 100))
    else:
        print("Logistic Regression - unfiltered - Total Accuracy - {:.2f}".format(final_accuracy * 100))
logistic_regression(iterations=iteration, n=learning_rate, lam=Lamda, stop_word=0)
logistic_regression(iterations=iteration, n=learning_rate, lam=Lamda, stop_word=1)