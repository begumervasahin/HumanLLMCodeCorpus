import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy as np
import sys
def read_file(filenames, stop_words):
    train_file = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            train_file += file.read()
    translator = str.maketrans('', '', string.punctuation + string.digits)
    train_file = train_file.translate(translator)
    word_counts = Counter(train_file.split())
    if stop_words:
        word_counts = Counter([word for word in word_counts if word not in stopwords.words('english')])
    return word_counts
def word_probability(word_counts):
    total_count = sum(word_counts.values())
    return {word: count / total_count for word, count in word_counts.items()}
def probability_given_word(word_counts, bag_of_words):
    return {word: word_counts.get(word, 0) / (bag_of_words.get(word, 0) + len(bag_of_words)) for word in bag_of_words}
def calculate_probability(test_files, prob_ham_given_word, prob_spam_given_word, bag_of_words):
    count_ham = 0.0
    count_spam = 0.0
    for filename in test_files:
        with open(filename, 'r') as file:
            test_file = file.read()
        test_file = Counter(test_file.split())
        prob_ham = 1.0
        prob_spam = 1.0
        for word in test_file:
            if word in bag_of_words:
                prob_ham *= prob_ham_given_word.get(word, 0)
                prob_spam *= prob_spam_given_word.get(word, 0)
        if prob_ham + prob_spam:
            if prob_ham / (prob_ham + prob_spam) > 0.5:
                count_ham += 1
            else:
                count_spam += 1
    return count_ham, count_spam
def laplace_smoothing(train_ham, train_spam, bag_of_words):
    for word in bag_of_words:
        train_ham[word] += 1
        train_spam[word] += 1
    return train_ham, train_spam
def accuracy_bayes(ham_train, spam_train, ham_test, spam_test, stop_words):
    unique_train_ham = read_file(ham_train, stop_words)
    unique_train_spam = read_file(spam_train, stop_words)
    bag_of_words = unique_train_ham + unique_train_spam
    train_ham_smoothed, train_spam_smoothed = laplace_smoothing(unique_train_ham, unique_train_spam, bag_of_words)
    prob_ham_given_word = probability_given_word(train_ham_smoothed, bag_of_words)
    prob_spam_given_word = probability_given_word(train_spam_smoothed, bag_of_words)
    count_ham, count_spam = calculate_probability(ham_test, prob_ham_given_word, prob_spam_given_word, bag_of_words)
    total_ham = len(ham_test)
    total_spam = len(spam_test)
    ham_accuracy = count_ham / total_ham if total_ham > 0 else 0
    spam_accuracy = count_spam / total_spam if total_spam > 0 else 0
    print(f"Ham Accuracy: {ham_accuracy}")
    print(f"Spam Accuracy: {spam_accuracy}")
if __name__ == "__main__":
    ham_train = glob.glob(sys.argv[1] + "/*.txt")
    spam_train = glob.glob(sys.argv[2] + "/*.txt")
    ham_test = glob.glob(sys.argv[3] + "/*.txt")
    spam_test = glob.glob(sys.argv[4] + "/*.txt")
    lamda = float(sys.argv[5])
    iteration = int(sys.argv[6])
    learning_rate = float(sys.argv[7])
    accuracy_bayes(ham_train, spam_train, ham_test, spam_test, stop_words=False)
    accuracy_bayes(ham_train, spam_train, ham_test, spam_test, stop_words=True)