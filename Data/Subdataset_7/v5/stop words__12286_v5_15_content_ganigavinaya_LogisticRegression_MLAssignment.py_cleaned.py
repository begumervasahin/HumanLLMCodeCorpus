import sys
import LRwithStopWords
import LRwithoutStopWords
def fonk1():
    if len(sys.argv) < 6:
        print("Please input command line arguments: ")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = sys.argv[5].lower() in {"y", "yes"}
    if b5:
        print("------------------------------------------------")
        print("Logistic regression removing stop words")
        b6 = LRwithStopWords.LogisticRegression(b1, b2, b3, b4)
    else:
        print("------------------------------------------------")
        print("Logistic regression without removing stop words")
        b6 = LRwithoutStopWords.LogisticRegression(b1, b2, b3, b4)
    b6.run()
    b6.train()
    b6.test()
fonk1()