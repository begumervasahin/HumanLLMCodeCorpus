
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
dataset = pd.read_csv(file_path)
columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
dataset_filtered = dataset.drop(columns=columns_to_drop)
fig, axes = plt.subplots(nrows=6, ncols=3, figsize=(15, 12))
fig.suptitle('Histograms of Numerical Columns', fontsize=20)
for index, ax in enumerate(axes.flat):
    column_name = dataset_filtered.columns[index]
    ax.set_title(column_name)
    unique_values = np.size(dataset_filtered[column_name].unique())
    if unique_values >= 100:
        unique_values = 100
    ax.hist(dataset_filtered[column_name], bins=unique_values, color='blue')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
correlation_with_target = dataset_filtered.corrwith(dataset['e_signed'])
correlation_with_target.plot.bar(figsize=(20, 10), title="Correlation with e_signed", fontsize=15, rot=45, grid=True)
plt.tight_layout()
plt.show()
sns.set(style="white")
correlation_matrix = dataset_filtered.corr()
mask = np.zeros_like(correlation_matrix, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(18, 15))
color_map = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=0.4, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()