import argparse
from knn import KNNClassifier
from ncc import NearestCentroidClassifier
def run_classifier(k, mode='knn', distance='euclidean', keep_punctuation=False, keep_stopwords=False):
    if mode == 'knn':
        classifier = KNNClassifier(k, distance=distance, keep_stopwords=keep_stopwords, keep_punc=keep_punctuation)
        classifier.score()
    elif mode == 'ncc':
        classifier = NearestCentroidClassifier(k, distance=distance, keep_stopwords=keep_stopwords, keep_punc=keep_punctuation)
        classifier.score()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    punctuation_group = parser.add_mutually_exclusive_group()
    punctuation_group.add_argument('--punc', dest='keep_punctuation', action='store_true', help='Keep punctuation in the text data')
    punctuation_group.add_argument('--no-punc', dest='keep_punctuation', action='store_false', help='Remove punctuation from the text data')
    stopword_group = parser.add_mutually_exclusive_group()
    stopword_group.add_argument('--stop', dest='keep_stopwords', action='store_true', help='Keep stopwords in the text data')
    stopword_group.add_argument('--no-stop', dest='keep_stopwords', action='store_false', help='Remove stopwords from the text data')
    parser.add_argument('--distance', dest='distance', default='euclidean', help='Distance metric for classification')
    parser.add_argument('-k', dest='k', required=True, type=int, help='Number of neighbors for classification')
    parser.set_defaults(keep_punctuation=False, keep_stopwords=False)
    args = parser.parse_args()
    run_classifier(k=args.k, distance=args.distance, keep_punctuation=args.keep_punctuation, keep_stopwords=args.keep_stopwords)