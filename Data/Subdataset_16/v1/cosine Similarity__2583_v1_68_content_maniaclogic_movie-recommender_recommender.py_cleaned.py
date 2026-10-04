import pandas as pd
import numpy as np
from models import R, nmf, DF
def fonk1(b13):
    b1 = sorted(list(R.columns))
    b2 = [np.nan] * len(b1)
    b3 = dict(zip(b1, b2))
    for key, value in b13.items():
        b3[key] = value
    b4 = pd.DataFrame([list(b3.values())], columns=b1)
    b5 = b4.fillna(3.0)
    b6 = nmf.transform(b5)
    b7 = np.dot(b6, nmf.components_)
    b8 = pd.DataFrame(b7, columns=R.columns)
    b9 = b8.T[0][b4.isna().T[0]]
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