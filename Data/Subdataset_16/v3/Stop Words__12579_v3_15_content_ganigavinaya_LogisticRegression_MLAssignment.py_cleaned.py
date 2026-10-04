import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
def fonk1():
    print("Please input command line arguments:")
    print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
def fonk2():
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = sys.argv[5].lower() in ("y", "yes")
    return b1, b2, b3, b4, b5
def fonk3(b1, b2, b3, b4, b5):
    if b5:
        print("------------------------------------------------")
        print("Logistic regression with stop words")
        b6 = LRwithStopWords.LogisticRegression(b1, b2, b3, b4)
    else:
        print("------------------------------------------------")
        print("Logistic regression without stop words")
        b6 = LRwithoutStopWords.LogisticRegression(b1, b2, b3, b4)
    b6.run()
    b6.train()
    b6.test()
def fonk4(b1, b2, b3, b4, b5):
    if b5:
        print("------------------------------------------------")
        print("Naive Bayes with stop words")
        b7 = NBwithStopWords.NaiveBayes(b1, b2, b3, b4)
    else:
        print("------------------------------------------------")
        print("Naive Bayes without stop words")
        b7 = NBwithoutStopWords.NaiveBayes(b1, b2, b3, b4)
    b7.run()
    b7.train()
    b7.test()
def fonk5():
    if len(sys.argv) < 6:
        fonk1()
        return
    b1, b2, b3, b4, b5 = fonk2()
    fonk3(b1, b2, b3, b4, b5)
    fonk4(b1, b2, b3, b4, b5)
if b8 = = "__main__":
    fonk5()