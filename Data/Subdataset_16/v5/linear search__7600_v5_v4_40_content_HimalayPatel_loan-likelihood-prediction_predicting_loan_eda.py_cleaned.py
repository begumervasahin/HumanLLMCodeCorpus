import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b2 = pd.read_csv(b1)
b3 = ['entry_id', 'pay_schedule', 'e_signed']
b4 = b2.drop(columns=b3)
def fonk1(df, b5 = (15, 12)):
    fig, b6 = plt.subplots(nrows=6, ncols=3, b5=b5)
    fig.suptitle('Histograms of Numerical Columns', b7 = 20)
    for i, b16 in enumerate(b6.flatten()):
        if i < df.shape[1]:
            b8 = df.columns[i]
            b9 = np.size(df[b8].unique())
            b10 = min(b9, 100)
            b16.hist(df[b8], b10 = b10, color='blue')
            b16.set_title(b8)
        else:
            b16.axis('off')
    plt.tight_layout(b11 = [0, 0.03, 1, 0.95])
    plt.show()
fonk1(b4)
def fonk2(df, target, b5 = (20, 10)):
    plt.figure(b5 = b5)
    df.corrwith(target).plot.bar(
        b12 = "Correlation with e_signed", b7=15, rot=45, grid=True
    )
    plt.tight_layout()
    plt.show()
fonk2(b4, b2['e_signed'])
def fonk3(df, b5 = (18, 15), vmax=0.4):
    sns.set(b13 = "white")
    b14 = df.corr()
    b15 = np.triu(np.ones_like(b14, dtype=bool))
    fig, b16 = plt.subplots(b5=b5)
    b17 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b14, b15 = b15, b17=b17, vmax=vmax, center=0,
                b18 = True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle("Correlation Matrix")
    plt.show()
fonk3(b4)