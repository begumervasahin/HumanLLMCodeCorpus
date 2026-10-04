import gaussianBayes
import multi
import sys
def fonk1():
    if len(sys.argv) < 5:
        print("Usage: script.py <b1> <b2> <b3> <b4>")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    fonk2(b1, b2, b3, b4)
    fonk3(b1, b2, b3, b4, "bag")
    fonk3(b1, b2, b3, b4, "tf")
def fonk2(b1, b2, b3, b4):
    print("\nMultinomial with Bag of Words")
    print("-" * 20)
    b5 = multi.MN(b1, b2)
    b5.predict(b3, b4)
def fonk3(b1, b2, b3, b4, vectorizer_type):
    """
    Runs the Gaussian Naive Bayes model using the specified vectorizer type.
    Parameters:
    b1 : str
        Path to the training data file.
    b2 : str
        Path to the training labels file.
    b3 : str
        Path to the test data file.
    b4 : str
        Path to the test labels file.
    vectorizer_type : str
        The type of vectorizer to use ("bag" for Bag of Words, "tf" for TF-IDF).
    """
    b6 = "Bag of Words" if vectorizer_type == "bag" else "TF-IDF"
    print(f"\nGaussian with {b6}")
    print("-" * 20)
    b7 = gaussianBayes.GN(vectorizer_type, b1, b2)
    b7.predict(b3, b4, vectorizer_type)
if b8 = = "__main__":
    fonk1()