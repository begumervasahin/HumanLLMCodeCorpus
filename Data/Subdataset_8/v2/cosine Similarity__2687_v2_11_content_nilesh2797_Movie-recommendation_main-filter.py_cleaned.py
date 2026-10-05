import csv
from math import sqrt
with open('movie-ratings.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    data = list(reader1)
movies = data[0][1:]
data.pop(0)
ratings = []
critic_names = []
for item in data:
    critic_names.append(item[0])
    ratings.append({movies[i]: float(item[i + 1]) for i in range(len(movies))})
with open('user_preference.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    user_data = list(reader2)
user_preferences = {user_data[0][i]: float(user_data[1][i]) for i in range(len(user_data[0]))}
corr_coefficients = []
for critic in ratings:
    xy = []
    x = []
    y = []
    x_squares = []
    y_squares = []
    for movie_name in user_preferences.keys():
        if critic.get(movie_name) is not None and user_preferences[movie_name] != -1:
            xy.append(critic[movie_name] * user_preferences[movie_name])
            x.append(critic[movie_name])
            y.append(user_preferences[movie_name])
            x_squares.append(critic[movie_name] ** 2)
            y_squares.append(user_preferences[movie_name] ** 2)
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
    for i in range(len(corr_coefficients)):
        if ratings[i].get(movie_name) is not None:
            weighted_ratings.append(corr_coefficients[i] * ratings[i][movie_name])
            sum_corr_coefficients.append(abs(corr_coefficients[i]))
    movie_ratings[movie_name] = sum(weighted_ratings) / sum(sum_corr_coefficients)
top_recommendations = sorted(movie_ratings, key=movie_ratings.get, reverse=True)
count = 0
for movie_name in top_recommendations:
    if user_preferences[movie_name] == -1 and count < 3:
        print(movie_name)
        count += 1