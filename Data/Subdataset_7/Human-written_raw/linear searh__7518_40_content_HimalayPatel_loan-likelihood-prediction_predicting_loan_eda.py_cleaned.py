import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = pd.read_csv("C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv")
b2 = b1.drop(columns=['entry_id', 'pay_schedule', 'e_signed'])
b3 = plt.figure(b9=(15, 12))
plt.suptitle('Histograms of Numerical Columns', b4 = 20)
for i in range(b2.shape[1]):
    plt.subplot(6, 3, i + 1)
    b5 = plt.gca()
    b5.set_title(b2.columns.values[i])
    b6 = np.size(b2.iloc[:, i].unique())
    if b6 >= 100:
        b6 = 100
    plt.hist(b2.iloc[:, i], b7 = b6, color='
plt.tight_layout(b8 = [0, 0.03, 1, 0.95])
plt.show()
b2.corrwith(b1.e_signed).plot.bar(
        b9 = (20, 10), title = "Correlation with e_signed", b4 = 15,
        b10 = 45, grid = True)
plt.tight_layout()
plt.show()
sns.set(b11 = "white")
b12 = b2.b12()
b13 = np.zeros_like(b12, dtype=np.bool)
b13[np.triu_indices_from(b13)] = True
b5, b14 = plt.subplots(b9=(18, 15))
b15 = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(b12, b13 = b13, b15=b15, vmax=0.4, center=0,
            b16 = True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()