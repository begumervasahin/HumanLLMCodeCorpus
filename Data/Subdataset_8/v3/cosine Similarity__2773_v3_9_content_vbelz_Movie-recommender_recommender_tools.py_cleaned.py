from fuzzywuzzy.process import extract
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
import sklearn.utils
from sqlalchemy import create_engine
from sklearn.decomposition import NMF
class Recommender:
    def __init__(self, nb_movies, movie_list, ratings_list):
        self.nb_movies = nb_movies
        self.movie_list = movie_list
        self.ratings_list = ratings_list
    def __repr__(self):
        return f"Recommender: {self.nb_movies} movies, Movie List: {self.movie_list}, Ratings: {self.ratings_list}"
    def read_db_get_predictions(self):
        engine = create_engine('sqlite:
        df_data = pd.read_sql_query("SELECT * FROM movie_ratings;", engine)
        list_id_movies = df_data['movieId'].unique()
        list_title_movies = df_data.groupby('movieId')['title'].first().values
        movie_id_to_title_dict = dict(zip(list_id_movies, list_title_movies))
        title_to_movie_id_dict = dict(zip(list_title_movies, list_id_movies))
        user_movie_ids = self.get_movie_id_for_user(self.movie_list, list_title_movies, title_to_movie_id_dict)
        user_ratings_vector = self.create_user_ratings_vector(user_movie_ids, self.ratings_list, list_id_movies)
        movies_to_recommend = self.recommend_movies_cosine_similarity(user_ratings_vector, self.nb_movies,
                                                                       list_id_movies, user_movie_ids,
                                                                       movie_id_to_title_dict, df_data)
        return movies_to_recommend
    def get_movie_id_for_user(self, user_movies, list_title_movies, title_to_id_dict):
        user_movie_ids = []
        for movie in user_movies:
            id_movie = title_to_id_dict[extract(movie, list_title_movies)[0][0]]
            user_movie_ids.append(id_movie)
        return user_movie_ids
    def create_user_ratings_vector(self, user_movie_ids, user_ratings, list_id_movies):
        ratings_dict = dict(zip(list_id_movies, [np.nan] * len(list_id_movies)))
        for movie_id, rating in zip(user_movie_ids, user_ratings):
            ratings_dict[movie_id] = float(rating)
        return list(ratings_dict.values())
    def recommend_movies_cosine_similarity(self, user_ratings_vector, N, list_id_movies, user_movie_ids,
                                           movie_id_to_title_dict, df_data):
        user_ratings_df = pd.DataFrame(user_ratings_vector, index=list_id_movies).T
        ratings_matrix = pd.pivot_table(df_data, 'rating', 'userId', 'movieId').fillna(3.0)
        ratings_matrix = (ratings_matrix - 3.0) / 2.0
        user_ratings_filled = user_ratings_df.fillna(3.0)
        user_ratings_filled = (user_ratings_filled - 3.0) / 2.0
        user_ratings_filled.index = ['new_user']
        ratings_matrix_with_user = pd.concat([ratings_matrix, user_ratings_filled])
        cos_similarity_matrix = cosine_similarity(ratings_matrix_with_user)
        cos_similarity_matrix = pd.DataFrame(cos_similarity_matrix, index=ratings_matrix_with_user.index,
                                             columns=ratings_matrix_with_user.index)
        similar_users = cos_similarity_matrix['new_user'].iloc[:-1].nlargest(3).index.values
        recommended_movies = []
        for user_id in similar_users:
            recommended_movies.extend(ratings_matrix.loc[user_id].nlargest(N * 2).index)
        recommended_movies = list(set(recommended_movies) - set(user_movie_ids))[:N]
        recommended_movies = [movie_id_to_title_dict[movie_id] for movie_id in recommended_movies]
        return recommended_movies
    def train_nmf_model(self, df_data):
        df_pivot = pd.pivot_table(df_data, 'rating', 'userId', 'movieId').fillna(3.0)
        df_pivot = (df_pivot - 3.0) / 2.0
        model = NMF(n_components=25, max_iter=500)
        model.fit(df_pivot)
        with open('./data/nmf_model_rating.bin', 'wb') as f:
            pickle.dump(model, f)
        return model