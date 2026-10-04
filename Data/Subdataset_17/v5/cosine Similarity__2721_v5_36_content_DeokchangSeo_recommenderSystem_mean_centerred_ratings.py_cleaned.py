
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
    sum_ratings = np.zeros(number_users, dtype=float)
    count_ratings = np.zeros(number_users, dtype=int)
    for user, ratings in iteritems(user_ratings):
        for item, rating in ratings:
            if rating != 0:
                u_matrix[user, item] += rating
                sum_ratings[user] += rating
                count_ratings[user] += 1
    print('Original user ratings:\n', u_matrix, '\n')
    avg_matrix = np.zeros((number_users, number_items), dtype=float)
    for user, ratings in iteritems(user_ratings):
        for item, _ in ratings:
            if u_matrix[user, item] != 0:
                avg_matrix[user, item] = sum_ratings[user] / count_ratings[user]
    mean_centered_matrix = u_matrix - avg_matrix
    return mean_centered_matrix
file_path = 'data/table2.1_ratings.txt'
mean_centered = mean_centered_ratings(file_path)
print('The mean centered ratings:\n', mean_centered)