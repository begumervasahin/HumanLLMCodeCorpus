import sys
class NBwithStopWords:
    class NaiveBayes:
        def __init__(self, training_ham_path, training_spam_path, test_ham_path, test_spam_path):
            self.training_ham_path = training_ham_path
            self.training_spam_path = training_spam_path
            self.test_ham_path = test_ham_path
            self.test_spam_path = test_spam_path
        def run(self):
            print(f"Running Naive Bayes with stop words on training data: {self.training_ham_path}, {self.training_spam_path}")
        def train(self):
            print("Training Naive Bayes with stop words...")
        def test(self):
            print(f"Testing Naive Bayes with stop words on test data: {self.test_ham_path}, {self.test_spam_path}")
class NBwithoutStopWords:
    class NaiveBayes:
        def __init__(self, training_ham_path, training_spam_path, test_ham_path, test_spam_path):
            self.training_ham_path = training_ham_path
            self.training_spam_path = training_spam_path
            self.test_ham_path = test_ham_path
            self.test_spam_path = test_spam_path
        def run(self):
            print(f"Running Naive Bayes without stop words on training data: {self.training_ham_path}, {self.training_spam_path}")
        def train(self):
            print("Training Naive Bayes without stop words...")
        def test(self):
            print(f"Testing Naive Bayes without stop words on test data: {self.test_ham_path}, {self.test_spam_path}")
def main():
    if len(sys.argv) < 6:
        print("Please input command line arguments: ")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    training_ham_path = sys.argv[1]
    training_spam_path = sys.argv[2]
    test_ham_path = sys.argv[3]
    test_spam_path = sys.argv[4]
    stopwords_flag = sys.argv[5].lower() in ['y', 'yes']
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
if __name__ == "__main__":
    main()