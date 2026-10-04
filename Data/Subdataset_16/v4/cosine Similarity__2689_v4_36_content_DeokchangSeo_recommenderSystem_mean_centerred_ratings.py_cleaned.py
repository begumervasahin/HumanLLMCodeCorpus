
from surprise import Dataset, Reader
from numpy import zeros
from six import iteritems
def fonk1(dataset_path):
    b1 = dataset_path
    b2 = Reader(line_format='user item rating', rating_scale=(1, 7), sep='\t')
    b3 = Dataset.load_from_file(b1, b2)
    b4 = b3.build_full_trainset()
    b5 = b4.n_users
    b6 = b4.n_items
    b7 = b4.ur
    b8 = zeros((b5, b6), dtype=float)
    b9 = zeros((b5, 3), dtype=float)
    b10 = zeros((b5, b6), dtype=float)
    for user, ratings in iteritems(b7):
        for item, rating in ratings:
            if rating != 0:
                b8[user, item] += rating
                b9[user, 1] += rating
                b9[user, 2] += 1
    print('Original user ratings:\n', b8, '\n')
    for user, ratings in iteritems(b7):
        for item, rating in ratings:
            if rating != 0:
                b10[user, item] += b9[user, 1] / b9[user, 2]
    b11 = b8 - b10
    return b11
b1 = 'b3/table2.1_ratings.txt'
b12 = fonk1(b1)
print('The mean centered ratings:\n', b12)