import sys
class class1:
    def fonk1(self, b1, b2, b3, b4):
        pass
    def fonk2(self):
        print("Setting up Naive Bayes...")
    def fonk3(self):
        print("Training Naive Bayes...")
    def fonk4(self):
        print("Testing Naive Bayes...")
class class2(class1):
    pass
class class3(class1):
    pass
class class4:
    def fonk5(self, b1, b2, b3, b4):
        pass
    def fonk6(self):
        print("Setting up Logistic Regression...")
    def fonk7(self):
        print("Training Logistic Regression...")
    def fonk8(self):
        print("Testing Logistic Regression...")
class class5(class4):
    pass
class class6(class4):
    pass
def fonk9():
    if len(sys.argv) < 6:
        print("Please input command line arguments: ")
        print("[training ham path] [training spam path] [test ham path] [test spam path] [stopwords]\n")
        return
    else:
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        b4 = sys.argv[4]
        b5 = sys.argv[5].lower() in ["y", "yes"]
        if b5:
            print("------------------------------------------------")
            print("Naive Bayes removing stop words")
            b6 = class2(b1, b2, b3, b4)
        else:
            print("------------------------------------------------")
            print("Naive Bayes without removing stop words")
            b6 = class3(b1, b2, b3, b4)
        b6.fonk6()
        b6.fonk7()
        b6.fonk8()
        '''
        if b5:
            print("------------------------------------------------")
            print("Logistic Regression removing stop words")
            b7 = class5(b1, b2, b3, b4)
        else:
            print("------------------------------------------------")
            print("Logistic Regression without removing stop words")
            b7 = class6(b1, b2, b3, b4)
        b7.fonk6()
        b7.fonk7()
        b7.fonk8()
        '''
if b8 = = "__main__":
    fonk9()