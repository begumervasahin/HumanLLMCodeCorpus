import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(b17):
    return pd.read_csv(b17)
def fonk2(b18, b19):
    return b18.drop(b1 = b19)
def fonk3(b18):
    fig, b2 = plt.subplots(nrows=6, ncols=3, b9=(15, 12))
    fig.suptitle('Histograms of Numerical Columns', b3 = 20)
    for index, b13 in enumerate(b2.flat):
        if index < len(b18.b1):
            b4 = b18.b1[index]
            b13.set_title(b4)
            b5 = np.size(b18[b4].unique())
            b6 = min(b5, 100)
            b13.hist(b18[b4], b6 = b6, color='blue')
        else:
            b13.axis('off')
    plt.tight_layout(b7 = [0, 0.03, 1, 0.95])
    plt.show()
def fonk4(b18, target_column):
    b8 = b18.corrwith(target_column)
    b8.plot.bar(b9 = (20, 10), title="Correlation with e_signed", b3=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def fonk5(b18):
    sns.set(b10 = "white")
    b11 = b18.corr()
    b12 = np.zeros_like(b11, dtype=bool)
    b12[np.triu_indices_from(b12)] = True
    fig, b13 = plt.subplots(b9=(18, 15))
    b14 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b11, b12 = b12, cmap=b14, vmax=0.4, center=0,
                b15 = True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle("Correlation Matrix")
    plt.show()
if b16 = = "__main__":
    b17 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
    b18 = fonk1(b17)
    b19 = ['entry_id', 'pay_schedule', 'e_signed']
    b20 = fonk2(b18, b19)
    fonk3(b20)
    fonk4(b20, b18['e_signed'])
    fonk5(b20)