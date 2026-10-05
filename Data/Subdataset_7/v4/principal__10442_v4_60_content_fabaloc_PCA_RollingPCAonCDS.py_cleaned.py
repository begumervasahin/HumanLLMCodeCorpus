
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from openpyxl import load_workbook
b1 = '~/Itraxxdata_22Mar19_04Jun19.xlsx'
b2 = pd.read_excel(b1, b24='Itraxx')
b2['Date'] = pd.to_datetime(b2['Date'])
b2['Date'] = b2['Date'].dt.strftime('%Y-%b13-%b12')
b3 = pd.to_datetime(b2['Date'])
b3 = b3.dt.strftime('%Y-%b13-%b12')
b2 = b2.iloc[:, 1:].set_index(b3)
b4 = ['S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y', 'S30_3Y', 'S30_5Y', 'S30_7Y', 'S30_10Y',
             'S28_3Y', 'S28_5Y', 'S28_7Y', 'S28_10Y', 'S26_3Y', 'S26_5Y', 'S26_7Y', 'S26_10Y',
             'S24_5Y', 'S24_7Y', 'S24_10Y']
b2.b5 = b4
b6 = ['S26_3Y', 'S24_5Y', 'S28_3Y', 'S30_3Y', 'S26_5Y',
             'S31_3Y', 'S24_7Y', 'S28_5Y', 'S26_7Y',
             'S30_5Y', 'S31_5Y', 'S28_7Y', 'S24_10Y',
             'S30_7Y', 'S31_7Y', 'S26_10Y', 'S28_10Y',
             'S30_10Y', 'S31_10Y']
b2 = b2.reindex(b5=b6)
plt.figure(b7 = (8, 4))
plt.plot(b2.T)
plt.xticks(b8 = 45)
plt.show()
b9 = b2.diff().dropna()
b10 = np.zeros(len(b9) - 1)
for i in range(len(b9) - 1):
    b11 = (b9.index[i] - b9.index[i + 1]).days
    b10[i] = 1 / (np.sqrt(((b11) / 365) * 260))
b12 = b9.mul(b10, axis=0)
n, b13 = b12.shape
a1 = 20
b14 = b3[0:n - a1]
for i in range(n - a1):
    b15 = b12.iloc[i:i + a1, :]
    b16 = StandardScaler(with_std=False).fit_transform(b15)
    b17 = PCA(n_components=3)
    b18 = b17.fit_transform(b16)
    b19 = b17.components_
    b20 = b17.explained_variance_
    b21 = b17.explained_variance_ratio_ * 100
b22 = r'~/PCA_ItraxxMain.xlsx'
with pd.ExcelWriter(b22, b23 = 'openpyxl') as writer:
    b2.to_excel(writer, b24 = 'Original_Data')
    b12.to_excel(writer, b24 = 'DailyChange')
plt.plot(b19[0, :], b25 = 'PC1')
plt.plot(b19[1, :], b25 = 'PC2')
plt.plot(b19[2, :], b25 = 'PC3')
plt.legend()
plt.plot(b19[0, :4], b25 = 'PC1')
plt.plot(b19[1, :4], b25 = 'PC2')
plt.plot(b19[2, :4], b25 = 'PC3')
plt.legend()
plt.plot(b9.iloc[:, :4], b25 = ['res31_3Y', 'res31_5Y', 'res31_7Y', 'res31_10Y'])
plt.legend(b26 = 'upper left', bbox_to_anchor=(1, 0.6))
plt.xticks(np.arange(0, len(b9), b27 = 3))
plt.xlabel('Date')
plt.ylabel('Residual')
plt.gcf().autofmt_xdate()
plt.show()