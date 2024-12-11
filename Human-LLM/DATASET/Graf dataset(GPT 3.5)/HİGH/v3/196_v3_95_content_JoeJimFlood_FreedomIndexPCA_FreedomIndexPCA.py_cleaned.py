import numpy as np
import pandas as pd
b1 = {
    'Countries (2014)': ['Country1', 'Country2', 'Country3', 'Country4', 'Country5'],
    'Economic': [8.3, 7.5, 6.8, 9.2, 5.5],
    'Personal': [7.2, 6.5, 8.1, 5.8, 9.0],
    'Social': [6.9, 5.5, 7.8, 6.2, 8.5]
}
b2 = pd.DataFrame(b1)
def fonk1(b2):
    b3 = b2[['Economic', 'Personal', 'Social']].copy()
    b4 = b3 - b3.mean(0)
    b5 = b4.shape[0]
    U, b6, b6 = np.linalg.svd(b4.T / np.sqrt(b5 - 1))
    b7 = np.dot(U.T, b4.T).T
    b8 = -b7[:, 0]
    b8 += (5 - b8.mean())
    return b8
b2['Combined'] = fonk1(b2)
b9 = b2.sort_values('Combined', ascending=False).set_index('Countries (2014)')
b9.to_csv('IndexData.csv')
b10 = b2.corr()
b10.to_csv('IndexCorrelations.csv')