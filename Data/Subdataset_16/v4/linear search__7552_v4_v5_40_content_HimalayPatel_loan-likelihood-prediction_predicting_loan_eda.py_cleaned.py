import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b2 = pd.read_csv(b1)
b3 = ['entry_id', 'pay_schedule', 'e_signed']
b4 = b2.drop(columns=b3)
b5 = b4.select_dtypes(include=[np.number]).columns
a1 = 3
b6 = (len(b5) + a1 - 1)
fig, b7 = plt.subplots(nrows=b6, ncols=a1, b15=(15, 12))
fig.suptitle('Histograms of Numerical Columns', b8 = 20)
for index, column_name in enumerate(b5):
    row, b9 = divmod(index, a1)
    b10 = b7[row, b9]
    b10.set_title(column_name)
    b11 = np.size(b4[column_name].unique())
    b12 = min(b11, 100)
    b10.hist(b4[column_name], b12 = b12, color='blue')
for b10 in b7.flat[len(b5):]:
    b10.axis('off')
plt.tight_layout(b13 = [0, 0.03, 1, 0.95])
plt.show()
b14 = b4.corrwith(b2['e_signed'])
b14.plot.bar(b15 = (20, 10), title="Correlation with e_signed", b8=15, rot=45, grid=True)
plt.tight_layout()
plt.show()
sns.set(b16 = "white")
b17 = b4.corr()
b18 = np.triu(np.ones_like(b17, dtype=bool))
fig, b10 = plt.subplots(b15=(18, 15))
b19 = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(b17, b18 = b18, cmap=b19, vmax=0.4, center=0,
            b20 = True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
plt.title("Correlation Matrix", b8 = 20)
plt.show()