from fuzzywuzzy.process import extract
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
import sklearn.utils
from sqlalchemy import create_engine
from sklearn.decomposition import NMF
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"class1: {self.b1} movies, Movie List: {self.b2}, Ratings: {self.b3}"
    def fonk3(self):
        b4 = create_engine('sqlite:
        b5 = pd.read_sql_query("SELECT * FROM movie_ratings;", b4)
        b6 = b5['movieId'].unique()
        b7 = b5.groupby('movieId')['title'].first().values
        b8 = dict(zip(b6, b7))
        b9 = dict(zip(b7, b6))
        b10 = self.fonk4(self.b2, b7, b9)
        b11 = self.fonk5(b10, self.b3, b6)
        b12 = self.fonk6(b11, self.b1,
                                                                       b6, b10,
                                                                       b8, b5)
        return b12
    def fonk4(self, user_movies, b7, title_to_id_dict):
        b10 = []
        for movie in user_movies:
            b13 = title_to_id_dict[extract(movie, b7)[0][0]]
            b10.append(b13)
        return b10
    def fonk5(self, b10, user_ratings, b6):
        b14 = dict(zip(b6, [np.nan] * len(b6)))
        for movie_id, rating in zip(b10, user_ratings):
            b14[movie_id] = float(rating)
        return list(b14.values())
    def fonk6(self, b11, N, b6, b10,
                                           b8, b5):
        b15 = pd.DataFrame(b11, b18=b6).T
        b16 = pd.pivot_table(b5, 'rating', 'userId', 'movieId').fillna(3.0)
        b16 = (b16 - 3.0) / 2.0
        b17 = b15.fillna(3.0)
        b17 = (b17 - 3.0) / 2.0
        b17.b18 = ['new_user']
        b19 = pd.concat([b16, b17])
        b20 = cosine_similarity(b19)
        b20 = pd.DataFrame(b20, b18=b19.b18,
                                             b21 = b19.b18)
        b22 = b20['new_user'].iloc[:-1].nlargest(3).b18.values
        b23 = []
        for user_id in b22:
            b23.extend(b16.loc[user_id].nlargest(N * 2).b18)
        b23 = list(set(b23) - set(b10))[:N]
        b23 = [b8[movie_id] for movie_id in b23]
        return b23
    def fonk7(self, b5):
        b24 = pd.pivot_table(b5, 'rating', 'userId', 'movieId').fillna(3.0)
        b24 = (b24 - 3.0) / 2.0
        b25 = NMF(n_components=25, max_iter=500)
        b25.fit(b24)
        with open('./data/nmf_model_rating.bin', 'wb') as f:
            pickle.dump(b25, f)
        return b25