import csv
from math import sqrt
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)
movies_data = read_csv('movie-ratings.csv')
movies = movies_data[0][1:]
movies_data.pop(0)
ratings = [{movies[i]: float(row[i + 1]) for i in range(len(movies))} for row in movies_data]
critic_names = [row[0] for row in movies_data]
user_data = read_csv('user_preference.csv')
user_preferences = {user_data[0][i]: float(user_data[1][i]) for i in range(len(user_data[0]))}
corr_coefficients = []
for critic in ratings:
    xy = []
    x = []
    y = []
    x_squares = []
    y_squares = []
    for movie_name, user_rating in user_preferences.items():
        critic_rating = critic.get(movie_name)
        if critic_rating is not None and user_rating != -1:
            xy.append(critic_rating * user_rating)
            x.append(critic_rating)
            y.append(user_rating)
            x_squares.append(critic_rating ** 2)
            y_squares.append(user_rating ** 2)
    n = len(xy)
    if n * sum(x_squares) - sum(x) * sum(x) != 0 and n * sum(y_squares) - sum(y) * sum(y) != 0:
        corr_coefficients.append((n * sum(xy) - sum(x) * sum(y)) / (sqrt(n * sum(x_squares) - sum(x) * sum(x)) * sqrt(n * sum(y_squares) - sum(y) * sum(y))))
    else:
        corr_coefficients.append(0)
pearson_order = sorted(zip(critic_names, corr_coefficients), key=lambda x: x[1], reverse=True)
movie_ratings = {}
for movie_name in movies:
    weighted_ratings = []
    sum_corr_coefficients = []
    for i, critic_rating in enumerate(ratings):
        if movie_name in critic_rating:
            weighted_ratings.append(corr_coefficients[i] * critic_rating[movie_name])
            sum_corr_coefficients.append(abs(corr_coefficients[i]))
    if sum_corr_coefficients:
        movie_ratings[movie_name] = sum(weighted_ratings) / sum(sum_corr_coefficients)
    else:
        movie_ratings[movie_name] = 0
rating_order = sorted(movie_ratings, key=movie_ratings.get, reverse=True)
count = 0
for movie_name in rating_order:
    if user_preferences[movie_name] == -1 and count < 3:
        print(movie_name)
        count += 1