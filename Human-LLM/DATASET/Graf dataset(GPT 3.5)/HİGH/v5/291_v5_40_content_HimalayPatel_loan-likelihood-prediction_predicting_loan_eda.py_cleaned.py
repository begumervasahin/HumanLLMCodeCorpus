
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
b2 = pd.read_csv(b1)
b3 = ['entry_id', 'pay_schedule', 'e_signed']
b4 = b2.drop(columns=b3)
fig, b5 = plt.subplots(nrows=6, ncols=3, b12=(15, 12))
fig.suptitle('Histograms of Numerical Columns', b6 = 20)
for index, b16 in enumerate(b5.flat):
    b7 = b4.columns[index]
    b16.set_title(b7)
    b8 = np.size(b4[b7].unique())
    if b8 >= 100:
        b8 = 100
    b16.hist(b4[b7], b9 = b8, color='blue')
plt.tight_layout(b10 = [0, 0.03, 1, 0.95])
plt.show()
b11 = b4.corrwith(b2['e_signed'])
b11.plot.bar(b12 = (20, 10), title="Correlation with e_signed", b6=15, rot=45, grid=True)
plt.tight_layout()
plt.show()
sns.set(b13 = "white")
b14 = b4.corr()
b15 = np.zeros_like(b14, dtype=np.bool)
b15[np.triu_indices_from(b15)] = True
fig, b16 = plt.subplots(b12=(18, 15))
b17 = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(b14, b15 = b15, cmap=b17, vmax=0.4, center=0,
            b18 = True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()