
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
    avg_rating_sum = np.zeros((number_users, 1), dtype=float)
    avg_rating_count = np.zeros((number_users, 1), dtype=int)
    avg_matrix = np.zeros((number_users, number_items), dtype=float)
    for user, item_ratings in iteritems(user_ratings):
        for item, rating in item_ratings:
            if rating != 0:
                u_matrix[user, item] += rating
                avg_rating_sum[user] += rating
                avg_rating_count[user] += 1
    print('Original user ratings:\n', u_matrix, '\n')
    for user, item_ratings in iteritems(user_ratings):
        for item, rating in item_ratings:
            if rating != 0:
                avg_matrix[user, item] += avg_rating_sum[user] / avg_rating_count[user]
    mean_centered_matrix = u_matrix - avg_matrix
    return mean_centered_matrix
file_path = 'data/table2.1_ratings.txt'
mean_centered = mean_centered_ratings(file_path)
print('The mean centered ratings:\n', mean_centered)