import sys
import LRwithStopWords
import LRwithoutStopWords
def main():
    if len(sys.argv) < 6:
        print("Please provide the following command line arguments:")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    training_ham_path = sys.argv[1]
    training_spam_path = sys.argv[2]
    test_ham_path = sys.argv[3]
    test_spam_path = sys.argv[4]
    use_stopwords = sys.argv[5].lower() in ['y', 'yes']
    if use_stopwords:
        print("------------------------------------------------")
        print("Logistic Regression with stop words removal")
        lr = LRwithStopWords.LogisticRegression(
            training_ham_path, training_spam_path, test_ham_path, test_spam_path
        )
    else:
        print("------------------------------------------------")
        print("Logistic Regression without stop words removal")
        lr = LRwithoutStopWords.LogisticRegression(
            training_ham_path, training_spam_path, test_ham_path, test_spam_path
        )
    lr.run()
    lr.train()
    lr.test()
if __name__ == "__main__":
    main()