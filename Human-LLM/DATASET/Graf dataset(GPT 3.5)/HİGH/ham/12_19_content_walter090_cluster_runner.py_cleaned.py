def fonk1(b12,
        b1 = 'knn',
        b2 = 'euclidean',
        b3 = False,
        b4 = False):
    from knn import KNNClassifier
    from ncc import NearestCentroidClassifier
    if b1 = = 'knn':
        b5 = KNNClassifier(b12, b2=b2, b4=b4, b3=b3)
        b5.score()
    elif b1 = = 'ncc':
        b5 = NearestCentroidClassifier(b12, b2=b2, b4=b4, b3=b3)
        b5.score()
if b6 = = '__main__':
    import argparse
    b7 = argparse.ArgumentParser()
    b8 = b7.add_mutually_exclusive_group()
    b8.add_argument('--punc', b9 = 'b3', action='store_true')
    b8.add_argument('--no-punc', b9 = 'b3', action='store_false')
    b10 = b7.add_mutually_exclusive_group()
    b10.add_argument('--stop', b9 = 'b4', action='store_true')
    b10.add_argument('--no-stop', b9 = 'b4', action='store_false')
    b7.add_argument('--b2', b9 = 'b2', default='euclidean')
    b7.add_argument('-b12', b9 = 'b12')
    b7.set_defaults(b3 = False, b4=False)
    b11 = b7.parse_args()
    fonk1(b12 = b11.b12, b2=b11.b2, b3=b11.b3, b4=b11.b4)