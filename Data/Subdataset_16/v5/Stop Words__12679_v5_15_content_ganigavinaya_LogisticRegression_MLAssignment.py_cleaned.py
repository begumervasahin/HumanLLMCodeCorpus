import sys
import LRwithStopWords
import LRwithoutStopWords
def fonk1():
    print("Please provide the following command line arguments:")
    print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
def fonk2():
    if len(sys.argv) < 6:
        fonk1()
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = sys.argv[5].strip().lower() in ['y', 'yes']
    return b1, b2, b3, b4, b5
def fonk3(b5, b1, b2, b3, b4):
    if b5:
        print("------------------------------------------------")
        print("Logistic Regression with stop words removal")
        return LRwithStopWords.LogisticRegression(b1, b2, b3, b4)
    else:
        print("------------------------------------------------")
        print("Logistic Regression without stop words removal")
        return LRwithoutStopWords.LogisticRegression(b1, b2, b3, b4)
def fonk4():
    b1, b2, b3, b4, b5 = fonk2()
    b6 = fonk3(b5, b1, b2, b3, b4)
    b6.run()
    b6.train()
    b6.test()
if b7 = = "__main__":
    fonk4()