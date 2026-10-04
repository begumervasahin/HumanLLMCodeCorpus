import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b2 = pd.read_csv(b1)
b3 = ['entry_id', 'pay_schedule', 'e_signed']
b4 = b2.drop(columns=b3)
def fonk1(data, b5 = 3):
    b6 = data.select_dtypes(include=[np.number]).columns
    b7 = (len(b6) + b5 - 1)
    fig, b8 = plt.subplots(nrows=b7, ncols=b5, b16=(15, 12))
    fig.suptitle('Histograms of Numerical Columns', b9 = 20)
    for index, column_name in enumerate(b6):
        row, b10 = divmod(index, b5)
        b11 = b8[row, b10]
        b11.set_title(column_name)
        b12 = np.size(data[column_name].unique())
        b13 = min(b12, 100)
        b11.hist(data[column_name], b13 = b13, color='blue')
    for b11 in b8.flat[len(b6):]:
        b11.axis('off')
    plt.tight_layout(b14 = [0, 0.03, 1, 0.95])
    plt.show()
def fonk2(data, target_column):
    b15 = data.corrwith(b2[target_column])
    b15.plot.bar(b16 = (20, 10), title=f"Correlation with {target_column}", b9=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def fonk3(data):
    sns.set(b17 = "white")
    b18 = data.corr()
    b19 = np.triu(np.ones_like(b18, dtype=bool))
    fig, b11 = plt.subplots(b16=(18, 15))
    b20 = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(b18, b19 = b19, cmap=b20, vmax=0.4, center=0,
                b21 = True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
    plt.title("Correlation Matrix", b9 = 20)
    plt.show()
fonk1(b4)
fonk2(b4, 'e_signed')
fonk3(b4)