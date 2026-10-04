import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
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
        stopWords = sys.argv[5].lower() in ("y", "yes")
        if stopWords:
            print("------------------------------------------------")
            print("Logistic regression with stop words")
            lr = LRwithStopWords.LogisticRegression(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        else:
            print("------------------------------------------------")
            print("Logistic regression without stop words")
            lr = LRwithoutStopWords.LogisticRegression(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        lr.run()
        lr.train()
        lr.test()
        if stopWords:
            print("------------------------------------------------")
            print("Naive Bayes with stop words")
            nb = NBwithStopWords.NaiveBayes(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        else:
            print("------------------------------------------------")
            print("Naive Bayes without stop words")
            nb = NBwithoutStopWords.NaiveBayes(trainingHamPath, trainingSpamPath, testHamPath, testSpamPath)
        nb.run()
        nb.train()
        nb.test()
if __name__ == "__main__":
    main()