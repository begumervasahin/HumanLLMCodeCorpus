
from surprise import Dataset, Reader
import numpy as np
from six import iteritems
def mean_centered_ratings(dataset_path):
    file_path = dataset_path
    reader = Reader(line_format='user item rating', rating_scale=(1, 7), sep='\t')
    data = Dataset.load_from_file(file_path, reader)
    trainset = data.build_full_trainset()
    number_users = trainset.n_users
    number_items = trainset.n_items
    user_ratings = trainset.ur
    u_matrix = np.zeros((number_users, number_items), dtype=float)
    avg_rating = np.zeros((number_users, 3), dtype=float)
    avg_matrix = np.zeros((number_users, number_items), dtype=float)
    for user, item_ratings in iteritems(user_ratings):
        for item, rating in item_ratings:
            if rating == 0:
                u_matrix[user, item] += 0
            else:
                u_matrix[user, item] += rating
                avg_rating[user, 1] += rating
                avg_rating[user, 2] += 1
    print('Original user ratings:\n', u_matrix, '\n')
    for user, item_ratings in iteritems(user_ratings):
        for item, rating in item_ratings:
            if rating == 0:
                avg_matrix[user, item] += 0
            else:
                avg_matrix[user, item] += avg_rating[user, 1] / avg_rating[user, 2]
    mean_matrix = u_matrix - avg_matrix
    return mean_matrix
file_path = 'data/table2.1_ratings.txt'
mean_centered = mean_centered_ratings(file_path)
print('The mean centered ratings:\n', mean_centered)