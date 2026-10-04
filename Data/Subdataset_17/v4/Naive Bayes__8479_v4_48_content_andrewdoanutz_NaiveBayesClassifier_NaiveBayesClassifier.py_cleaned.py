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
    print("\nMultinomial with Bag of Words")
    print("-" * 20)
    bag_mn = multi.MN(train_file, train_labels)
    bag_mn.predict(test_file, test_labels)
    print("\nGaussian with Bag of Words")
    print("-" * 20)
    bag_gn = gaussianBayes.GN("bag", train_file, train_labels)
    bag_gn.predict(test_file, test_labels, "bag")
    print("\nGaussian with TF-IDF")
    print("-" * 20)
    tf_gn = gaussianBayes.GN("tf", train_file, train_labels)
    tf_gn.predict(test_file, test_labels, "tf")
if __name__ == "__main__":
    main()