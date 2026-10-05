import numpy as np
import pandas as pd
sample_data = {
    'Countries (2014)': ['Country1', 'Country2', 'Country3', 'Country4', 'Country5'],
    'Economic': [8.3, 7.5, 6.8, 9.2, 5.5],
    'Personal': [7.2, 6.5, 8.1, 5.8, 9.0],
    'Social': [6.9, 5.5, 7.8, 6.2, 8.5]
}
data_frame = pd.DataFrame(sample_data)
def calculate_combined_index(data_frame):
    relevant_columns = data_frame[['Economic', 'Personal', 'Social']].copy()
    standardized_data = relevant_columns - relevant_columns.mean(0)
    n_rows = standardized_data.shape[0]
    U, _, _ = np.linalg.svd(standardized_data.T / np.sqrt(n_rows - 1))
    projection = np.dot(U.T, standardized_data.T).T
    combined_index = -projection[:, 0]
    combined_index += (5 - combined_index.mean())
    return combined_index
data_frame['Combined'] = calculate_combined_index(data_frame)
sorted_data = data_frame.sort_values('Combined', ascending=False).set_index('Countries (2014)')
sorted_data.to_csv('IndexData.csv')
correlation_matrix = data_frame.corr()
correlation_matrix.to_csv('IndexCorrelations.csv')