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
b1 = pd.DataFrame(b1)
b2 = (b1[['Economic', 'Personal', 'Social']].copy())
b2 -= b2.mean(0)
b3 = b2.shape[0]
(U, S, VT) = np.linalg.svd(b2.T/np.sqrt(b3-1))
b4 = np.dot(U.T, b2.T).T
b1['Combined'] = -b4[:, 0]
b1['Combined'] += (5 - b1['Combined'].mean())
b1.set_index('Countries (2014)').sort_values('Combined', b5 = False).to_csv('IndexData.csv')
b1.corr().to_csv('IndexCorrelations.csv')