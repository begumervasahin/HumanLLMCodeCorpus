
import numpy as np
import pandas as pd
import os
from scipy.stats import norm
from scipy.special import erfinv
base_path = os.path.split(__file__)[0]
data_file = os.path.join(base_path, 'IndexData.csv')
corr_file = os.path.join(base_path, 'IndexCorrelations.csv')
data = pd.read_csv(data_file).dropna()
X = data[['Economic', 'Personal', 'Social']].copy()
X -= X.mean(0)
n = X.shape[0]
(U, S, VT) = np.linalg.svd(X.T / np.sqrt(n - 1))
projection = np.dot(U.T, X.T).T
data['Combined'] = -projection[:, 0]
data['Combined'] += (5 - data['Combined'].mean())
sorted_data = data.set_index('Countries (2014)').sort_values('Combined', ascending=False)
sorted_data.to_csv(data_file)
correlation_matrix = data.corr()
correlation_matrix.to_csv(corr_file)