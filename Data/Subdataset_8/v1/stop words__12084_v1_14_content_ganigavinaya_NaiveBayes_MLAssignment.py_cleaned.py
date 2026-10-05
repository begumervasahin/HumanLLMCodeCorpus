import sys
class NaiveBayes:
    def __init__(self, trainingHamPath, trainingSpamPath, testHamPath, testSpamPath):
        pass
    def run(self):
        print("Setting up Naive Bayes...")
    def train(self):
        print("Training Naive Bayes...")
    def test(self):
        print("Testing Naive Bayes...")
class NaiveBayesWithStopWords(NaiveBayes):
    pass
class NaiveBayesWithoutStopWords(NaiveBayes):
    pass
class LogisticRegression:
    def __init__(self, trainingHamPath, trainingSpamPath, testHamPath, testSpamPath):
        pass
    def run(self):
        print("Setting up Logistic Regression...")
    def train(self):
        print("Training Logistic Regression...")
    def test(self):
        print("Testing Logistic Regression...")
class LRWithStopWords(LogisticRegression):
    pass
class LRWithoutStopWords(LogisticRegression):
    pass
def main():
    if len(sys.argv) < 6:
        print("Please input command line arguments: ")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    else:
        trainingHamPath = sys.argv[1]
        trainingSpamPath = sys.argv[2]
        testHamPath = sys.argv[3]
        testSpamPath = sys.argv[4]
        stopWords = sys.argv[5].lower() in ["y", "yes"]
        if stopWords:
            print("------------------------------------------------")
            print("Naive Bayes removing stop words")
            nb = NaiveBayesWithStopWords(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        else:
            print("------------------------------------------------")
            print("Naive Bayes without removing stop words")
            nb = NaiveBayesWithoutStopWords(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        nb.run()
        nb.train()
        nb.test()
        '''
        if stopWords:
            print("------------------------------------------------")
            print("Logistic Regression removing stop words")
            lr = LRWithStopWords(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        else:
            print("------------------------------------------------")
            print("Logistic Regression without removing stop words")
            lr = LRWithoutStopWords(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        lr.run()
        lr.train()
        lr.test()
        '''
if __name__ == "__main__":
    main()