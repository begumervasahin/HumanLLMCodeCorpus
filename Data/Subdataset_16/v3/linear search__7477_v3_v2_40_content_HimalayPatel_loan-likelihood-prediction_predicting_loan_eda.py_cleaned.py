import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(dataframe, columns_to_remove):
    return dataframe.drop(b1 = columns_to_remove)
def fonk3(dataframe):
    b2 = dataframe.shape[1]
    b3 = (b2
    b4 = plt.figure(b11=(15, 12))
    plt.suptitle('Histograms of Numerical Columns', b5 = 20)
    for index, column in enumerate(dataframe.b1):
        plt.subplot(b3, 3, index + 1)
        plt.gca().set_title(column)
        b6 = np.size(dataframe[column].unique())
        b7 = min(b6, 100)
        plt.hist(dataframe[column], b8 = b7, color='blue')
    plt.tight_layout(b9 = [0, 0.03, 1, 0.95])
    plt.show()
def fonk4(dataframe, target_series):
    b10 = dataframe.corrwith(target_series)
    b10.plot.bar(
        b11 = (20, 10), title="Correlation with e_signed", b5=15,
        b12 = 45, grid=True)
    plt.tight_layout()
    plt.show()
def fonk5(dataframe):
    sns.set(b13 = "white")
    b14 = dataframe.corr()
    b15 = np.zeros_like(b14, dtype=bool)
    b15[np.triu_indices_from(b15)] = True
    b4, b16 = plt.subplots(b11=(18, 15))
    b17 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b14, b15 = b15, cmap=b17, vmax=0.4, center=0,
                b18 = True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle("Correlation Matrix")
    plt.show()
def fonk6():
    b19 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
    b20 = ['entry_id', 'pay_schedule', 'e_signed']
    b21 = fonk1(b19)
    b22 = fonk2(b21, b20)
    fonk3(b22)
    fonk4(b22, b21['e_signed'])
    fonk5(b22)
if b23 = = "__main__":
    fonk6()