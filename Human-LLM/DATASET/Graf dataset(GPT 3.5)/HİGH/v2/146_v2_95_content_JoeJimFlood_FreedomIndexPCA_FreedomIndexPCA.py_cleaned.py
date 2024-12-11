
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.special import erfinv
b1 = {
    'Countries (2014)': ['Country1', 'Country2', 'Country3', 'Country4', 'Country5'],
    'Economic': [8.3, 7.5, 6.8, 9.2, 5.5],
    'Personal': [7.2, 6.5, 8.1, 5.8, 9.0],
    'Social': [6.9, 5.5, 7.8, 6.2, 8.5]
}
b2 = pd.DataFrame(b1)
b3 = b2[['Economic', 'Personal', 'Social']].copy()
b4 = b3 - b3.mean(0)
b5 = b4.shape[0]
U, S, b6 = np.linalg.svd(b4.T / np.sqrt(b5 - 1))
b7 = np.dot(U.T, b4.T).T
b2['Combined'] = -b7[:, 0]
b2['Combined'] += (5 - b2['Combined'].mean())
b8 = b2.set_index('Countries (2014)').sort_values('Combined', ascending=False)
b8.to_csv('IndexData.csv')
b9 = b2.corr()
b9.to_csv('IndexCorrelations.csv')