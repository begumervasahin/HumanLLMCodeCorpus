import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies_data = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print("First few rows of the dataset:")
print(movies_data.head(3))
total_movies = len(movies_data)
print("Total number of movies in the dataset:", total_movies)
unique_movie_titles = len(movies_data['original_title'].unique())
print("Number of unique movie titles:", unique_movie_titles)
unique_languages = movies_data['original_language'].unique()
print("Unique languages in the dataset:", unique_languages)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
movies_data['overview'] = movies_data['overview'].fillna('')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_data['overview'])
print("TF-IDF matrix shape:", tfidf_matrix.shape)
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
movie_indices = pd.Series(movies_data.index, index=movies_data['original_title']).drop_duplicates()
def get_recommendations(movie_title, cosine_similarities=cosine_similarities):
    movie_index = movie_indices[movie_title]
    similarity_scores = list(enumerate(cosine_similarities[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similar_movies_indices = [index[0] for index in similarity_scores[1:20]]
    return movies_data['original_title'].iloc[similar_movies_indices]
recommendations = get_recommendations("No Reservations")
print("Recommendations for 'No Reservations':")
print(recommendations)