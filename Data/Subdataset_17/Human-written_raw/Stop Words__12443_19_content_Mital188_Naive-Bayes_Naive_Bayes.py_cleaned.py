import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy
import sys
ham_train = sys.argv[1]
spam_train = sys.argv[2]
ham_test = sys.argv[3]
spam_test = sys.argv[4]
Lamda = sys.argv[5]
iteration = sys.argv[6]
learning_rate = sys.argv[7]
ham_train = glob.glob(ham_train+"/*.txt")
spam_train = glob.glob(spam_train+"/*.txt")
ham_test = glob.glob(ham_test+"/*.txt")
spam_test = glob.glob(spam_test+"/*.txt")
def read_file(filename, stop_words, bayes):
    train_file = ""
    for file_names in filename:
        files = open(file_names)
        train_file += files.read()
    translator = str.maketrans('', '', string.punctuation)
    train_file = train_file.translate(translator)
    translator = str.maketrans('', '', string.digits)
    train_file = train_file.translate(translator)
    train_file = Counter(train_file.split())
    if stop_words:
        train_file = Counter([word for word in train_file if word not in stopwords.words('english')])
    return train_file
def word_probability(unique_words):
    word_prob = {}
    total_count = 0
    for i in unique_words:
        total_count += unique_words[i]
    for i in unique_words:
        word_prob[i] = float(unique_words[i]) / int(total_count)
    return word_prob
def probability_given_word(unique_word):
    prob = {}
    for word_bag in bag_of_words:
        prob[word_bag] = float(unique_word[word_bag]) / float(bag_of_words[word_bag] + len(bag_of_words))
    return prob
def calculate_probability(test_file):
    count_spam = 0.0
    count_ham = 0.0
    for file_name in test_file:
        ln_prob_spam = 0.0
        ln_prob_ham = 0.0
        prob_ham = 1.0
        prob_spam = 1.0
        file = open(file_name)
        test_file_ham = file.read()
        test_file_ham = Counter(test_file_ham.split())
        for word in test_file_ham:
            if word in bag_of_words:
                prob_ham = prob_ham * prob_ham_given_word[word]
                prob_spam = prob_spam * prob_spam_given_word[word]
        if prob_ham + prob_spam:
            if prob_ham / (prob_ham + prob_spam) > 0.5:
                count_ham += 1
            else:
                count_spam += 1
    return count_ham, count_spam
def laplace_smoothing(train_1, train_2, bag):
    for word in bag:
        train_1[word] += 1
        train_2[word] += 1
    return train_1, train_2
def accuracy_bayes(stop_word):
    unique_train_ham = read_file(ham_train, stop_word, 0)
    unique_train_spam = read_file(spam_train, stop_word, 0)
accuracy_bayes(stop_word=0)
accuracy_bayes(stop_word=1)