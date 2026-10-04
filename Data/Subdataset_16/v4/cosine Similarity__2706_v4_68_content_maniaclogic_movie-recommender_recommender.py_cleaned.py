import pandas as pd
import numpy as np
from models import R, nmf, DF
def fonk1(b13):
    b1 = sorted(R.columns)
    b2 = dict(zip(b1, [np.nan] * len(b1)))
    for movie_id, rating in b13.items():
        b2[movie_id] = rating
    b3 = pd.DataFrame([list(b2.values())], columns=b1)
    b4 = b3.fillna(3.0)
    b5 = nmf.transform(b4)
    b6 = np.dot(b5, nmf.components_)
    b7 = pd.DataFrame(b6, columns=R.columns)
    b8 = b3.isna().T[0]
    b9 = b7.T[0][b8]
    b10 = b9.sort_values(ascending=False).index[:5]
    b11 = DF.loc[DF['movieId'].isin(b10), 'title'].values.tolist()
    return b11
if b12 = = "__main__":
    b13 = {
        1: 5.0,
        2: 3.5,
    }
    b11 = fonk1(b13)
    print("Recommended Movies:")
    for movie in b11:
        print(movie)