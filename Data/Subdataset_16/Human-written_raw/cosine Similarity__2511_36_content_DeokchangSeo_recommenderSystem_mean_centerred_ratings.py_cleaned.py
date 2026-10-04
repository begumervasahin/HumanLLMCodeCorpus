
from __future__ import (absolute_import, division, print_function, unicode_literals)
from surprise import Dataset, Reader
from numpy import *
from six import iteritems
def fonk1(dataset_path):
    b1 = dataset_path
    b2 = Reader(line_format= 'user item rating', rating_scale=(1, 7), sep='\t')
    b3 = Dataset.load_from_file(b1, b2)
    b4 = b3.build_full_trainset()
    b5 = b4.n_users
    b6 = b4.n_items
    b7 = b4.ur
    b8 = b4.ir
    b9 = b5
    b10 = b6
    b11 = zeros((b9, b10), float)
    b12 = zeros((b9, 3), float)
    b13 = zeros((b9, b10), float)
    for y, y_ratings in iteritems(b7):
        for xi, b14 in y_ratings:
            if b14 = = 0:
                b11[y, xi] += 0
            else:
        	    b11[y, xi] += b14
        	    b12[y, 1] += b14
        	    b12[y, 2] += 1
    print ('Original user ratings\n', b11, '\n')
    for y, y_ratings in iteritems(b7):
        for xi, b14 in y_ratings:
            if b14 = = 0:
                b13[y, xi] += 0
            else:
        	    b13[y, xi] += b12[y, 1]/b12[y, 2]
    b15 = b11-b13
    return b15
b1 = 'b3/table2.1_ratings.txt'
print ('The mean centerred ratings\n', fonk1(b1))