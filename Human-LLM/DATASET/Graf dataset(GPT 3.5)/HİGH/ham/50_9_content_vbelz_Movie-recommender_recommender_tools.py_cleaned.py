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
        return f
    def fonk3(self):
        b4 = create_engine('sqlite:
        b5 = pd.read_sql_query("SELECT * FROM movie_ratings;", b4)
        b6 = b5['movieId'].unique()
        b7 = b5.groupby('movieId')['title'].first().values
        b8 = dict(zip(b6, b7))
        b9 = dict(zip(b7, b6))
        b10 = self.fonk4(self.b2, b7, b9)
        b11 = self.fonk5(b10, self.b3, b6)
        b12 = self.fonk6(b11, self.b1, b6, b10, b8, b5)
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
        for u_movie_id, u_rating in zip(b10,user_ratings):
            b16[u_movie_id] = float(u_rating)
        b11 = list(b16.values())
        return b11
    def fonk6(self, b11, N, b6, b10, b8, b5):
        b11 = pd.DataFrame(b11, b21=b6).T
        b17 = pd.pivot_table(b5, 'rating', 'userId', 'movieId')
        print(b11)
        b17.fillna(3.0, b18 = True)
        b17 = (b17 - 3.0)/2.0
        b19 = b17.b21
        b20 = b11.fillna(3.0)
        b20 = (b20 - 3.0)/2.0
        b20.b21 = ['new_user']
        b22 = pd.concat([b17,b20])
        b23 = cosine_similarity(b22)
        b23 = pd.DataFrame(b23, b21=b22.b21, columns=b22.b21)
        b24 = b23['new_user'].iloc[:-1]
        b25 = b24.nlargest(3).b21.values
        b26 = []
        b27 = []
        for id_user in b25:
            b26.extend(b17.loc[id_user].nlargest(N*2).b21)
            b27.extend(b17.loc[id_user].nlargest(N*2).values)
        b28 = {'id_movie': b26, 'score': b27}
        b28 = pd.DataFrame(b28)
        b28 = sklearn.utils.shuffle(b28)
        b28 = b28.sort_values(by='score',ascending=False)
        b29 = b28['id_movie'].unique()
        b30 = []
        for id_nb in b29:
            if (id_nb not in b10) and (len(b30) < N) :
                b30.append(b8[id_nb])
        return b30
    def fonk7(self, b11, N, b6, b8, b5):
        b31 = './data/'
        if not os.path.exists(b31+'nmf_model_rating.bin'):
                b32 = self.train_nmf_model(b5)
        else:
            b33 = open(b31+'nmf_model_rating.bin', 'rb').read()
            b32 = pickle.loads(b33)
        b11 = pd.DataFrame(b11, b21=b6).T
        print(b11)
        b34 = b11.fillna(2.5)
        b35 = b32.transform(b34)
        b36 = b32.inverse_transform(b35)
        b37 = pd.DataFrame(b36.reshape(-1), b21=b6).T
        b38 = np.isnan(b11)
        b39 = b37[b38]
        b40 = b39.T.sort_values(by=[0], ascending=False).b21[:N]
        b30 = []
        for id_nb in b40:
            b30.append(b8[id_nb])
        return b30
        def fonk8(self, b5):
            b41 = pd.pivot_table(df_merge, 'rating', 'userId', 'movieId')
            b41.fillna(b41.median(), b18 = True)
            b42 = NMF(n_components=25, max_iter=500)
            b42.fit(b41)
            b33 = pickle.dumps(m)
            open(b31+'nmf_model_rating.bin', 'wb').write(b33)
        return