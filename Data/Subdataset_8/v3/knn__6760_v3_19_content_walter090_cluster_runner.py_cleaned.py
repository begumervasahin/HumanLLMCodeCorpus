import argparse
from knn import KNNClassifier
from ncc import NearestCentroidClassifier
def run_classifier(k, mode='knn', distance='euclidean', keep_punc=False, keep_stopwords=False):
    if mode == 'knn':
        classifier = KNNClassifier(k, distance=distance, keep_stopwords=keep_stopwords, keep_punc=keep_punc)
    elif mode == 'ncc':
        classifier = NearestCentroidClassifier(k, distance=distance, keep_stopwords=keep_stopwords, keep_punc=keep_punc)
    classifier.score()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run kNN or Nearest Centroid Classifier.')
    punc_parse = parser.add_mutually_exclusive_group()
    punc_parse.add_argument('--punc', dest='keep_punc', action='store_true', help='Keep punctuation')
    punc_parse.add_argument('--no-punc', dest='keep_punc', action='store_false', help='Remove punctuation')
    stop_parse = parser.add_mutually_exclusive_group()
    stop_parse.add_argument('--stop', dest='keep_stopwords', action='store_true', help='Keep stopwords')
    stop_parse.add_argument('--no-stop', dest='keep_stopwords', action='store_false', help='Remove stopwords')
    parser.add_argument('--distance', dest='distance', default='euclidean', help='Distance metric to use')
    parser.add_argument('-k', dest='k', type=int, help='Number of neighbors for kNN')
    parser.add_argument('--mode', dest='mode', default='knn', choices=['knn', 'ncc'], help='Choose between kNN or NCC')
    parser.set_defaults(keep_punc=False, keep_stopwords=False)
    args = parser.parse_args()
    run_classifier(k=args.k, mode=args.mode, distance=args.distance, keep_punc=args.keep_punc, keep_stopwords=args.keep_stopwords)