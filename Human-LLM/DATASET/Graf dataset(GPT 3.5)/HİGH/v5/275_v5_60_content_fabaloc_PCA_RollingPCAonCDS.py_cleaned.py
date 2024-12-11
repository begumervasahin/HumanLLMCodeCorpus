import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from openpyxl import load_workbook
b1 = '~/Itraxxdata_22Mar19_04Jun19.xlsx'
b2 = pd.read_excel(b1, b19='Itraxx')
b2['Date'] = pd.to_datetime(b2['Date']).dt.strftime('%Y-%b10-%b9')
b2 = b2.iloc[:, 1:].set_index('Date')
b3 = ['S26_3Y', 'S24_5Y', 'S28_3Y', 'S30_3Y', 'S26_5Y',
                'S31_3Y', 'S24_7Y', 'S28_5Y', 'S26_7Y',
                'S30_5Y', 'S31_5Y', 'S28_7Y', 'S24_10Y',
                'S30_7Y', 'S31_7Y', 'S26_10Y', 'S28_10Y',
                'S30_10Y', 'S31_10Y']
b2 = b2.reindex(columns=b3)
plt.figure(b4 = (8, 4))
plt.plot(b2.T)
plt.xticks(b5 = 45)
plt.show()
b6 = b2.diff().dropna()
b7 = np.zeros(len(b6) - 1)
for i in range(len(b6) - 1):
    b8 = (b6.index[i] - b6.index[i + 1]).days
    b7[i] = 1 / (np.sqrt(((b8) / 365) * 260))
b9 = b6.mul(b7, axis=0)
n, b10 = b9.shape
a1 = 20
b11 = b2.index[0:n - a1]
for i in range(n - a1):
    b12 = b9.iloc[i:i + a1, :]
    b13 = StandardScaler(with_std=False).fit_transform(b12)
    b14 = PCA(n_components=3)
    b15 = b14.fit_transform(b13)
    b16 = b14.components_
b17 = r'~/PCA_ItraxxMain.xlsx'
with pd.ExcelWriter(b17, b18 = 'openpyxl') as writer:
    b2.to_excel(writer, b19 = 'Original_Data')
    b9.to_excel(writer, b19 = 'DailyChange')
plt.plot(b16[0, :], b20 = 'PC1')
plt.plot(b16[1, :], b20 = 'PC2')
plt.plot(b16[2, :], b20 = 'PC3')
plt.legend()
plt.plot(b16[0, :4], b20 = 'PC1')
plt.plot(b16[1, :4], b20 = 'PC2')
plt.plot(b16[2, :4], b20 = 'PC3')
plt.legend()
plt.plot(b6.iloc[:, :4], b20 = ['res31_3Y', 'res31_5Y', 'res31_7Y', 'res31_10Y'])
plt.legend(b21 = 'upper left', bbox_to_anchor=(1, 0.6))
plt.xticks(np.arange(0, len(b6), b22 = 3))
plt.xlabel('Date')
plt.ylabel('Residual')
plt.gcf().autofmt_xdate()
plt.show()