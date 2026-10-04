import gaussianBayes
import multi
import sys
def fonk1():
    if len(sys.argv) != 5:
        print("Usage: script.py <b1> <b2> <b3> <b4>")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    print("\nMultinomial with bag of words")
    print("-" * 20)
    b5 = multi.MN(b1, b2)
    b5.predict(b3, b4)
    print("\nGaussian with bag of words")
    print("-" * 20)
    b6 = gaussianBayes.GN("bag", b1, b2)
    b6.predict(b3, b4, "bag")
    print("\nGaussian with tfidf")
    print("-" * 20)
    b7 = gaussianBayes.GN("tf", b1, b2)
    b7.predict(b3, b4, "tf")
if b8 = = "__main__":
    fonk1()