
from surprise import Dataset, Reader
import numpy as np
from six import iteritems
def fonk1(dataset_path):
    b1 = dataset_path
    b2 = Reader(line_format='user item b11', rating_scale=(1, 7), sep='\t')
    b3 = Dataset.load_from_file(b1, b2)
    b4 = b3.build_full_trainset()
    b5 = b4.n_users
    b6 = b4.n_items
    b7 = b4.ur
    b8 = np.zeros((b5, b6), dtype=float)
    b9 = np.zeros((b5, 3), dtype=float)
    b10 = np.zeros((b5, b6), dtype=float)
    for user, item_ratings in iteritems(b7):
        for item, b11 in item_ratings:
            if b11 = = 0:
                b8[user, item] += 0
            else:
                b8[user, item] += b11
                b9[user, 1] += b11
                b9[user, 2] += 1
    print('Original user ratings:\n', b8, '\n')
    for user, item_ratings in iteritems(b7):
        for item, b11 in item_ratings:
            if b11 = = 0:
                b10[user, item] += 0
            else:
                b10[user, item] += b9[user, 1] / b9[user, 2]
    b12 = b8 - b10
    return b12
b1 = 'b3/table2.1_ratings.txt'
b13 = fonk1(b1)
print('The mean centered ratings:\n', b13)