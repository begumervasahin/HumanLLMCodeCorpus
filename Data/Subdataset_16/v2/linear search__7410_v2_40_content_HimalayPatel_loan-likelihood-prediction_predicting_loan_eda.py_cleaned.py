import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = pd.read_csv("C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv")
b2 = ['entry_id', 'pay_schedule', 'e_signed']
b3 = b1.drop(columns=b2)
b4 = plt.figure(b11=(15, 12))
plt.suptitle('Histograms of Numerical Columns', b5 = 20)
for i, column in enumerate(b3.columns):
    plt.subplot(6, 3, i + 1)
    b6 = plt.gca()
    b6.set_title(column)
    b7 = np.size(b3[column].unique())
    if b7 >= 100:
        b7 = 100
    plt.hist(b3[column], b8 = b7, color='blue')
plt.tight_layout(b9 = [0, 0.03, 1, 0.95])
plt.show()
b10 = b3.corrwith(b1['e_signed'])
b10.plot.bar(
    b11 = (20, 10), title="Correlation with e_signed", b5=15,
    b12 = 45, grid=True)
plt.tight_layout()
plt.show()
sns.set(b13 = "white")
b14 = b3.corr()
b15 = np.zeros_like(b14, dtype=np.bool)
b15[np.triu_indices_from(b15)] = True
b4, b16 = plt.subplots(b11=(18, 15))
b17 = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(b14, b15 = b15, cmap=b17, vmax=0.4, center=0,
            b18 = True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()