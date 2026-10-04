import gaussianBayes
import multi
import sys
def main():
    if len(sys.argv) < 5:
        print("Usage: script.py <train_file> <train_labels> <test_file> <test_labels>")
        sys.exit(1)
    train_file = sys.argv[1]
    train_labels = sys.argv[2]
    test_file = sys.argv[3]
    test_labels = sys.argv[4]
    run_multinomial_naive_bayes(train_file, train_labels, test_file, test_labels)
    run_gaussian_naive_bayes(train_file, train_labels, test_file, test_labels, "bag")
    run_gaussian_naive_bayes(train_file, train_labels, test_file, test_labels, "tf")
def run_multinomial_naive_bayes(train_file, train_labels, test_file, test_labels):
    print("\nMultinomial with Bag of Words")
    print("-" * 20)
    bag_mn = multi.MN(train_file, train_labels)
    bag_mn.predict(test_file, test_labels)
def run_gaussian_naive_bayes(train_file, train_labels, test_file, test_labels, vectorizer_type):
    """
    Runs the Gaussian Naive Bayes model using the specified vectorizer type.
    Parameters:
    train_file : str
        Path to the training data file.
    train_labels : str
        Path to the training labels file.
    test_file : str
        Path to the test data file.
    test_labels : str
        Path to the test labels file.
    vectorizer_type : str
        The type of vectorizer to use ("bag" for Bag of Words, "tf" for TF-IDF).
    """
    vectorizer_name = "Bag of Words" if vectorizer_type == "bag" else "TF-IDF"
    print(f"\nGaussian with {vectorizer_name}")
    print("-" * 20)
    gn_model = gaussianBayes.GN(vectorizer_type, train_file, train_labels)
    gn_model.predict(test_file, test_labels, vectorizer_type)
if __name__ == "__main__":
    main()