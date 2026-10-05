import sys
import LRwithStopWords
import LRwithoutStopWords
def main():
    if len(sys.argv) < 6:
        print("Please input command line arguments: ")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    training_ham_path = sys.argv[1]
    training_spam_path = sys.argv[2]
    test_ham_path = sys.argv[3]
    test_spam_path = sys.argv[4]
    stop_words = sys.argv[5].lower() in {"y", "yes"}
    if stop_words:
        print("------------------------------------------------")
        print("Logistic regression removing stop words")
        lr = LRwithStopWords.LogisticRegression(training_ham_path, training_spam_path, test_ham_path, test_spam_path)
    else:
        print("------------------------------------------------")
        print("Logistic regression without removing stop words")
        lr = LRwithoutStopWords.LogisticRegression(training_ham_path, training_spam_path, test_ham_path, test_spam_path)
    lr.run()
    lr.train()
    lr.test()
main()