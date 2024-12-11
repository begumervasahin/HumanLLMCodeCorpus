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
        return f"The User will have {self.b1} movies recommended, " \
               f"his movie list is {self.b2} with rating {self.b3}"
    def fonk3(self):
        b4 = create_engine('sqlite:
        b5 = pd.read_sql_query("SELECT * FROM movie_ratings;", b4)
        b6 = b5['movieId'].unique()
        b7 = b5.groupby('movieId')['title'].first().values
        b8 = dict(zip(b6, b7))
        b9 = dict(zip(b7, b6))
        b10 = self.fonk4(self.b2, b7, b9)
        b11 = self.fonk5(b10, self.b3, b6)
        b12 = self.fonk6(b11, self.b1, b6,
                                                    b10, b8, b5)
        return b12
    def fonk4(self, user_movie, b7, title_to_id_dictionary):
        b13 = []
        for m in user_movie:
            b14 = title_to_id_dictionary[extract(m, b7)[0][0]]
            b13.append(b14)
        return b13
    def fonk5(self, b10, user_ratings, b6):
        b15 = [np.nan] * len(b6)
        b16 = dict(zip(b6, b15))
        for u_movie_id, u_rating in zip(b10, user_ratings):
            b16[u_movie_id] = float(u_rating)
        b11 = list(b16.values())
        return b11
    def fonk6(self, b11, N, b6, b10, b8, b5):
        b11 = pd.DataFrame(b11, b20=b6).T
        b17 = pd.pivot_table(b5, 'rating', 'userId', 'movieId')
        b17.fillna(3.0, b18 = True)
        b17 = (b17 - 3.0) / 2.0
        b19 = b11.fillna(3.0)
        b19 = (b19 - 3.0) / 2.0
        b19.b20 = ['new_user']
        b21 = pd.concat([b17, b19])
        b22 = cosine_similarity(b21)
        b22 = pd.DataFrame(b22, b20=b21.b20, columns=b21.b20)
        b23 = b22['new_user'].iloc[:-1]
        b24 = b23.nlargest(3).b20.values
        b25 = []
        b26 = []
        for id_user in b24:
            b25.extend(b17.loc[id_user].nlargest(N * 2).b20)
            b26.extend(b17.loc[id_user].nlargest(N * 2).values)
        b27 = {'id_movie': b25, 'score': b26}
        b27 = pd.DataFrame(b27)
        b27 = sklearn.utils.shuffle(b27)
        b27 = b27.sort_values(by='score', ascending=False)
        b28 = b27['id_movie'].unique()
        b29 = []
        for id_nb in b28:
            if (id_nb not in b10) and (len(b29) < N):
                b29.append(b8[id_nb])
        return b29
    def fonk7(self, b11, N, b6, b8, b5):
        b30 = './data/'
        if not os.path.exists(b30 + 'nmf_model_rating.bin'):
            b31 = self.train_nmf_model(b5)
        else:
            b32 = open(b30 + 'nmf_model_rating.bin', 'rb').read()
            b31 = pickle.loads(b32)
        b11 = pd.DataFrame(b11, b20=b6).T
        b33 = b11.fillna(2.5)
        b34 = b31.transform(b33)
        b35 = b31.inverse_transform(b34)
        b36 = pd.DataFrame(b35.reshape(-1), b20=b6).T
        b37 = np.isnan(b11)
        b38 = b36[b37]
        b39 = b38.T.sort_values(by=[0], ascending=False).b20