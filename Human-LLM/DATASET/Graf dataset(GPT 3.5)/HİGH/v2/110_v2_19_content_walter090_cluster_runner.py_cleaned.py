import argparse
from knn import KNNClassifier
from ncc import NearestCentroidClassifier
def fonk1(b10, b1 = 'knn', distance='euclidean', b8=False, keep_stopwords=False):
    if b1 = = 'knn':
        b2 = KNNClassifier(b10, distance=distance, keep_stopwords=keep_stopwords, b8=b8)
    elif b1 = = 'ncc':
        b2 = NearestCentroidClassifier(b10, distance=distance, keep_stopwords=keep_stopwords, b8=b8)
    b2.score()
if b3 = = '__main__':
    b4 = argparse.ArgumentParser()
    b5 = b4.add_mutually_exclusive_group()
    b5.add_argument('--punc', b6 = 'b8', action='store_true', help='Keep punctuation')
    b5.add_argument('--no-punc', b6 = 'b8', action='store_false', help='Remove punctuation')
    b7 = b4.add_mutually_exclusive_group()
    b7.add_argument('--stop', b6 = 'keep_stopwords', action='store_true', help='Keep stopwords')
    b7.add_argument('--no-stop', b6 = 'keep_stopwords', action='store_false', help='Remove stopwords')
    b4.add_argument('--distance', b6 = 'distance', default='euclidean', help='Distance metric to use')
    b4.add_argument('-b10', b6 = 'b10', help='Number of neighbors for kNN')
    b4.set_defaults(b8 = False, keep_stopwords=False)
    b9 = b4.parse_args()
    fonk1(b10 = b9.b10, distance=b9.distance, b8=b9.b8, keep_stopwords=b9.keep_stopwords)