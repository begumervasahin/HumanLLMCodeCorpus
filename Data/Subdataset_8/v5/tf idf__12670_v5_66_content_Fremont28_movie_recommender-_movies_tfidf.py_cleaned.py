import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies_df = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print("First few rows of the dataset:")
print(movies_df.head(3))
total_movies_count = len(movies_df)
movie_popularity = movies_df.groupby('original_title')['popularity'].count().reset_index()
unique_movie_titles_count = len(movie_popularity)
unique_languages = movies_df['original_language'].unique()
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
movies_df['overview'] = movies_df['overview'].fillna('')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['overview'])
tfidf_matrix_shape = tfidf_matrix.shape
cosine_similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
movie_indices = pd.Series(movies_df.index, index=movies_df['original_title']).drop_duplicates()
def get_similar_movies(title, cosine_sim=cosine_similarity_matrix):
    movie_index = movie_indices[title]
    similarity_scores = list(enumerate(cosine_sim[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:20]
    similar_movie_indices = [index[0] for index in similarity_scores]
    return movies_df['original_title'].iloc[similar_movie_indices]
recommended_movies = get_similar_movies("No Reservations")
print("\nRecommended movies for 'No Reservations':")
print(recommended_movies)