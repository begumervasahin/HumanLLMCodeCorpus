import pandas as pd
import numpy as np
from models import R, nmf, DF
b1 = def fonk1(dic):
    b2 = sorted(list(R.columns))
    b3 = [np.nan]*len(b2)
    b4 = dict(zip(b2, b3))
    for key, value in dic.items():
        b4[key] = value
    b5 = list(b4.values())
    b6 = pd.DataFrame(b5, index = b2)
    b6 = b6.transpose()
    b7 = b6.fillna(3.0)
    b8 = nmf.transform(b7)
    b9 = np.dot(b8, nmf.components_)
    b10 = pd.DataFrame(b9, columns = R.columns)
    b11 = b10.transpose()[0][np.isnan(profile_floats[0])]
    b12 = pd.DataFrame(b11)
    b13 = list(b12[0].sort_values(ascending=False).index[:5])
    b14 = [DF['title'].values[each] for each in b13]
    return b14