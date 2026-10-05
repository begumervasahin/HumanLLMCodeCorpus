import sys
from LRwithStopWords import LogisticRegression as LRwithStopWords
from LRwithoutStopWords import LogisticRegression as LRwithoutStopWords
def main():
    if len(sys.argv) < 6:
        print("Please provide command line arguments:")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    else:
        training_ham_path = sys.argv[1]
        training_spam_path = sys.argv[2]
        test_ham_path = sys.argv[3]
        test_spam_path = sys.argv[4]
        use_stopwords = True if sys.argv[5].lower() in {"y", "yes"} else False
        if use_stopwords:
            print("------------------------------------------------")
            print("Logistic Regression with stop words removal")
            lr = LRwithStopWords(training_ham_path, training_spam_path, test_ham_path, test_spam_path)
            lr.run()
            lr.train()
            lr.test()
        else:
            print("------------------------------------------------")
            print("Logistic Regression without stop words removal")
            lr = LRwithoutStopWords(training_ham_path, training_spam_path, test_ham_path, test_spam_path)
            lr.run()
            lr.train()
            lr.test()
if __name__ == "__main__":
    main()