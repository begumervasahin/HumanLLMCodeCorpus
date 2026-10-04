import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
def read_file(filenames, remove_stopwords=False):
    combined_text = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            combined_text += file.read()
    translator = str.maketrans('', '', string.punctuation + string.digits)
    cleaned_text = combined_text.translate(translator)
    word_counts = Counter(cleaned_text.split())
    if remove_stopwords:
        word_counts = Counter([word for word in word_counts if word not in stopwords.words('english')])
    return word_counts
def calculate_word_probabilities(word_counts):
    total_count = sum(word_counts.values())
    return {word: count / total_count for word, count in word_counts.items()}
def calculate_probabilities_given_word(word_counts, bag_of_words):
    return {word: word_counts.get(word, 0) / (bag_of_words.get(word, 0) + len(bag_of_words)) for word in bag_of_words}
def calculate_test_file_probabilities(test_files, prob_ham_given_word, prob_spam_given_word, bag_of_words):
    count_ham = 0.0
    count_spam = 0.0
    for filename in test_files:
        with open(filename, 'r') as file:
            test_text = file.read()
        test_word_counts = Counter(test_text.split())
        prob_ham = prob_spam = 1.0
        for word in test_word_counts:
            if word in bag_of_words:
                prob_ham *= prob_ham_given_word.get(word, 0)
                prob_spam *= prob_spam_given_word.get(word, 0)
        if prob_ham + prob_spam:
            if prob_ham / (prob_ham + prob_spam) > 0.5:
                count_ham += 1
            else:
                count_spam += 1
    return count_ham, count_spam
def apply_laplace_smoothing(train_ham, train_spam, bag_of_words):
    for word in bag_of_words:
        train_ham[word] += 1
        train_spam[word] += 1
    return train_ham, train_spam
def evaluate_accuracy(ham_train, spam_train, ham_test, spam_test, remove_stopwords):
    train_ham_counts = read_file(ham_train, remove_stopwords)
    train_spam_counts = read_file(spam_train, remove_stopwords)
    bag_of_words = train_ham_counts + train_spam_counts
    smoothed_ham_counts, smoothed_spam_counts = apply_laplace_smoothing(train_ham_counts, train_spam_counts, bag_of_words)
    prob_ham_given_word = calculate_probabilities_given_word(smoothed_ham_counts, bag_of_words)
    prob_spam_given_word = calculate_probabilities_given_word(smoothed_spam_counts, bag_of_words)
    ham_correct, spam_correct = calculate_test_file_probabilities(ham_test, prob_ham_given_word, prob_spam_given_word, bag_of_words)
    ham_accuracy = ham_correct / len(ham_test) if ham_test else 0
    spam_accuracy = spam_correct / len(spam_test) if spam_test else 0
    print(f"Ham Accuracy: {ham_accuracy:.2f}")
    print(f"Spam Accuracy: {spam_accuracy:.2f}")
if __name__ == "__main__":
    ham_train_files = glob.glob(sys.argv[1] + "/*.txt")
    spam_train_files = glob.glob(sys.argv[2] + "/*.txt")
    ham_test_files = glob.glob(sys.argv[3] + "/*.txt")
    spam_test_files = glob.glob(sys.argv[4] + "/*.txt")
    lamda = float(sys.argv[5])
    iteration = int(sys.argv[6])
    learning_rate = float(sys.argv[7])
    print("Evaluating without stopword removal:")
    evaluate_accuracy(ham_train_files, spam_train_files, ham_test_files, spam_test_files, remove_stopwords=False)
    print("\nEvaluating with stopword removal:")
    evaluate_accuracy(ham_train_files, spam_train_files, ham_test_files, spam_test_files, remove_stopwords=True)