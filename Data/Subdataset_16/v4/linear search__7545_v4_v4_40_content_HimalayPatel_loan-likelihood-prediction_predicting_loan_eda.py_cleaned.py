import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = pd.read_csv("C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv")
b2 = b1.drop(columns=['entry_id', 'pay_schedule', 'e_signed'])
fig, b3 = plt.subplots(nrows=6, ncols=3, b9=(15, 12))
fig.suptitle('Histograms of Numerical Columns', b4 = 20)
for i, b14 in enumerate(b3.flatten()):
    if i < b2.shape[1]:
        b5 = b2.columns[i]
        b6 = np.size(b2[b5].unique())
        b7 = min(b6, 100)
        b14.hist(b2[b5], b7 = b7, color='blue')
        b14.set_title(b5)
    else:
        b14.axis('off')
plt.tight_layout(b8 = [0, 0.03, 1, 0.95])
plt.show()
plt.figure(b9 = (20, 10))
b2.corrwith(b1['e_signed']).plot.bar(
    b10 = "Correlation with e_signed", b4=15, rot=45, grid=True
)
plt.tight_layout()
plt.show()
sns.set(b11 = "white")
b12 = b2.corr()
b13 = np.triu(np.ones_like(b12, dtype=bool))
fig, b14 = plt.subplots(b9=(18, 15))
b15 = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(b12, b13 = b13, b15=b15, vmax=0.4, center=0,
            b16 = True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()