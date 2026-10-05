import numpy as np
import pandas as pd
import os
from scipy.stats import norm
from scipy.special import erfinv
base_path = os.path.dirname(__file__)
data_file = os.path.join(base_path, 'IndexData.csv')
corr_file = os.path.join(base_path, 'IndexCorrelations.csv')
data = pd.read_csv(data_file).dropna()
index_columns = ['Economic', 'Personal', 'Social']
X = data[index_columns].copy()
X_standardized = X - X.mean()
U, S, VT = np.linalg.svd(X_standardized.T / np.sqrt(X_standardized.shape[0] - 1))
projection = np.dot(U.T, X_standardized.T).T
combined_index = -projection[:, 0]
combined_index += (5 - combined_index.mean())
data['Combined'] = combined_index
sorted_data = data.set_index('Countries (2014)').sort_values('Combined', ascending=False)
sorted_data.to_csv(data_file)
correlation_matrix = data.corr()
correlation_matrix.to_csv(corr_file)