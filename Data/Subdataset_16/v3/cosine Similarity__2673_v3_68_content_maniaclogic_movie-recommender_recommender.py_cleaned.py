import pandas as pd
import numpy as np
from models import R, nmf, DF
def fonk1(b14):
    b1 = sorted(R.columns)
    b2 = [np.nan] * len(b1)
    b3 = dict(zip(b1, b2))
    for movie_id, rating in b14.items():
        b3[movie_id] = rating
    b4 = pd.DataFrame([list(b3.values())], columns=b1)
    b5 = b4.fillna(3.0)
    b6 = nmf.transform(b5)
    b7 = np.dot(b6, nmf.components_)
    b8 = pd.DataFrame(b7, columns=R.columns)
    b9 = b4.isna().T[0]
    b10 = b8.T[0][b9]
    b11 = b10.sort_values(ascending=False).index[:5]
    b12 = DF.loc[DF['movieId'].isin(b11), 'title'].values.tolist()
    return b12
if b13 = = "__main__":
    b14 = {
        1: 5.0,
        2: 3.5,
    }
    b12 = fonk1(b14)
    print("Recommended Movies:")
    for movie in b12:
        print(movie)