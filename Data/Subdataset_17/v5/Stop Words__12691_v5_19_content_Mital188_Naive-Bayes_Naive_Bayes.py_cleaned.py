import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
ham_train_path = sys.argv[1]
spam_train_path = sys.argv[2]
ham_test_path = sys.argv[3]
spam_test_path = sys.argv[4]
Lambda = float(sys.argv[5])
iterations = int(sys.argv[6])
learning_rate = float(sys.argv[7])
ham_train_files = glob.glob(f"{ham_train_path}/*.txt")
spam_train_files = glob.glob(f"{spam_train_path}/*.txt")
ham_test_files = glob.glob(f"{ham_test_path}/*.txt")
spam_test_files = glob.glob(f"{spam_test_path}/*.txt")
def read_files(filenames, use_stop_words=False):
    content = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            content += file.read()
    translator = str.maketrans('', '', string.punctuation + string.digits)
    content = content.translate(translator)
    word_counts = Counter(content.split())
    if use_stop_words:
        stop_words = set(stopwords.words('english'))
        word_counts = Counter([word for word in word_counts if word not in stop_words])
    return word_counts
def calculate_word_probabilities(word_counts):
    total_words = sum(word_counts.values())
    return {word: count / total_words for word, count in word_counts.items()}
def calculate_conditional_probabilities(word_counts, vocabulary):
    return {word: (word_counts[word] + 1) / (vocabulary[word] + len(vocabulary)) for word in vocabulary}
def classify_emails(test_files, vocabulary, prob_ham_given_word, prob_spam_given_word):
    ham_count, spam_count = 0, 0
    for filename in test_files:
        with open(filename, 'r') as file:
            content = file.read()
        word_counts = Counter(content.split())
        prob_ham, prob_spam = 1.0, 1.0
        for word in word_counts:
            if word in vocabulary:
                prob_ham *= prob_ham_given_word.get(word, 1.0)
                prob_spam *= prob_spam_given_word.get(word, 1.0)
        if prob_ham > prob_spam:
            ham_count += 1
        else:
            spam_count += 1
    return ham_count, spam_count
def apply_laplace_smoothing(ham_counts, spam_counts, vocabulary):
    for word in vocabulary:
        ham_counts[word] += 1
        spam_counts[word] += 1
    return ham_counts, spam_counts
def calculate_accuracy(use_stop_words):
    ham_word_counts = read_files(ham_train_files, use_stop_words)
    spam_word_counts = read_files(spam_train_files, use_stop_words)
    vocabulary = set(ham_word_counts) | set(spam_word_counts)
    vocabulary = Counter(vocabulary)
    ham_word_counts, spam_word_counts = apply_laplace_smoothing(ham_word_counts, spam_word_counts, vocabulary)
    prob_ham_given_word = calculate_conditional_probabilities(ham_word_counts, vocabulary)
    prob_spam_given_word = calculate_conditional_probabilities(spam_word_counts, vocabulary)
    ham_correct, spam_correct = classify_emails(ham_test_files, vocabulary, prob_ham_given_word, prob_spam_given_word)
    print(f"Ham Accuracy: {ham_correct / len(ham_test_files):.2f}")
    print(f"Spam Accuracy: {spam_correct / len(spam_test_files):.2f}")
calculate_accuracy(use_stop_words=False)
calculate_accuracy(use_stop_words=True)