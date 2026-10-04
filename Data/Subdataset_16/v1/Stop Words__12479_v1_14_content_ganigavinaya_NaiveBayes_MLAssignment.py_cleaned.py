import sys
class class1:
    class class2:
        def fonk1(self, b1, b2, b3, b4):
            self.b1 = b1
            self.b2 = b2
            self.b3 = b3
            self.b4 = b4
        def fonk2(self):
            print(f"Running Naive Bayes with stop words on training data: {self.b1}, {self.b2}")
        def fonk3(self):
            print("Training Naive Bayes with stop words...")
        def fonk4(self):
            print(f"Testing Naive Bayes with stop words on test data: {self.b3}, {self.b4}")
class class3:
    class class4:
        def fonk5(self, b1, b2, b3, b4):
            self.b1 = b1
            self.b2 = b2
            self.b3 = b3
            self.b4 = b4
        def fonk6(self):
            print(f"Running Naive Bayes without stop words on training data: {self.b1}, {self.b2}")
        def fonk7(self):
            print("Training Naive Bayes without stop words...")
        def fonk8(self):
            print(f"Testing Naive Bayes without stop words on test data: {self.b3}, {self.b4}")
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
        b5 = sys.argv[5].lower() in ['y', 'yes']
        if b5:
            print("------------------------------------------------")
            print("Naive Bayes removing stop words")
            b6 = class1.class4(b1, b2, b3, b4)
        else:
            print("------------------------------------------------")
            print("Naive Bayes without removing stop words")
            b6 = class3.class4(b1, b2, b3, b4)
        b6.fonk6()
        b6.fonk7()
        b6.fonk8()
if b7 = = "__main__":
    fonk9()