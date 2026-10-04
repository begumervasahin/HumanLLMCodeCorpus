import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
cinema = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print(cinema.head(3))
print(len(cinema))
movie_grouped = cinema.groupby(['original_title']).agg({'popularity': 'count'}).reset_index()
movie_count = cinema['original_title'].unique()
print(len(movie_count))
lengua_count = cinema['original_language'].unique()
print(lengua_count)
tfidf = TfidfVectorizer(stop_words='english')
cinema['overview'] = cinema['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(cinema['overview'])
print(tfidf_matrix.shape)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(cinema.index, index=cinema['original_title']).drop_duplicates()
def get_recs(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:20]
    movie_indices = [i[0] for i in sim_scores]
    return cinema['original_title'].iloc[movie_indices]
print(get_recs("No Reservations"))