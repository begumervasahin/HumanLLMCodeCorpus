'''                                             PRINCIPAL COMPONENT ANALYSIS                                                  '''
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
b1 = os.getcwd()
b2 = pd.read_excel(r'~/Itraxxdata_22Mar19_04Jun19.xlsx',  b54='Itraxx')
b2.head()
b2.tail()
print(b2.dtypes)
b2.isnull().values.sum()
b2['Date'] = pd.to_datetime(b2.Date)
b2['Date'] = b2['Date'].dt.strftime('%Y-%b15-%b13')
b3 = pd.to_datetime(b2.iloc[:,0])
b3 = b3.dt.strftime('%Y-%b15-%b13')
b2 = b2.iloc[:, 1::].set_index(b3)
b4 = ['S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y','S30_3Y', 'S30_5Y', 'S30_7Y', 'S30_10Y',
             'S28_3Y', 'S28_5Y', 'S28_7Y', 'S28_10Y', 'S26_3Y',
             'S26_5Y', 'S26_7Y', 'S26_10Y', 'S24_5Y', 'S24_7Y',
             'S24_10Y']
b2.b5 = b4
b6 = ['S26_3Y', 'S24_5Y', 'S28_3Y', 'S30_3Y','S26_5Y',
     'S31_3Y', 'S24_7Y', 'S28_5Y', 'S26_7Y',
     'S30_5Y', 'S31_5Y',  'S28_7Y', 'S24_10Y',
     'S30_7Y', 'S31_7Y', 'S26_10Y', 'S28_10Y',
     'S30_10Y', 'S31_10Y']
b2 = b2.reindex(b5=b6)
plt.figure(b7 = (8,4))
plt.plot(b2.T)
plt.xticks(b8 = 45)
b9 = b2.iloc[::-1, :].diff()
b9 = b9.set_index(b3[::-1])
b9 = b9[1::].sort_index(ascending=False, axis=0)
b9 = b9.b60[~(b9 == 0).any(axis=1)]
b10 = list(b9.b50)
b10.append(b3[len(b3)-1])
b10 = pd.to_datetime(b10)
b11 = np.zeros(len(b10)-1)
for i in range(len(b10)-1):
    b12 = (b10[i] - b10[i+1]).days
    b11[i] = 1/(np.sqrt(((b12)/365) * 260))
b13 = b9.mul(b11, axis=0)
b14 = b13.describe()
'''                                                             Rolling PCA                                                   '''
n, b15 = b13.shape
a1 = 20
b16 = b3[0:n-a1:]
b17 = np.zeros((n-a1))
b18 = np.zeros((n-a1))
b19 = np.zeros((n-a1))
b20 = pd.DataFrame(data = np.zeros((n-a1, b15)))
b21 = pd.DataFrame(data = np.zeros((n-a1, b15)))
b22 = pd.DataFrame(data = np.zeros((n-a1, b15)))
b23 = np.zeros((n-a1))
b24 = np.zeros((n-a1))
b25 = np.zeros((n-a1))
b26 = np.zeros((n-a1))
b27 = np.zeros((n-a1))
b28 = np.zeros((n-a1))
b29 = pd.DataFrame(data = np.zeros((n-a1, b15)))
b30 = pd.DataFrame(data = np.zeros((n-a1, b15)))
b31 = pd.DataFrame(data = np.zeros((n-a1, b15)))
b32 = pd.DataFrame(data = np.zeros((n-a1, b15)))
for i in range(n-a1):
    b33 = b13.iloc[i:i+a1,:]
    b34 = StandardScaler(with_std=False).fit_transform(b13.iloc[i:i+a1,:])
    b35 = np.b35(b13.iloc[i:i+a1,:], axis=0)
    b36 = np.sqrt(np.var(b13.iloc[i:i+a1, :], axis=0))
    b37 = PCA(n_components=3)
    b38 = b37.fit_transform(b34)
    b39 = b37.components_
    b40 = b37.explained_variance_
    b41 = b37.explained_variance_ratio_ * 100
    b42 = b37.inverse_transform(b38)
    b43 = b42 + b35.values
    b44 = b33 - b43
    b17[i] = b38[0, 0]
    b18[i] = b38[0, 1]
    b19[i] = b38[0, 2]
    b20.iloc[i, :] = b39[0, :]
    b21.iloc[i, :] = b39[1, :]
    b22.iloc[i, :] = b39[2, :]
    b23[i] = b40[0]
    b24[i] = b40[1]
    b25[i] = b40[2]
    b26[i] = b41[0]
    b27[i] = b41[1]
    b28[i] = b41[2]
    b29.iloc[i, :] = b44.iloc[0, :].values
b30 = b20 * np.std(b17)
b31 = b21 * np.std(b18)
b32 = b22 * np.std(b19)
b45 = b17 / np.std(b17)
b46 = b18 / np.std(b18)
b47 = b19 / np.std(b19)
b48 = pd.DataFrame({'scaledscore1': b45,
                             'scaledscore2': b46,
                             'scaledscore3': b47})
b48 = b48.set_index(b16)
b38 = pd.DataFrame({'b17': b17, 'b18': b18, 'b19': b19}, b50=b16)
b20 = b20.set_index(b16)
b20.b5 = b13.b5
b21 = b21.set_index(b16)
b21.b5 = b13.b5
b22 = b22.set_index(b16)
b22.b5 = b13.b5
b30 = b30.set_index(b16)
b30.b5 = b13.b5
b31 = b31.set_index(b16)
b31.b5 = b13.b5
b32 = b32.set_index(b16)
b32.b5 = b13.b5
b29 = b29.set_index(b16)
b29.b5 = b13.b5
from openpyxl import load_workbook
b49 = b2.to_excel(r'~\b49.xlsx',
                                    b50 = True , header = True, b54='Original_Data')
b51 = r'~\b49.xlsx'
b52 = load_workbook(b51)
b53 = pd.ExcelWriter(b51, engine='openpyxl')
b53.b52 = b52
b13.to_excel(b53, b54 = 'DailyChange')
b48.to_excel(b53, b54 = 'Weights_Betas')
b30.to_excel(b53, b54 = 'ScaledCoeff1')
b31.to_excel(b53, b54 = 'ScaledCoeff2')
b32.to_excel(b53, b54 = 'ScaledCoeff3')
b29.to_excel(b53, b54 = 'Residuals')
b53.save()
plt.plot(b20.iloc[0,:], b55 = 'PC1')
plt.plot(b21.iloc[0,:], b55 = 'PC2')
plt.plot(b22.iloc[0,:], b55 = 'PC3')
plt.legend()
b56 = b20[['S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y']]
b56 = b56[::-1]
b57 = b21[['S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y']]
b57 = b57[::-1]
b58 = b22[['S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y']]
b58 = b58[::-1]
plt.plot(b56.iloc[0,:], b55 = 'PC1')
plt.plot(b57.iloc[0,:], b55 = 'PC2')
plt.plot(b58.iloc[0,:], b55 = 'PC3')
plt.legend()
b59 = b29[['S31_3Y', 'S31_5Y', 'S31_7Y', 'S31_10Y']]
b59 = b59[::-1]
plt.plot(b59.iloc[:, 0], b55 = 'res31_3Y')
plt.plot(b59.iloc[:, 1], b55 = 'res31_5Y')
plt.plot(b59.iloc[:, 2], b55 = 'res31_7Y')
plt.plot(b59.iloc[:, 3], b55 = 'res31_10Y')
plt.legend(b60 = 'upper left', bbox_to_anchor=(1, 0.6))
plt.xticks(np.arange(0, len(b29), b61 = 3))
plt.xlabel('Date')
plt.ylabel('Residual')
plt.gcf().autofmt_xdate()
plt.show()