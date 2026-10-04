import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv")
dataset_cleaned = dataset.drop(columns=['entry_id', 'pay_schedule', 'e_signed'])
fig, axes = plt.subplots(nrows=6, ncols=3, figsize=(15, 12))
fig.suptitle('Histograms of Numerical Columns', fontsize=20)
for i, ax in enumerate(axes.flatten()):
    if i < dataset_cleaned.shape[1]:
        col = dataset_cleaned.columns[i]
        unique_values = np.size(dataset_cleaned[col].unique())
        bins = min(unique_values, 100)
        ax.hist(dataset_cleaned[col], bins=bins, color='blue')
        ax.set_title(col)
    else:
        ax.axis('off')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
plt.figure(figsize=(20, 10))
dataset_cleaned.corrwith(dataset['e_signed']).plot.bar(
    title="Correlation with e_signed", fontsize=15, rot=45, grid=True
)
plt.tight_layout()
plt.show()
sns.set(style="white")
correlation_matrix = dataset_cleaned.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
fig, ax = plt.subplots(figsize=(18, 15))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=0.4, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()