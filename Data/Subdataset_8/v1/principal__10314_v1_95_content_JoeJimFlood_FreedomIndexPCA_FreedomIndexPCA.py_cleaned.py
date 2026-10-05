import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.special import erfinv
data = {
    'Countries (2014)': ['Country1', 'Country2', 'Country3', 'Country4', 'Country5'],
    'Economic': [8.3, 7.5, 6.8, 9.2, 5.5],
    'Personal': [7.2, 6.5, 8.1, 5.8, 9.0],
    'Social': [6.9, 5.5, 7.8, 6.2, 8.5]
}
data = pd.DataFrame(data)
X = (data[['Economic', 'Personal', 'Social']].copy())
X -= X.mean(0)
n = X.shape[0]
(U, S, VT) = np.linalg.svd(X.T/np.sqrt(n-1))
projection = np.dot(U.T, X.T).T
data['Combined'] = -projection[:, 0]
data['Combined'] += (5 - data['Combined'].mean())
data.set_index('Countries (2014)').sort_values('Combined', ascending=False).to_csv('IndexData.csv')
data.corr().to_csv('IndexCorrelations.csv')