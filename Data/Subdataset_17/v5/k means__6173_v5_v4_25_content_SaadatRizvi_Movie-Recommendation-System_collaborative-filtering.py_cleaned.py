import pandas as pd
def load_and_merge_data(ratings_file, movies_file):
    ratings_cols = ['user_id', 'movie_id', 'rating']
    movies_cols = ['movie_id', 'title']
    ratings = pd.read_csv(ratings_file, sep='\t', names=ratings_cols, usecols=range(3))
    movies = pd.read_csv(movies_file, sep='|', names=movies_cols, usecols=range(2))
    return pd.merge(movies, ratings)
def create_user_ratings_pivot(ratings):
    return ratings.pivot_table(index='user_id', columns='title', values='rating')
def calculate_correlation_matrix(user_ratings, min_periods=100):
    return user_ratings.corr(method='pearson', min_periods=min_periods)
def find_similar_movies(user_ratings, corr_matrix, user_id):
    my_ratings = user_ratings.loc[user_id].dropna()
    similar_candidates = pd.Series(dtype='float64')
    for movie in my_ratings.index:
        similarities = corr_matrix[movie].dropna()
        similarities = similarities.map(lambda x: x * my_ratings[movie])
        similar_candidates = similar_candidates.append(similarities)
    similar_candidates = similar_candidates.groupby(similar_candidates.index).sum()
    similar_candidates.sort_values(inplace=True, ascending=False)
    return similar_candidates.drop(my_ratings.index, errors='ignore')
def main():
    ratings_file = 'u.data'
    movies_file = 'u.item'
    user_id = 2
    ratings = load_and_merge_data(ratings_file, movies_file)
    user_ratings = create_user_ratings_pivot(ratings)
    corr_matrix = calculate_correlation_matrix(user_ratings)
    similar_movies = find_similar_movies(user_ratings, corr_matrix, user_id)
    print(similar_movies.head())
    similar_movies.to_csv("filteredSims.csv")
if __name__ == "__main__":
    main()