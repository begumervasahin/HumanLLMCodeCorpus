import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from openpyxl import load_workbook
def fonk1(b23, b1 = 'Itraxx'):
    b2 = pd.read_excel(b23, b1=b1)
    b2['Date'] = pd.to_datetime(b2['Date']).dt.strftime('%Y-%m-%d')
    return b2
def fonk2(b2):
    b3 = [
        'S26_3Y', 'S24_5Y', 'S28_3Y', 'S30_3Y', 'S26_5Y', 'S31_3Y', 'S24_7Y', 'S28_5Y', 'S26_7Y',
        'S30_5Y', 'S31_5Y', 'S28_7Y', 'S24_10Y', 'S30_7Y', 'S31_7Y', 'S26_10Y', 'S28_10Y', 'S30_10Y', 'S31_10Y'
    ]
    b2 = b2[b3]
    return b2
def fonk3(b2):
    b4 = b2.diff().dropna()
    return b4
def fonk4(b4):
    b5 = b4.index
    b6 = np.zeros(len(b5) - 1)
    for i in range(len(b5) - 1):
        b7 = (b5[i] - b5[i + 1]).days
        b6[i] = 1 / (np.sqrt(((b7) / 365) * 260)))
    return b4.mul(b6, b8 = 0)
def fonk5(b4, b9 = 20):
    b10 = pd.DataFrame()
    for i in range(len(b4) - b9):
        b11 = b4.iloc[i:i + b9]
        b12 = StandardScaler(with_std=False).fit_transform(b11)
        b13 = PCA(n_components=3)
        b14 = b13.fit_transform(b12)
        b15 = b13.components_
        b16 = b13.inverse_transform(b14) + b11.mean().values
        b17 = (b11 - b16).iloc[0]
        b10 = b10.append(b17, ignore_index=True)
    return b10
def fonk6(b2, diff_df, b10, b18 = 'PCA_ItraxxMain.xlsx'):
    with pd.ExcelWriter(b18, b19 = 'openpyxl') as writer:
        b2.to_excel(writer, b1 = 'Original_Data', index=True, header=True)
        diff_df.to_excel(writer, b1 = 'DailyChange', index=True, header=True)
        b10.to_excel(writer, b1 = 'Residuals', index=True, header=True)
def fonk7(b10):
    for column in b10.columns:
        plt.plot(b10.index, b10[column], b20 = column)
    plt.legend(b21 = 'upper left', bbox_to_anchor=(1, 0.6))
    plt.xticks(np.arange(0, len(b10), b22 = 3))
    plt.xlabel('Date')
    plt.ylabel('Residual')
    plt.gcf().autofmt_xdate()
    plt.show()
def fonk8():
    b23 = 'Itraxxdata_22Mar19_04Jun19.xlsx'
    b2 = fonk1(b23)
    b2 = fonk2(b2)
    b4 = fonk3(b2)
    b4 = fonk4(b4)
    b10 = fonk5(b4)
    fonk6(b2, b4, b10)
    fonk7(b10)
if b24 = = "__main__":
    fonk8()