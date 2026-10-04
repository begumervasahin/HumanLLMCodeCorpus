
import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
def display_usage_instructions():
    print("Please input the following command line arguments: ")
    print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords (y/n)]\n")
def parse_command_line_arguments():
    if len(sys.argv) < 6:
        display_usage_instructions()
        sys.exit(1)
    training_ham_path = sys.argv[1]
    training_spam_path = sys.argv[2]
    test_ham_path = sys.argv[3]
    test_spam_path = sys.argv[4]
    stopwords_flag = sys.argv[5].lower() in ["y", "yes"]
    return training_ham_path, training_spam_path, test_ham_path, test_spam_path, stopwords_flag
def run_naive_bayes(training_ham_path, training_spam_path, test_ham_path, test_spam_path, stopwords_flag):
    if stopwords_flag:
        print("------------------------------------------------")
        print("Naive Bayes removing stop words")
        nb = NBwithStopWords.NaiveBayes(training_ham_path, training_spam_path, test_ham_path, test_spam_path)
    else:
        print("------------------------------------------------")
        print("Naive Bayes without removing stop words")
        nb = NBwithoutStopWords.NaiveBayes(training_ham_path, training_spam_path, test_ham_path, test_spam_path)
    nb.run()
    nb.train()
    nb.test()
def main():
    training_ham_path, training_spam_path, test_ham_path, test_spam_path, stopwords_flag = parse_command_line_arguments()
    run_naive_bayes(training_ham_path, training_spam_path, test_ham_path, test_spam_path, stopwords_flag)
if __name__ == "__main__":
    main()