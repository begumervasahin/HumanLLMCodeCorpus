import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from openpyxl import load_workbook
df = pd.read_excel('Itraxxdata_22Mar19_04Jun19.xlsx', sheet_name='Itraxx')
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
date = pd.to_datetime(df['Date'])
column_names = [
    'S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y', 'S30_3Y', 'S30_5Y', 'S30_7Y', 'S30_10Y',
    'S28_3Y', 'S28_5Y', 'S28_7Y', 'S28_10Y', 'S26_3Y', 'S26_5Y', 'S26_7Y', 'S26_10Y',
    'S24_5Y', 'S24_7Y', 'S24_10Y'
]
df.columns = column_names
new_order = [
    'S26_3Y', 'S24_5Y', 'S28_3Y', 'S30_3Y', 'S26_5Y', 'S31_3Y', 'S24_7Y', 'S28_5Y', 'S26_7Y',
    'S30_5Y', 'S31_5Y', 'S28_7Y', 'S24_10Y', 'S30_7Y', 'S31_7Y', 'S26_10Y', 'S28_10Y', 'S30_10Y', 'S31_10Y'
]
df = df.reindex(columns=new_order)
diff_df = df.diff().dropna()
new_date = diff_df.index
multiplier = np.zeros(len(new_date) - 1)
for i in range(len(new_date) - 1):
    delta = (new_date[i] - new_date[i + 1]).days
    multiplier[i] = 1 / (np.sqrt(((delta) / 365) * 260))
differences = diff_df.mul(multiplier, axis=0)
n_rows, n_cols = differences.shape
window_size = 20
dates = date.iloc[:n_rows - window_size]
residuals = pd.DataFrame(data=np.zeros((n_rows - window_size, n_cols)), index=dates, columns=differences.columns)
for i in range(n_rows - window_size):
    window_data = differences.iloc[i:i + window_size, :]
    window_scaled = StandardScaler(with_std=False).fit_transform(window_data)
    pca = PCA(n_components=3)
    pca_scores = pca.fit_transform(window_scaled)
    loadings = pca.components_
    projected_data = pca.inverse_transform(pca_scores) + window_data.mean().values
    residuals.iloc[i, :] = (window_data - projected_data).iloc[0, :].values
with pd.ExcelWriter('PCA_ItraxxMain.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Original_Data', index=True, header=True)
    diff_df.to_excel(writer, sheet_name='DailyChange', index=True, header=True)
    residuals.to_excel(writer, sheet_name='Residuals', index=True, header=True)
plt.plot(residuals.index, residuals['S31_3Y'], label='res31_3Y')
plt.plot(residuals.index, residuals['S31_5Y'], label='res31_5Y')
plt.plot(residuals.index, residuals['S31_7Y'], label='res31_7Y')
plt.plot(residuals.index, residuals['S31_10Y'], label='res31_10Y')
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.6))
plt.xticks(np.arange(0, len(residuals), step=3))
plt.xlabel('Date')
plt.ylabel('Residual')
plt.gcf().autofmt_xdate()
plt.show()