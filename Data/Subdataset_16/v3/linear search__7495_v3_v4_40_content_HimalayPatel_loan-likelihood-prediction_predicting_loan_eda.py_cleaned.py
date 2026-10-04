
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b2 = pd.read_csv(b1)
b3 = ['entry_id', 'pay_schedule', 'e_signed']
b4 = b2.drop(columns=b3)
def fonk1(data, b5 = (15, 12)):
    fig, b6 = plt.subplots(nrows=6, ncols=3, b5=b5)
    fig.suptitle('Histograms of Numerical Columns', b7 = 20)
    for i, column in enumerate(data.columns):
        b8 = b6[i
        b9 = min(np.size(data[column].unique()), 100)
        b8.hist(data[column], b10 = b9, color='blue')
        b8.set_title(column)
    plt.tight_layout(b11 = [0, 0.03, 1, 0.95])
    plt.show()
fonk1(b4)
def fonk2(data, target, b5 = (20, 10)):
    b12 = data.corrwith(target)
    b12.plot.bar(b5 = b5, title="Correlation with e_signed", b7=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
fonk2(b4, b2['e_signed'])
def fonk3(data, b5 = (18, 15), vmax=0.4):
    sns.set(b13 = "white")
    b14 = data.corr()
    b15 = np.triu(np.ones_like(b14, dtype=bool))
    fig, b8 = plt.subplots(b5=b5)
    b16 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b14, b15 = b15, cmap=b16, vmax=vmax, center=0,
                b17 = True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.title("Correlation Matrix", b7 = 20)
    plt.show()
fonk3(b4)