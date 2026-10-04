import argparse
def fonk1(b9, b1 = 'knn', distance='euclidean', b7=False, keep_stopwords=False):
    from knn import KNNClassifier
    from ncc import NearestCentroidClassifier
    if b1 = = 'knn':
        b2 = KNNClassifier(b9, distance=distance, keep_stopwords=keep_stopwords, b7=b7)
    elif b1 = = 'ncc':
        b2 = NearestCentroidClassifier(b9, distance=distance, keep_stopwords=keep_stopwords, b7=b7)
    b2.score()
def fonk2():
    b3 = argparse.ArgumentParser(description="Run KNN or Nearest Centroid Classifier.")
    b4 = b3.add_mutually_exclusive_group()
    b4.add_argument('--punc', b5 = 'b7', action='store_true', help="Keep punctuation in the text.")
    b4.add_argument('--no-punc', b5 = 'b7', action='store_false', help="Remove punctuation from the text.")
    b6 = b3.add_mutually_exclusive_group()
    b6.add_argument('--stop', b5 = 'keep_stopwords', action='store_true', help="Keep stopwords in the text.")
    b6.add_argument('--no-stop', b5 = 'keep_stopwords', action='store_false', help="Remove stopwords from the text.")
    b3.add_argument('--distance', b5 = 'distance', default='euclidean', help="Distance metric to use.")
    b3.add_argument('-b9', b5 = 'b9', type=int, required=True, help="Number of neighbors or centroids.")
    b3.add_argument('--b1', b5 = 'b1', default='knn', choices=['knn', 'ncc'], help="Classifier b1 to use.")
    b3.set_defaults(b7 = False, keep_stopwords=False)
    b8 = b3.parse_args()
    fonk1(b9 = b8.b9, b1=b8.b1, distance=b8.distance, b7=b8.b7, keep_stopwords=b8.keep_stopwords)
if b10 = = '__main__':
    fonk2()