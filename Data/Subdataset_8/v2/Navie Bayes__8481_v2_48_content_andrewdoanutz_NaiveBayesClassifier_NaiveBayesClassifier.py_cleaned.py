import gaussianBayes
import multi
import sys
def main():
    print("\nMultinomial Naive Bayes with Bag of Words")
    print("-" * 20)
    bag_of_words_mnb = multi.MN(sys.argv[1], sys.argv[2])
    bag_of_words_mnb.predict(sys.argv[3], sys.argv[4])
    print("\nGaussian Naive Bayes with Bag of Words")
    print("-" * 20)
    bag_of_words_gnb = gaussianBayes.GN("bag", sys.argv[1], sys.argv[2])
    bag_of_words_gnb.predict(sys.argv[3], sys.argv[4], "bag")
    print("\nGaussian Naive Bayes with TF-IDF")
    print("-" * 20)
    tfidf_gnb = gaussianBayes.GN("tf", sys.argv[1], sys.argv[2])
    tfidf_gnb.predict(sys.argv[3], sys.argv[4], "tf")
if __name__ == "__main__":
    main()