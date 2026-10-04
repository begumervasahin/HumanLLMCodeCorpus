import pandas as pd
ratings_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=ratings_cols, usecols=range(3))
movies_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=movies_cols, usecols=range(2))
ratings = pd.merge(movies, ratings)
user_ratings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
corr_matrix = user_ratings.corr(method='pearson', min_periods=100)
user_id = 2
my_ratings = user_ratings.loc[user_id].dropna()
similar_candidates = pd.Series()
for i in range(len(my_ratings.index)):
    similarities = corr_matrix[my_ratings.index[i]].dropna()
    similarities = similarities.map(lambda x: x * my_ratings[i])
    similar_candidates = similar_candidates.append(similarities)
similar_candidates.sort_values(inplace=True, ascending=False)
similar_candidates = similar_candidates.groupby(similar_candidates.index).sum()
similar_candidates.sort_values(inplace=True, ascending=False)
filtered_sims = similar_candidates.drop(my_ratings.index, errors='ignore')
print(filtered_sims.head())
filtered_sims.to_csv("filteredSims.csv")