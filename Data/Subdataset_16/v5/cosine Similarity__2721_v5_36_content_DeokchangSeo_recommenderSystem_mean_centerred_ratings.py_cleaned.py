
from surprise import Dataset, Reader
import numpy as np
from six import iteritems
def fonk1(dataset_path):
    b1 = dataset_path
    b2 = Reader(line_format='user item rating', rating_scale=(1, 7), sep='\t')
    b3 = Dataset.load_from_file(b1, b2)
    b4 = b3.build_full_trainset()
    b5 = b4.n_users
    b6 = b4.n_items
    b7 = b4.ur
    b8 = np.zeros((b5, b6), dtype=float)
    b9 = np.zeros(b5, dtype=float)
    b10 = np.zeros(b5, dtype=int)
    for user, ratings in iteritems(b7):
        for item, rating in ratings:
            if rating != 0:
                b8[user, item] += rating
                b9[user] += rating
                b10[user] += 1
    print('Original user ratings:\n', b8, '\n')
    b11 = np.zeros((b5, b6), dtype=float)
    for user, ratings in iteritems(b7):
        for item, _ in ratings:
            if b8[user, item] != 0:
                b11[user, item] = b9[user] / b10[user]
    b12 = b8 - b11
    return b12
b1 = 'b3/table2.1_ratings.txt'
b13 = fonk1(b1)
print('The mean centered ratings:\n', b13)