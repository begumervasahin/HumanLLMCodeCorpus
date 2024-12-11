from fuzzywuzzy.process import extract
import numpy as np
import pandas as pd
import pickle
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
        b13 = [title_to_id_dictionary[extract(m, b7)[0][0]] for m in user_movie]
        return b13
    def fonk5(self, b10, user_ratings, b6):
        b14 = dict(zip(b6, [float(r) for r in user_ratings]))
        b11 = [b14.get(m, np.nan) for m in b6]
        return b11
    def fonk6(self, b11, N, b6, b10, b8, b5):
        b15 = pd.DataFrame(b11, b18=b6).T
        b16 = pd.pivot_table(b5, 'rating', 'userId', 'movieId').fillna(3.0)
        b16 = (b16 - 3.0) / 2.0
        b17 = b15.fillna(3.0) / 2.0
        b17.b18 = ['new_user']
        b19 = pd.concat([b16, b17])
        b20 = cosine_similarity(b19)
        b20 = pd.DataFrame(b20, b18=b19.b18, columns=b19.b18)
        b21 = b20['new_user'].iloc[:-1]
        b22 = b21.nlargest(3).b18.values
        b23 = pd.DataFrame({
            'id_movie': b16.loc[b22].nlargest(N * 2).b18.values.flatten(),
            'score': b16.loc[b22].nlargest(N * 2).values.flatten()
        })
        b23 = sklearn.utils.shuffle(b23)
        b23 = b23.sort_values(by='score', ascending=False)
        b24 = b23['id_movie'].unique()
        b25 = [b8[id_nb] for id_nb in b24
                              if (id_nb not in b10) and (len(b25) < N)]
        return b25
    def fonk7(self, b11, N, b6, b8, b5):
        b26 = './data/'
        b27 = b26 + 'nmf_model_rating.bin'
        if not os.path.exists(b27):
            b28 = self.fonk8(b5, b27)
        else:
            with open(b27, 'rb') as f:
                b28 = pickle.load(f)
        b15 = pd.DataFrame(b11, b18=b6).T.fillna(2.5)
        b29 = b28.transform(b15)
        b30 = b28.inverse_transform(b29)
        b31 = pd.DataFrame(b30.reshape(-1), b18=b6).T
        b32 = np.isnan(b15)
        b33 = b31[b32]
        b34 = b33.T.sort_values(by=[0], ascending=False).b18[:N]
        b25 = [b8[id_nb] for id_nb in b34]
        return b25
    def fonk8(self, b5, b27):
        b35 = pd.pivot_table(b5, 'rating', 'userId', 'movieId').fillna(b5['rating'].median())
        b36 = NMF(n_components=25, max