import pandas as pd
ratings_df = pd.read_csv('u.data', sep='\t', names=['user_id', 'movie_id', 'rating'])
movies_df = pd.read_csv('u.item', sep='|', names=['movie_id', 'title'])
merged_df = pd.merge(movies_df, ratings_df)
user_ratings_pivot = merged_df.pivot_table(index='user_id', columns='title', values='rating')
corr_matrix = user_ratings_pivot.corr(method='pearson', min_periods=100)
user_id = 2
user_ratings = user_ratings_pivot.loc[user_id].dropna()
sim_candidates = pd.Series()
for movie_title, rating in user_ratings.items():
    similar_movies = corr_matrix[rating].dropna()
    similar_movies = similar_movies.map(lambda x: x * rating)
    sim_candidates = sim_candidates.append(similar_movies)
sim_candidates.sort_values(inplace=True, ascending=False)
sim_candidates = sim_candidates.groupby(sim_candidates.index).sum()
filtered_sims = sim_candidates.drop(user_ratings.index, errors='ignore')
print(filtered_sims.head())
filtered_sims.to_csv("filteredSims.csv")