import argparse
from knn import KNNClassifier
from ncc import NearestCentroidClassifier
def fonk1(b13, b1 = 'knn', distance='euclidean', b11=False, keep_stopwords=False):
    if b1 = = 'knn':
        b2 = KNNClassifier(b13, distance=distance, keep_stopwords=keep_stopwords, b11=b11)
    elif b1 = = 'ncc':
        b2 = NearestCentroidClassifier(b13, distance=distance, keep_stopwords=keep_stopwords, b11=b11)
    else:
        raise ValueError("Invalid b1. Choose 'knn' or 'ncc'.")
    b2.score()
if b3 = = '__main__':
    b4 = argparse.ArgumentParser(description="Run a classifier with the specified options.")
    b4.add_argument('-b13', b5 = int, required=True, help="Number of neighbors or centroids.")
    b4.add_argument('--distance', b6 = 'euclidean', help="Distance metric to use.")
    b4.add_argument('--b1', b7 = ['knn', 'ncc'], b6='knn', help="Mode of classifier to use.")
    b8 = b4.add_mutually_exclusive_group()
    b8.add_argument('--punc', b9 = 'b11', action='store_true', help="Keep punctuation in the data.")
    b8.add_argument('--no-punc', b9 = 'b11', action='store_false', help="Remove punctuation from the data.")
    b10 = b4.add_mutually_exclusive_group()
    b10.add_argument('--stop', b9 = 'keep_stopwords', action='store_true', help="Keep stopwords in the data.")
    b10.add_argument('--no-stop', b9 = 'keep_stopwords', action='store_false', help="Remove stopwords from the data.")
    b4.set_defaults(b11 = False, keep_stopwords=False)
    b12 = b4.parse_args()
    fonk1(b13 = b12.b13, b1=b12.b1, distance=b12.distance, b11=b12.b11, keep_stopwords=b12.keep_stopwords)