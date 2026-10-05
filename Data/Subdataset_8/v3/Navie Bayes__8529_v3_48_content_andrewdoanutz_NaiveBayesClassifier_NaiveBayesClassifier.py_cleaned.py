import gaussianBayes
import multi
import sys
def main():
    print("\nMultinomial Naive Bayes with Bag of Words")
    print("-" * 20)
    mnb_bag_of_words = multi.MultinomialNaiveBayes(sys.argv[1], sys.argv[2])
    mnb_bag_of_words.predict(sys.argv[3], sys.argv[4])
    print("\nGaussian Naive Bayes with Bag of Words")
    print("-" * 20)
    gnb_bag_of_words = gaussianBayes.GaussianNaiveBayes("bag", sys.argv[1], sys.argv[2])
    gnb_bag_of_words.predict(sys.argv[3], sys.argv[4], "bag")
    print("\nGaussian Naive Bayes with TF-IDF")
    print("-" * 20)
    gnb_tfidf = gaussianBayes.GaussianNaiveBayes("tf", sys.argv[1], sys.argv[2])
    gnb_tfidf.predict(sys.argv[3], sys.argv[4], "tf")
if __name__ == "__main__":
    main()