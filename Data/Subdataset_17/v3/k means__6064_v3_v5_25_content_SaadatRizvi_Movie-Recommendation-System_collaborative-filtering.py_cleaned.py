import pandas as pd
def load_data(ratings_path, movies_path):
    ratings_cols = ['user_id', 'movie_id', 'rating']
    ratings = pd.read_csv(ratings_path, sep='\t', names=ratings_cols, usecols=range(3))
    movies_cols = ['movie_id', 'title']
    movies = pd.read_csv(movies_path, sep='|', names=movies_cols, usecols=range(2))
    return pd.merge(movies, ratings)
def create_user_ratings_pivot(ratings):
    return ratings.pivot_table(index='user_id', columns='title', values='rating')
def calculate_correlation_matrix(user_ratings):
    return user_ratings.corr(method='pearson', min_periods=100)
def get_user_ratings(user_ratings, user_id):
    return user_ratings.loc[user_id].dropna()
def find_similar_movies(corr_matrix, my_ratings):
    similar_candidates = pd.Series(dtype=float)
    for movie in my_ratings.index:
        similarities = corr_matrix[movie].dropna()
        similarities = similarities.map(lambda x: x * my_ratings[movie])
        similar_candidates = similar_candidates.append(similarities)
    similar_candidates = similar_candidates.groupby(similar_candidates.index).sum()
    similar_candidates.sort_values(inplace=True, ascending=False)
    return similar_candidates.drop(my_ratings.index, errors='ignore')
def main():
    ratings_path = 'u.data'
    movies_path = 'u.item'
    user_id = 2
    ratings = load_data(ratings_path, movies_path)
    user_ratings = create_user_ratings_pivot(ratings)
    corr_matrix = calculate_correlation_matrix(user_ratings)
    my_ratings = get_user_ratings(user_ratings, user_id)
    filtered_sims = find_similar_movies(corr_matrix, my_ratings)
    print(filtered_sims.head())
    filtered_sims.to_csv("filteredSims.csv")
if __name__ == "__main__":
    main()