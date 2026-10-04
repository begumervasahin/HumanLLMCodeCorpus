import argparse
from knn import KNNClassifier
from ncc import NearestCentroidClassifier
def fonk1(b12, b1 = 'knn', distance='euclidean', b10=False, keep_stopwords=False):
    if b1 = = 'knn':
        b2 = KNNClassifier(b12, distance=distance, keep_stopwords=keep_stopwords, b10=b10)
    elif b1 = = 'ncc':
        b2 = NearestCentroidClassifier(b12, distance=distance, keep_stopwords=keep_stopwords, b10=b10)
    else:
        raise ValueError("Invalid b1. Choose 'knn' or 'ncc'.")
    b2.score()
def fonk2():
    b3 = argparse.ArgumentParser(description="Run a classifier with the specified options.")
    b3.add_argument('-b12', b4 = int, required=True, help="Number of neighbors or centroids.")
    b3.add_argument('--distance', b5 = 'euclidean', help="Distance metric to use.")
    b3.add_argument('--b1', b6 = ['knn', 'ncc'], b5='knn', help="Mode of classifier to use.")
    b7 = b3.add_mutually_exclusive_group()
    b7.add_argument('--punc', b8 = 'b10', action='store_true', help="Keep punctuation in the data.")
    b7.add_argument('--no-punc', b8 = 'b10', action='store_false', help="Remove punctuation from the data.")
    b9 = b3.add_mutually_exclusive_group()
    b9.add_argument('--stop', b8 = 'keep_stopwords', action='store_true', help="Keep stopwords in the data.")
    b9.add_argument('--no-stop', b8 = 'keep_stopwords', action='store_false', help="Remove stopwords from the data.")
    b3.set_defaults(b10 = False, keep_stopwords=False)
    b11 = b3.parse_args()
    fonk1(b12 = b11.b12, b1=b11.b1, distance=b11.distance, b10=b11.b10, keep_stopwords=b11.keep_stopwords)
if b13 = = '__main__':
    fonk2()