
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
data_frame = pd.DataFrame(data)
economic_personal_social = data_frame[['Economic', 'Personal', 'Social']].copy()
standardized_data = economic_personal_social - economic_personal_social.mean(0)
n_rows = standardized_data.shape[0]
U, S, VT = np.linalg.svd(standardized_data.T / np.sqrt(n_rows - 1))
projection = np.dot(U.T, standardized_data.T).T
data_frame['Combined'] = -projection[:, 0]
data_frame['Combined'] += (5 - data_frame['Combined'].mean())
sorted_data = data_frame.set_index('Countries (2014)').sort_values('Combined', ascending=False)
sorted_data.to_csv('IndexData.csv')
correlation_matrix = data_frame.corr()
correlation_matrix.to_csv('IndexCorrelations.csv')