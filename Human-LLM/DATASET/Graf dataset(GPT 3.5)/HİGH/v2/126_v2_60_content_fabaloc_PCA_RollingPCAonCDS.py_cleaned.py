import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from openpyxl import load_workbook
b1 = pd.read_excel('Itraxxdata_22Mar19_04Jun19.xlsx', b21='Itraxx')
b1['Date'] = pd.to_datetime(b1['Date']).dt.strftime('%Y-%m-%d')
b2 = pd.to_datetime(b1['Date'])
b3 = [
    'S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y', 'S30_3Y', 'S30_5Y', 'S30_7Y', 'S30_10Y',
    'S28_3Y', 'S28_5Y', 'S28_7Y', 'S28_10Y', 'S26_3Y', 'S26_5Y', 'S26_7Y', 'S26_10Y',
    'S24_5Y', 'S24_7Y', 'S24_10Y'
]
b1.b4 = b3
b5 = [
    'S26_3Y', 'S24_5Y', 'S28_3Y', 'S30_3Y', 'S26_5Y', 'S31_3Y', 'S24_7Y', 'S28_5Y', 'S26_7Y',
    'S30_5Y', 'S31_5Y', 'S28_7Y', 'S24_10Y', 'S30_7Y', 'S31_7Y', 'S26_10Y', 'S28_10Y', 'S30_10Y', 'S31_10Y'
]
b1 = b1.reindex(b4=b5)
b6 = b1.diff().dropna()
b7 = b6.index
b8 = np.zeros(len(b7) - 1)
for i in range(len(b7) - 1):
    b9 = (b7[i] - b7[i + 1]).days
    b8[i] = 1 / (np.sqrt(((b9) / 365) * 260))
b10 = b6.mul(b8, axis=0)
n_rows, b11 = b10.shape
a1 = 20
b12 = b2.iloc[:n_rows - a1]
b13 = pd.DataFrame(data=np.zeros((n_rows - a1, b11)), index=b12, b4=b10.b4)
for i in range(n_rows - a1):
    b14 = b10.iloc[i:i + a1, :]
    b15 = StandardScaler(with_std=False).fit_transform(b14)
    b16 = PCA(n_components=3)
    b17 = b16.fit_transform(b15)
    b18 = b16.components_
    b19 = b16.inverse_transform(b17) + b14.mean().values
    b13.iloc[i, :] = (b14 - b19).iloc[0, :].values
with pd.ExcelWriter('PCA_ItraxxMain.xlsx', b20 = 'openpyxl') as writer:
    b1.to_excel(writer, b21 = 'Original_Data', index=True, header=True)
    b6.to_excel(writer, b21 = 'DailyChange', index=True, header=True)
    b13.to_excel(writer, b21 = 'Residuals', index=True, header=True)
plt.plot(b13.index, b13['S31_3Y'], b22 = 'res31_3Y')
plt.plot(b13.index, b13['S31_5Y'], b22 = 'res31_5Y')
plt.plot(b13.index, b13['S31_7Y'], b22 = 'res31_7Y')
plt.plot(b13.index, b13['S31_10Y'], b22 = 'res31_10Y')
plt.legend(b23 = 'upper left', bbox_to_anchor=(1, 0.6))
plt.xticks(np.arange(0, len(b13), b24 = 3))
plt.xlabel('Date')
plt.ylabel('Residual')
plt.gcf().autofmt_xdate()
plt.show()