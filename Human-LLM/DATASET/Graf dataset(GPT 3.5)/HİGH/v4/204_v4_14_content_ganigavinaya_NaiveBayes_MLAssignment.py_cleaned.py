import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
def fonk1():
    if len(sys.argv) < 6:
        print("Please input command line arguments:")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    else:
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        b4 = sys.argv[4]
        if sys.argv[5].lower() in ("y", "yes"):
            b5 = True
        else:
            b5 = False
        if b5:
            print("------------------------------------------------")
            print("Naive Bayes removing stop words")
            b6 = NBwithStopWords.NaiveBayes(b1, b2, b3, b4)
            b6.run()
            b6.train()
            b6.test()
        else:
            print("------------------------------------------------")
            print("Naive Bayes without removing stop words")
            b6 = NBwithoutStopWords.NaiveBayes(b1, b2, b3, b4)
            b6.run()
            b6.train()
            b6.test()
if b7 = = "__main__":
    fonk1()