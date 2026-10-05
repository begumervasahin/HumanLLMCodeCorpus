import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
def fonk1():
    if len(sys.argv) < 6:
        print("Insufficient arguments provided.")
        print("Usage: [training ham path] [training spam path] [test ham path] [test spam path] [b5 (y/n)]\n")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = sys.argv[5].lower() in ("y", "yes")
    return b1, b2, b3, b4, b5
def fonk2(b1, b2, b3, b4, b5):
    if b5:
        print("------------------------------------------------")
        print("Running Naive Bayes with stop words removed")
        b6 = NBwithStopWords.NaiveBayes(b1, b2, b3, b4)
    else:
        print("------------------------------------------------")
        print("Running Naive Bayes without removing stop words")
        b6 = NBwithoutStopWords.NaiveBayes(b1, b2, b3, b4)
    b6.run()
    b6.train()
    b6.test()
def fonk3():
    b1, b2, b3, b4, b5 = fonk4()
    fonk5(b1, b2, b3, b4, b5)
if b7 = = "__main__":
    fonk6()
import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
def fonk4():
    if len(sys.argv) < 6:
        print("Insufficient arguments provided.")
        print("Usage: [training ham path] [training spam path] [test ham path] [test spam path] [b5 (y/n)]\n")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = sys.argv[5].lower() in ("y", "yes")
    return b1, b2, b3, b4, b5
def fonk5(b1, b2, b3, b4, b5):
    if b5:
        print("------------------------------------------------")
        print("Running Naive Bayes with stop words removed")
        b6 = NBwithStopWords.NaiveBayes(b1, b2, b3, b4)
    else:
        print("------------------------------------------------")
        print("Running Naive Bayes without removing stop words")
        b6 = NBwithoutStopWords.NaiveBayes(b1, b2, b3, b4)
    b6.run()
    b6.train()
    b6.test()
def fonk6():
    b1, b2, b3, b4, b5 = fonk4()
    fonk5(b1, b2, b3, b4, b5)
if b7 = = "__main__":
    fonk6()