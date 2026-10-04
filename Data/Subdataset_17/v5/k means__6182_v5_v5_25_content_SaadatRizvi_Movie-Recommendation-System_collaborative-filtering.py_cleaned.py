import pandas as pd
def load_data():
    ratings_cols = ['user_id', 'movie_id', 'rating']
    movies_cols = ['movie_id', 'title']
    ratings = pd.read_csv('u.data', sep='\t', names=ratings_cols, usecols=range(3))
    movies = pd.read_csv('u.item', sep='|', names=movies_cols, usecols=range(2))
    return ratings, movies
def merge_data(ratings, movies):
    return pd.merge(movies, ratings)
def create_user_ratings_pivot(ratings):
    return ratings.pivot_table(index='user_id', columns='title', values='rating')
def calculate_correlation_matrix(user_ratings):
    return user_ratings.corr(method='pearson', min_periods=100)
def get_user_ratings(user_ratings, user_id):
    return user_ratings.loc[user_id].dropna()
def find_similar_movies(user_ratings, my_ratings, corr_matrix):
    similar_candidates = pd.Series()
    for movie in my_ratings.index:
        similarities = corr_matrix[movie].dropna()
        similarities = similarities.map(lambda x: x * my_ratings[movie])
        similar_candidates = similar_candidates.append(similarities)
    similar_candidates = similar_candidates.groupby(similar_candidates.index).sum()
    similar_candidates.sort_values(inplace=True, ascending=False)
    return similar_candidates
def filter_already_rated_movies(similar_candidates, my_ratings):
    return similar_candidates.drop(my_ratings.index, errors='ignore')
def main(user_id):
    ratings, movies = load_data()
    ratings = merge_data(ratings, movies)
    user_ratings = create_user_ratings_pivot(ratings)
    corr_matrix = calculate_correlation_matrix(user_ratings)
    my_ratings = get_user_ratings(user_ratings, user_id)
    similar_candidates = find_similar_movies(user_ratings, my_ratings, corr_matrix)
    recommended_movies = filter_already_rated_movies(similar_candidates, my_ratings)
    print(recommended_movies.head())
    recommended_movies.to_csv("filteredSims.csv")
if __name__ == "__main__":
    main(user_id=2)