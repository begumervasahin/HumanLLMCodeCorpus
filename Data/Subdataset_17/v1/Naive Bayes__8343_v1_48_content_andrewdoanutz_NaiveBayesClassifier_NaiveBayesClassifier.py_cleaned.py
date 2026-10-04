import gaussianBayes
import multi
import sys
def main():
    if len(sys.argv) != 5:
        print("Usage: script.py <train_file> <test_file> <vectorizer_train> <vectorizer_test>")
        sys.exit(1)
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    vectorizer_train = sys.argv[3]
    vectorizer_test = sys.argv[4]
    print("\nMultinomial with bag of words")
    print("-" * 20)
    bagMN = multi.MN(train_file, test_file)
    bagMN.predict(vectorizer_train, vectorizer_test)
    print("\nGaussian with bag of words")
    print("-" * 20)
    bagGN = gaussianBayes.GN("bag", train_file, test_file)
    bagGN.predict(vectorizer_train, vectorizer_test, "bag")
    print("\nGaussian with tfidf")
    print("-" * 20)
    tfGN = gaussianBayes.GN("tf", train_file, test_file)
    tfGN.predict(vectorizer_train, vectorizer_test, "tf")
if __name__ == "__main__":
    main()