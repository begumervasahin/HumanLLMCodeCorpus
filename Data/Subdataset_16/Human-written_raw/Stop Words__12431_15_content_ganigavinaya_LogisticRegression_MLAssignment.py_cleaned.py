
import sys
import LRwithStopWords
import LRwithoutStopWords
import NBwithStopWords
import NBwithoutStopWords
def fonk1():
    if(len(sys.argv)<6):
        print("please input command line arguments: ")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    else:
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        b4 = sys.argv[4]
        if(sys.argv[5]=="y" or (sys.argv[5]).lower()=="yes"):
            b5 = "yes"
        else:
            b5 = None
        if(b5 !=None):
            print("------------------------------------------------")
            print("Logistic regression removing stop words")
            b6 = LRwithStopWords.LogisticRegression(b1,b2,b3,b4)
            b6.run()
            b6.train()
            b6.test()
        else:
            print("------------------------------------------------")
            print("Logistic regression without removing stop words")
            b6 = LRwithoutStopWords.LogisticRegression(b1,b2,b3,b4)
            b6.run()
            b6.train()
            b6.test()
fonk1()