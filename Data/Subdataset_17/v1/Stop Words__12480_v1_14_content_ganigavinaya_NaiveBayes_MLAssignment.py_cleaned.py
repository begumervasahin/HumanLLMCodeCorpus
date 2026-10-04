import sys
class NBwithStopWords:
    class NaiveBayes:
        def __init__(self, trainingHamPath, trainingSpamPath, testHamPath, testSpamPath):
            self.trainingHamPath = trainingHamPath
            self.trainingSpamPath = trainingSpamPath
            self.testHamPath = testHamPath
            self.testSpamPath = testSpamPath
        def run(self):
            print(f"Running Naive Bayes with stop words on training data: {self.trainingHamPath}, {self.trainingSpamPath}")
        def train(self):
            print("Training Naive Bayes with stop words...")
        def test(self):
            print(f"Testing Naive Bayes with stop words on test data: {self.testHamPath}, {self.testSpamPath}")
class NBwithoutStopWords:
    class NaiveBayes:
        def __init__(self, trainingHamPath, trainingSpamPath, testHamPath, testSpamPath):
            self.trainingHamPath = trainingHamPath
            self.trainingSpamPath = trainingSpamPath
            self.testHamPath = testHamPath
            self.testSpamPath = testSpamPath
        def run(self):
            print(f"Running Naive Bayes without stop words on training data: {self.trainingHamPath}, {self.trainingSpamPath}")
        def train(self):
            print("Training Naive Bayes without stop words...")
        def test(self):
            print(f"Testing Naive Bayes without stop words on test data: {self.testHamPath}, {self.testSpamPath}")
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
        stopWords = sys.argv[5].lower() in ['y', 'yes']
        if stopWords:
            print("------------------------------------------------")
            print("Naive Bayes removing stop words")
            nb = NBwithStopWords.NaiveBayes(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        else:
            print("------------------------------------------------")
            print("Naive Bayes without removing stop words")
            nb = NBwithoutStopWords.NaiveBayes(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        nb.run()
        nb.train()
        nb.test()
if __name__ == "__main__":
    main()