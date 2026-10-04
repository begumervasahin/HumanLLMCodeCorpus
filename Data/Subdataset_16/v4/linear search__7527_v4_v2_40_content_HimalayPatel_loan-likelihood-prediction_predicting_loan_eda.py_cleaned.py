import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(b17, b18):
    b1 = pd.read_csv(b17)
    b2 = b1.drop(columns=b18)
    return b2
def fonk2(df, b3 = (15, 12), suptitle='Histograms of Numerical Columns'):
    b4 = plt.figure(b3=b3)
    plt.suptitle(suptitle, b5 = 20)
    for i, column in enumerate(df.columns):
        plt.subplot(6, 3, i + 1)
        plt.b10(column)
        b6 = np.size(df[column].unique())
        b7 = min(b6, 100)
        plt.hist(df[column], b7 = b7, color='blue')
    plt.tight_layout(b8 = [0, 0.03, 1, 0.95])
    plt.show()
def fonk3(df, target_column, b3 = (20, 10), b10="Correlation with Target"):
    b9 = df.corrwith(df[target_column])
    b9.plot.bar(b3 = b3, b10=b10, b5=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def fonk4(df, b10 = "Correlation Matrix", b3=(18, 15)):
    sns.set(b11 = "white")
    b12 = df.corr()
    b13 = np.zeros_like(b12, dtype=bool)
    b13[np.triu_indices_from(b13)] = True
    b4, b14 = plt.subplots(b3=b3)
    b15 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b12, b13 = b13, cmap=b15, vmax=0.4, center=0,
                b16 = True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle(b10)
    plt.show()
b17 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b18 = ['entry_id', 'pay_schedule', 'e_signed']
b19 = fonk1(b17, b18)
fonk2(b19)
fonk3(b19, 'e_signed')
fonk4(b19)