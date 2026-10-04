import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(b19, b20):
    b1 = pd.read_csv(b19)
    b2 = b1.drop(columns=b20)
    return b2
def fonk2(df, b3 = (15, 12), suptitle='Histograms of Numerical Columns'):
    b4 = plt.figure(b3=b3)
    plt.suptitle(suptitle, b5 = 20)
    b6 = df.select_dtypes(include=[np.number]).columns
    b7 = len(b6)
    for i, column in enumerate(b6):
        plt.subplot((b7
        plt.b12(column)
        b8 = df[column].nunique()
        b9 = min(b8, 100)
        plt.hist(df[column], b9 = b9, color='blue')
    plt.tight_layout(b10 = [0, 0.03, 1, 0.95])
    plt.show()
def fonk3(df, target_column, b3 = (20, 10), b12="Correlation with Target"):
    b11 = df.corrwith(df[target_column])
    b11.plot.bar(b3 = b3, b12=b12, b5=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def fonk4(df, b12 = "Correlation Matrix", b3=(18, 15)):
    sns.set(b13 = "white")
    b14 = df.corr()
    b15 = np.zeros_like(b14, dtype=bool)
    b15[np.triu_indices_from(b15)] = True
    b4, b16 = plt.subplots(b3=b3)
    b17 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b14, b15 = b15, cmap=b17, vmax=0.4, center=0,
                b18 = True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle(b12)
    plt.show()
b19 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b20 = ['entry_id', 'pay_schedule', 'e_signed']
b21 = fonk1(b19, b20)
fonk2(b21)
fonk3(b21, 'e_signed')
fonk4(b21)