import argparse
from knn import KNNClassifier
from ncc import NearestCentroidClassifier
def run_classifier(k, mode='knn', distance='euclidean', keep_punc=False, keep_stopwords=False):
    if mode == 'knn':
        clf = KNNClassifier(k, distance=distance, keep_stopwords=keep_stopwords, keep_punc=keep_punc)
    elif mode == 'ncc':
        clf = NearestCentroidClassifier(k, distance=distance, keep_stopwords=keep_stopwords, keep_punc=keep_punc)
    else:
        raise ValueError("Invalid mode. Choose 'knn' or 'ncc'.")
    clf.score()
def main():
    parser = argparse.ArgumentParser(description="Run a classifier with the specified options.")
    parser.add_argument('-k', type=int, required=True, help="Number of neighbors or centroids.")
    parser.add_argument('--distance', default='euclidean', help="Distance metric to use.")
    parser.add_argument('--mode', choices=['knn', 'ncc'], default='knn', help="Mode of classifier to use.")
    punc_group = parser.add_mutually_exclusive_group()
    punc_group.add_argument('--punc', dest='keep_punc', action='store_true', help="Keep punctuation in the data.")
    punc_group.add_argument('--no-punc', dest='keep_punc', action='store_false', help="Remove punctuation from the data.")
    stop_group = parser.add_mutually_exclusive_group()
    stop_group.add_argument('--stop', dest='keep_stopwords', action='store_true', help="Keep stopwords in the data.")
    stop_group.add_argument('--no-stop', dest='keep_stopwords', action='store_false', help="Remove stopwords from the data.")
    parser.set_defaults(keep_punc=False, keep_stopwords=False)
    args = parser.parse_args()
    run_classifier(k=args.k, mode=args.mode, distance=args.distance, keep_punc=args.keep_punc, keep_stopwords=args.keep_stopwords)
if __name__ == '__main__':
    main()